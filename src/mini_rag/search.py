"""A tiny dependency-free document retrieval engine.

The implementation intentionally keeps the mathematics readable for beginners.
It uses tokenization, TF-IDF-style vectors, and cosine similarity.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import json
import math
from pathlib import Path
import re
from typing import Iterable


WORD_PATTERN = re.compile(r"[A-Za-z0-9']+")

STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "how", "i", "in", "is", "it", "of", "on", "or", "that", "the",
    "this", "to", "was", "what", "when", "where", "which", "who",
    "why", "with", "you", "your"
}


@dataclass(frozen=True)
class SearchResult:
    """One search result returned by the retriever."""

    id: int
    title: str
    content: str
    score: float


def tokenize(text: str) -> list[str]:
    """Convert text into normalized word tokens."""
    return [token for token in WORD_PATTERN.findall(text.lower()) if token not in STOP_WORDS]


class MiniRAG:
    """Search a small JSON document collection using TF-IDF and cosine similarity."""

    def __init__(self, documents: list[dict]) -> None:
        if not documents:
            raise ValueError("At least one document is required.")

        self.documents = documents
        self.document_tokens = [
            tokenize(f"{doc.get('title', '')} {doc.get('content', '')}")
            for doc in documents
        ]
        self.idf = self._build_idf(self.document_tokens)
        self.document_vectors = [
            self._vectorize(tokens) for tokens in self.document_tokens
        ]

    @classmethod
    def from_json(cls, file_path: str | Path) -> "MiniRAG":
        """Create a search engine from a JSON file containing a list of documents."""
        path = Path(file_path)
        with path.open("r", encoding="utf-8") as file:
            documents = json.load(file)

        if not isinstance(documents, list):
            raise ValueError("The JSON file must contain a list of documents.")

        return cls(documents)

    def _build_idf(self, tokenized_documents: Iterable[list[str]]) -> dict[str, float]:
        """Calculate inverse document frequency for every token."""
        docs = list(tokenized_documents)
        document_count = len(docs)
        document_frequency: Counter[str] = Counter()

        for tokens in docs:
            document_frequency.update(set(tokens))

        return {
            token: math.log((1 + document_count) / (1 + frequency)) + 1
            for token, frequency in document_frequency.items()
        }

    def _vectorize(self, tokens: list[str]) -> dict[str, float]:
        """Create a sparse TF-IDF-style vector."""
        if not tokens:
            return {}

        counts = Counter(tokens)
        token_count = len(tokens)

        return {
            token: (count / token_count) * self.idf.get(token, 0.0)
            for token, count in counts.items()
            if token in self.idf
        }

    @staticmethod
    def _cosine_similarity(
        vector_a: dict[str, float], vector_b: dict[str, float]
    ) -> float:
        """Return cosine similarity between two sparse vectors."""
        if not vector_a or not vector_b:
            return 0.0

        shared_tokens = vector_a.keys() & vector_b.keys()
        dot_product = sum(vector_a[token] * vector_b[token] for token in shared_tokens)

        magnitude_a = math.sqrt(sum(value * value for value in vector_a.values()))
        magnitude_b = math.sqrt(sum(value * value for value in vector_b.values()))

        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0

        return dot_product / (magnitude_a * magnitude_b)

    def search(self, query: str, top_k: int = 3) -> list[SearchResult]:
        """Return the top matching documents for a query."""
        if not query.strip():
            return []

        if top_k < 1:
            raise ValueError("top_k must be at least 1.")

        query_vector = self._vectorize(tokenize(query))
        results: list[SearchResult] = []

        for document, document_vector in zip(
            self.documents, self.document_vectors, strict=True
        ):
            score = self._cosine_similarity(query_vector, document_vector)
            results.append(
                SearchResult(
                    id=int(document.get("id", 0)),
                    title=str(document.get("title", "Untitled")),
                    content=str(document.get("content", "")),
                    score=score,
                )
            )

        results.sort(key=lambda item: item.score, reverse=True)

        # Avoid showing unrelated documents when at least one relevant result exists.
        positive_results = [result for result in results if result.score > 0]
        return positive_results[:top_k]
