"""Entry point for Mini RAG Python."""

import sys
from src.mini_rag.cli import interactive_mode, run_single_query


def main() -> None:
    """Start interactive mode or answer a query passed on the command line."""
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        run_single_query(query)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
