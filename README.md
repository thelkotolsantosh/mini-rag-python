# Mini RAG Python

A small, beginner-friendly **Retrieval-Augmented Generation (RAG)-style document search project** written in Python.

This project teaches the retrieval part of RAG without requiring an API key, paid service, vector database, or large language model. It loads documents, converts text into simple TF-IDF-style vectors, compares a user's question with the documents, and returns the most relevant results.

## Repository name

`mini-rag-python`

## What this project does

When you type a question such as:

```text
What is retrieval augmented generation?
```

the program:

1. Loads documents from `data/documents.json`.
2. Breaks text into words.
3. Builds TF-IDF-style vectors.
4. Measures similarity between your question and every document.
5. Returns the most relevant documents with similarity scores.

This is the **retrieval** stage used in many RAG systems.

## Features

- Pure Python retrieval engine
- No OpenAI API key required
- No paid services
- No external runtime dependencies
- Command-line interface
- Sample documents included
- Unit tests included
- GitHub Actions workflow included
- Clean project structure
- Easy to extend later with embeddings, FAISS, ChromaDB, Ollama, or OpenAI

## Project structure

```text
mini-rag-python/
├── .github/
│   └── workflows/
│       └── tests.yml
├── data/
│   └── documents.json
├── src/
│   └── mini_rag/
│       ├── __init__.py
│       ├── cli.py
│       └── search.py
├── tests/
│   └── test_search.py
├── .gitignore
├── app.py
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
├── requirements-dev.txt
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- Git (optional, but recommended)
- GitHub account if you want to publish the project

## Quick start

### 1. Download or clone the project

If you created an empty GitHub repository:

```bash
git clone https://github.com/YOUR-USERNAME/mini-rag-python.git
cd mini-rag-python
```

Then copy all project files into that folder.

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install requirements

The application itself uses only Python's standard library, so there are no mandatory third-party runtime packages.

```bash
pip install -r requirements.txt
```

For development and testing:

```bash
pip install -r requirements-dev.txt
```

### 4. Run the application

```bash
python app.py
```

You should see:

```text
Mini RAG Document Search
Type a question, or type 'exit' to quit.
```

Example:

```text
Question: What is RAG?
```

The program will print the most relevant documents.

## Run a single query

You can also pass your question directly:

```bash
python app.py "What is a vector database?"
```

## Example output

```text
Query: What is retrieval augmented generation?

1. Retrieval-Augmented Generation
   Score: 0.6241
   RAG combines information retrieval with language generation...
```

The exact score can vary if you change the sample documents.

## Add your own documents

Open:

```text
data/documents.json
```

Add an object in this format:

```json
{
  "id": 6,
  "title": "My Document",
  "content": "Write the document content here."
}
```

Save the file and restart the program.

## Run tests

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Then run:

```bash
pytest
```

## How the search works

The program uses a lightweight TF-IDF-style scoring approach.

### Term Frequency

Term frequency measures how often a word appears in a document.

```text
TF = word count / total words in document
```

### Inverse Document Frequency

IDF gives more importance to words that are uncommon across the document collection.

```text
IDF = log((1 + number of documents) / (1 + documents containing word)) + 1
```

### Cosine similarity

After creating vectors for the query and documents, cosine similarity measures how closely they point in the same direction.

A higher similarity score means the document is more relevant to the question.

## Why this project is useful for learning RAG

A production RAG application normally contains:

```text
Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Database
   ↓
Similarity Search
   ↓
Relevant Context
   ↓
LLM
   ↓
Answer
```

This repository focuses on the retrieval/search part:

```text
Documents
   ↓
Text Vectorization
   ↓
Similarity Search
   ↓
Relevant Documents
```

Once you understand this project, you can replace the simple vectorizer with a real embedding model.

## Ideas for version 2

You can extend this project with:

- Sentence Transformers
- FAISS
- ChromaDB
- Ollama
- OpenAI embeddings
- PDF upload
- Streamlit web interface
- Chat history
- Source citations
- Document chunking
- Local LLM integration

## GitHub upload instructions

Create a new repository on GitHub named:

```text
mini-rag-python
```

Do not add another README, `.gitignore`, or license if you are uploading this complete project.

Then, from the project folder:

```bash
git init
git add .
git commit -m "Initial commit: Mini RAG Python project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/mini-rag-python.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Suggested GitHub description

```text
A beginner-friendly Mini RAG document search engine built in Python using TF-IDF-style retrieval and cosine similarity.
```

## Suggested GitHub topics

```text
python
rag
retrieval-augmented-generation
information-retrieval
nlp
machine-learning
ai
document-search
cosine-similarity
beginner-project
```

## License

This project is licensed under the MIT License. See `LICENSE`.

## Author

Replace this section with your name and GitHub profile.

Example:

```text
Your Name
GitHub: https://github.com/YOUR-USERNAME
```
