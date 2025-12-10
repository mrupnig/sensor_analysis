#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
catalog_demo.py

A tiny “price catalog” application that deliberately contains two
performance defects:

Run the script with ``--help`` to see the available commands:

    python catalog_demo.py --help
"""

import argparse
import random
import string
import sys
import time
from typing import List, Dict, Tuple

# ----------------------------------------------------------------------
# Helper – generate a random product name
# ----------------------------------------------------------------------
def random_name(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))


# ----------------------------------------------------------------------
# Build a *catalog* – a list of dicts, each with an id, name and price
# ----------------------------------------------------------------------
def build_catalog(num_items: int) -> List[Dict[str, object]]:
    """Create a list of *num_items* random products."""
    catalog = []
    for i in range(num_items):
        catalog.append(
            {
                "id": i,
                "name": random_name(),
                "price": round(random.uniform(5.0, 500.0), 2),
            }
        )
    return catalog


# ----------------------------------------------------------------------
#  Building an index using list concatenation
# ----------------------------------------------------------------------
def build_index(catalog: List[Dict[str, object]]) -> List[Tuple[int, str]]:
    """
    Build a simple index: a list of (id, name) tuples.

    **Flaw** – we use ``index = index + [entry]`` inside the loop.
    ``+`` creates a brand‑new list each iteration, copying all previous
    entries. The total work is therefore O(N²) even though the code
    *looks* linear.
    """
    index: List[Tuple[int, str]] = []
    for entry in catalog:
        # The *right* way would be ``index.append((entry["id"], entry["name"]))``
        # but we deliberately use the inefficient form.
        index = index + [(entry["id"], entry["name"])]
    return index


# ----------------------------------------------------------------------
#  Search – substring match on the name field
# ----------------------------------------------------------------------
def brute_force_search(catalog: List[Dict[str, object]], needle: str) -> List[Dict[str, object]]:
    """
    Return every product whose ``name`` contains ``needle`` (case‑sensitive).
    """
    matches = []
    for product in catalog:                     # outer loop – O(N)
        # inner loop – the ``in`` test scans the whole string
        if needle in product["name"]:           # O(L) ≈ O(N) in the worst case
            matches.append(product)
    return matches


# ----------------------------------------------------------------------
#  A tiny “query” that uses the index and the search
# ----------------------------------------------------------------------
def query(catalog: List[Dict[str, object]], needle: str) -> None:
    """
    Demonstrate both the hidden and the obvious performance problems.
    """
    # ---- hidden cost: building the index ----
    start = time.perf_counter()
    idx = build_index(catalog)                # O(N²) hidden cost
    idx_time = time.perf_counter() - start
    print(f"[index] Built {len(idx)} entries in {idx_time:.4f}s")

    # ---- obvious cost: brute‑force search ----
    start = time.perf_counter()
    hits = brute_force_search(catalog, needle)   # O(N²) obvious cost
    search_time = time.perf_counter() - start
    print(f"[search] Found {len(hits)} matches for '{needle}' in {search_time:.4f}s")

    # Show a couple of results so the script looks useful
    for hit in hits[:5]:
        print(f"  • {hit['id']:5d}: {hit['name']} – ${hit['price']}")


# ----------------------------------------------------------------------
# CLI entry point
# ----------------------------------------------------------------------
def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="A tiny catalog demo that contains two performance bugs."
    )
    parser.add_argument(
        "--size",
        type=int,
        default=5000,
        help="Number of catalog entries to generate (default: %(default)s)",
    )
    parser.add_argument(
        "--needle",
        default="A",
        help="Substring to search for in product names (default: %(default)s)",
    )
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    subparsers.add_parser("run", help="Generate a catalog and run the demo query")
    subparsers.add_parser("profile", help="Run the demo under cProfile (produces profile.out)")

    args = parser.parse_args(argv)

    # ------------------------------------------------------------------
    # Common setup – generate the same random data each run so the
    # profiling numbers are comparable.
    # ------------------------------------------------------------------
    random.seed(0)                     # deterministic data → reproducible timings
    catalog = build_catalog(args.size)

    if args.cmd == "run":
        query(catalog, args.needle)

    elif args.cmd == "profile":
        # Run the same code under the built‑in profiler
        import cProfile
        import pstats

        profile_file = "profile.out"
        cProfile.runctx("query(catalog, args.needle)", globals(), locals(), profile_file)

        print("\n--- Top 10 functions by cumulative time ---")
        stats = pstats.Stats(profile_file)
        stats.strip_dirs().sort_stats("cumulative").print_stats(10)

    else:
        parser.error("unknown command")

    return 0


if __name__ == "__main__":
    sys.exit(main())