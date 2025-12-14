import streamlit as st
import tempfile
import base64


from chatbot import create_retriever, build_qa_chain
def add_bg_from_local(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


st.set_page_config(page_title="PDF Q&A Chatbot", page_icon="📄")
add_bg_from_local("background.jpg")

st.title("📄 PDF Q&A Chatbot (Free + Groq)")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    with st.spinner("Processing PDF..."):
        retriever = create_retriever(pdf_path)
        qa_chain = build_qa_chain(retriever)

    st.success("PDF ready! Ask questions below 👇")

    question = st.text_input("Ask a question")

    if question:
        with st.spinner("Thinking..."):
            answer = qa_chain.invoke(question)

        st.markdown("### ✅ Answer")
        st.write(answer)
