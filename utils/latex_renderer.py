import re
import streamlit as st


def _normalize_latex(text: str) -> str:
    """
    Fix common LaTeX formatting issues from LLM or RAG outputs
    """

    if not text:
        return text

    # Convert \[ ... \] → $$ ... $$
    text = re.sub(r"\\\[(.*?)\\\]", r"$$\1$$", text, flags=re.DOTALL)

    # Convert \( ... \) → $ ... $
    text = re.sub(r"\\\((.*?)\\\)", r"$\1$", text, flags=re.DOTALL)

    # Remove stray closing brackets
    text = text.replace("\\]", "")
    text = text.replace("\\[", "")

    # Fix common math words
    text = text.replace("implies", r"\implies")

    # Normalize fractions like dy/dx
    text = re.sub(r"\bdy/dx\b", r"\\frac{dy}{dx}", text)

    # sqrt(x) → \sqrt{x}
    text = re.sub(r"sqrt\((.*?)\)", r"\\sqrt{\1}", text)

    return text


def _split_math_blocks(text: str):
    """
    Splits text into normal text and math blocks
    """

    pattern = r"(\$\$.*?\$\$|\$.*?\$)"
    parts = re.split(pattern, text, flags=re.DOTALL)

    return parts


def render_math(text: str):
    """
    Main function to render mixed text + LaTeX in Streamlit
    """

    text = _normalize_latex(text)
    parts = _split_math_blocks(text)

    for part in parts:

        part = part.strip()

        if not part:
            continue

        # Block math
        if part.startswith("$$") and part.endswith("$$"):
            equation = part[2:-2]
            st.latex(equation)

        # Inline math
        elif part.startswith("$") and part.endswith("$"):
            st.markdown(part)

        else:
            st.markdown(part)