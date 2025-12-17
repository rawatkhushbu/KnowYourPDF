# 📄 PDF Bot – AI-Powered Document Question Answering System

## 🚀 Project Overview

PDF Bot is an **AI-powered knowledge assistant** that allows users to upload PDF documents and ask questions in natural language. The system intelligently retrieves relevant information from the document and generates accurate answers using **Retrieval-Augmented Generation (RAG)**.

This project is designed to demonstrate practical use of **Generative AI, LangChain, vector databases, and LLM-based question answering**, making it suitable for **data science, ML, and GenAI roles**.

---

## 🎯 Key Features

* Upload one or multiple PDF documents
* Ask questions in natural language
* Context-aware and accurate answers using RAG
* Efficient semantic search over large documents
* Simple and interactive web interface

---

## 🧠 Tech Stack Used

* **Programming Language:** Python
* **Frontend / UI:** Streamlit
* **LLM Framework:** LangChain
* **Vector Database:** FAISS
* **Embeddings:** Hugging Face / OpenAI Embeddings
* **Document Loader:** PyPDFLoader
* **Deployment:** Streamlit Cloud

---

## 🛠️ System Workflow

1. User uploads PDF documents through the Streamlit interface.
2. PDF text is extracted and split into smaller chunks.
3. Text chunks are converted into vector embeddings.
4. Embeddings are stored in FAISS for fast semantic search.
5. User query is embedded and matched with relevant chunks.
6. Retrieved context is passed to the LLM.
7. LLM generates a precise answer based on the document content.

---

## 📂 Project Structure

```
PDF-Bot/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── utils/                 # Helper functions (if any)
├── data/                  # Sample PDFs (optional)
├── faiss_index/           # Stored vector embeddings
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-bot.git
cd pdf-bot
```

2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
source venv/bin/activate  # For Linux/Mac
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
streamlit run app.py
```

---

## 📊 Use Cases

* Academic document analysis
* Research paper Q&A
* Resume or policy document understanding
* Knowledge assistant for large PDFs

---

## 🧪 Testing Strategy

* Manual testing with multiple PDFs
* Validation of answers with document references
* Edge case testing for empty or large documents

---

## 🌱 Future Enhancements

* Support for DOCX and TXT files
* Chat history and conversation memory
* Source citation for answers
* Authentication for multiple users
* Advanced LLM model integration

---

## 👩‍💻 Author

**Khushbu Rawat**
Final Year BCA Student | Aspiring Data Scientist / ML Engineer

---

## ⭐ Acknowledgements

* LangChain Documentation
* Streamlit Community
* OpenAI / Hugging Face

---

⭐ *If you find this project useful, please consider starring the repository!*
