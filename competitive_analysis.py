"""Generate a structured competitor analysis for a product/category."""

from __future__ import annotations

import argparse

from config import call_claude, read_prompt


def build_user_prompt(product: str, category: str) -> str:
    return (
        "Create a structured competitor teardown using public information.\n\n"
        f"Product name: {product}\n"
        f"Target category: {category}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a structured competitor analysis."
    )
    parser.add_argument("--product", required=True, help="Competitor product name.")
    parser.add_argument("--category", required=True, help="Target category or market segment.")
    parser.add_argument(
        "--output",
        help="Optional output markdown file path. Prints to stdout if omitted.",
    )
    parser.add_argument("--model", help="Optional Claude model override.")
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=1500,
        help="Maximum tokens in the model response.",
    )
    args = parser.parse_args()

    system_prompt = read_prompt("competitive_system.txt")
    result = call_claude(
        system_prompt=system_prompt,
        user_prompt=build_user_prompt(args.product, args.category),
        model=args.model,
        max_tokens=args.max_tokens,
    )

    if args.output:
        from pathlib import Path

        output_path = Path(args.output)
        output_path.write_text(result, encoding="utf-8")
        print(f"Competitive analysis written to: {output_path}")
        return

    print(result)


if __name__ == "__main__":
    main()
