"""Tests for the Mini RAG retrieval engine."""

from src.mini_rag.search import MiniRAG, tokenize


SAMPLE_DOCUMENTS = [
    {
        "id": 1,
        "title": "Python",
        "content": "Python is used for automation and artificial intelligence.",
    },
    {
        "id": 2,
        "title": "Databases",
        "content": "A database stores and retrieves information.",
    },
]


def test_tokenize_normalizes_text() -> None:
    assert tokenize("Hello, PYTHON!") == ["hello", "python"]


def test_search_returns_relevant_document_first() -> None:
    engine = MiniRAG(SAMPLE_DOCUMENTS)
    results = engine.search("Python artificial intelligence")

    assert results
    assert results[0].title == "Python"
    assert results[0].score > 0


def test_empty_query_returns_empty_list() -> None:
    engine = MiniRAG(SAMPLE_DOCUMENTS)
    assert engine.search("   ") == []


def test_invalid_top_k_raises_error() -> None:
    engine = MiniRAG(SAMPLE_DOCUMENTS)

    try:
        engine.search("Python", top_k=0)
    except ValueError as error:
        assert "top_k" in str(error)
    else:
        raise AssertionError("Expected ValueError")
