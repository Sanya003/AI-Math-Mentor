import os
import tempfile
import streamlit as st

from utils.ocr import extract_text_from_image
from utils.audio_asr import transcribe_audio
from utils.math_cleaner import normalize_math_text
from utils.latex_renderer import render_math

from rag.build_vectorstore import build_vectorstore, get_knowledge_text, get_text_chunks

from agents.parser_agent import parse_problem
from agents.router_agent import route_problem
from agents.solver_agent import solve_problem
from agents.verifier_agent import verify_solution
from agents.explainer_agent import explain_solution

from memory.memory_store import save_memory, find_similar_memory


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(page_title="AI Math Mentor", layout="wide")

st.title("📘 AI Math Mentor")
st.caption("AI-powered JEE Math Tutor • Multi-agent system")
st.divider()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "solve" not in st.session_state:
    st.session_state.solve = False

if "question" not in st.session_state:
    st.session_state.question = None


# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# --------------------------------------------------
# LOAD KNOWLEDGE BASE
# --------------------------------------------------

@st.cache_resource
def load_knowledge_base():

    kb_path = "knowledge_base"

    texts, metadata = get_knowledge_text(kb_path)

    chunks, chunk_meta = get_text_chunks(texts, metadata)

    vectorstore = build_vectorstore(chunks, chunk_meta)

    return vectorstore


vectorstore = load_knowledge_base()


# --------------------------------------------------
# INPUT MODE
# --------------------------------------------------

input_mode = st.radio(
    "Choose input mode:",
    ["Text", "Image", "Audio"]
)


# --------------------------------------------------
# TEXT INPUT
# --------------------------------------------------

if input_mode == "Text":

    user_prompt = st.chat_input("Type your math question...")

    if user_prompt:
        st.session_state.question = normalize_math_text(user_prompt)
        st.session_state.solve = True


# --------------------------------------------------
# IMAGE INPUT
# --------------------------------------------------

elif input_mode == "Image":

    uploaded_image = st.file_uploader(
        "Upload image of math problem",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_image:

        st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

        extracted_text, conf = extract_text_from_image(uploaded_image)

        st.subheader("OCR Extracted Text")

        edited_text = st.text_area(
            "Edit OCR result if needed",
            extracted_text
        )

        st.write(f"OCR Confidence: {round(conf,2)}")

        if conf < 0.6:
            st.warning("Low OCR confidence. Please verify carefully.")

        if st.button("Solve Problem"):

            st.session_state.question = normalize_math_text(edited_text)
            st.session_state.solve = True


# --------------------------------------------------
# AUDIO INPUT
# --------------------------------------------------

elif input_mode == "Audio":

    uploaded_audio = st.file_uploader(
        "Upload audio",
        type=["wav", "mp3"]
    )

    recorded_audio = st.audio_input("Or record your question")

    audio_bytes = None

    if uploaded_audio:
        audio_bytes = uploaded_audio.read()

    if recorded_audio:
        audio_bytes = recorded_audio.read()

    if audio_bytes:

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(audio_bytes)
            audio_path = tmp.name

        transcript = transcribe_audio(audio_path)

        st.subheader("Audio Transcript")

        edited_text = st.text_area(
            "Confirm or edit transcript",
            transcript
        )

        if st.button("Solve Problem"):

            st.session_state.question = normalize_math_text(edited_text)
            st.session_state.solve = True


# --------------------------------------------------
# MAIN PIPELINE
# --------------------------------------------------

if st.session_state.solve:

    question = st.session_state.question

    if not question:
        st.error("Please provide a question.")
        st.stop()

    st.session_state.solve = False

    # USER MESSAGE
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("AI agents solving the problem..."):

        # MEMORY LOOKUP
        similar = find_similar_memory(question)

        if similar:

            with st.expander("🧠 Similar Solved Problems"):

                for item in similar[:3]:

                    st.markdown(f"**Q:** {item['input']}")
                    st.markdown(f"**A:** {item['final_answer']}")
                    st.divider()

        # PARSER
        parsed_problem = parse_problem(question)

        # ROUTER
        topic = route_problem(parsed_problem)

        # RAG RETRIEVAL
        docs = vectorstore.similarity_search(question, k=3)

        context = "\n\n".join([d.page_content for d in docs])
        sources = [d.metadata.get("source", "") for d in docs]

        with st.chat_message("assistant"):

            with st.container(border=True):

                st.markdown("### 📚 Retrieved Knowledge")

                render_math(context[:512])

        # SOLVER
        solution = solve_problem(
            question,
            parsed_problem,
            context
        )

        # VERIFIER
        confidence, verification_text = verify_solution(
            question,
            solution
        )

        if confidence < 0.5:

            st.warning("Low confidence solution.")

            solution = st.text_area(
                "Edit solution if needed",
                solution
            )

        # EXPLAINER
        explanation = explain_solution(solution)

        # SAVE MEMORY
        save_memory(
            original_input=question,
            parsed_problem=parsed_problem,
            retrieved_context=context,
            final_answer=solution,
            verifier_result=verification_text
        )

    # --------------------------------------------------
    # AI RESPONSE
    # --------------------------------------------------

    with st.chat_message("assistant"):

        st.markdown("## 🧠 Step-by-Step Solution")

        steps = solution.split("STEP")

        step_num = 1

        for step in steps:

            if step.strip():

                with st.expander(f"Step {step_num}", expanded=True):

                    render_math(step.strip())

                step_num += 1

        # FINAL ANSWER
        if "FINAL ANSWER" in solution:

            final = solution.split("FINAL ANSWER:")[-1].strip()

            st.markdown("### ✅ Final Answer")

            render_math(final)

        # EXPLANATION
        st.markdown("### 📖 Explanation")

        st.markdown(explanation)

        # CONFIDENCE
        st.markdown("### 📊 Confidence Score")

        st.progress(confidence)

        # SOURCES
        if sources:

            st.markdown("### 📚 Sources")

            for s in set(sources):

                st.write("-", s)

    assistant_message = f"""
        ### 🧠 Solution

        {solution}

        ### 📖 Explanation

        {explanation}

        Confidence: {round(confidence,2)}
    """

    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_message
    })


# --------------------------------------------------
# FEEDBACK
# --------------------------------------------------

if st.session_state.messages:

    st.divider()

    st.subheader("Feedback")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Correct"):
            st.success("Feedback saved")

    with col2:
        if st.button("❌ Incorrect"):

            comment = st.text_input("What was wrong?")

            if comment:
                st.info("Thanks for the feedback!")

