import os

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


# -----------------------------
# READ TXT FILES
# -----------------------------
def get_knowledge_text(folder_path):

    texts = []
    metadata = []

    for file in os.listdir(folder_path):

        if file.endswith(".md"):

            path = os.path.join(folder_path, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            texts.append(content)
            metadata.append({
                "source": file
            })

    return texts, metadata


# -----------------------------
# SPLIT TEXT INTO CHUNKS
# -----------------------------
def get_text_chunks(texts, metadata):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=120,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = []
    chunk_meta = []

    for i, text in enumerate(texts):

        split = text_splitter.split_text(text)

        for chunk in split:
            chunks.append(chunk)
            chunk_meta.append(metadata[i])

    return chunks, chunk_meta


# -----------------------------
# BUILD VECTOR STORE
# -----------------------------
def build_vectorstore(texts, metadata):

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en"
    )

    vectorstore = FAISS.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadata
    )

    return vectorstore