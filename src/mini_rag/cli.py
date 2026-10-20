"""Command-line interface for Mini RAG."""

from pathlib import Path

from .search import MiniRAG, SearchResult


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_ROOT / "data" / "documents.json"


def load_engine() -> MiniRAG:
    """Load the default document collection."""
    return MiniRAG.from_json(DATA_FILE)


def print_results(query: str, results: list[SearchResult]) -> None:
    """Pretty-print retrieval results."""
    print(f"\nQuery: {query}\n")

    if not results:
        print("No relevant documents were found.")
        return

    for index, result in enumerate(results, start=1):
        print(f"{index}. {result.title}")
        print(f"   Score: {result.score:.4f}")
        print(f"   {result.content}")
        print()


def run_single_query(query: str) -> None:
    """Run one query and print the result."""
    engine = load_engine()
    print_results(query, engine.search(query))


def interactive_mode() -> None:
    """Run the interactive terminal application."""
    engine = load_engine()

    print("=" * 60)
    print("Mini RAG Document Search")
    print("Type a question, or type 'exit' to quit.")
    print("=" * 60)

    while True:
        try:
            query = input("\nQuestion: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if query.lower() in {"exit", "quit", "q"}:
            print("Goodbye!")
            break

        if not query:
            print("Please type a question.")
            continue

        print_results(query, engine.search(query))
