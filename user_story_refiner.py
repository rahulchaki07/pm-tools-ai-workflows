"""Evaluate and rewrite user stories against a quality rubric."""

from __future__ import annotations

import argparse

from config import call_claude, read_prompt


def build_user_prompt(story: str) -> str:
    return (
        "Review this user story using the quality rubric.\n\n"
        f"User story:\n{story}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Check and refine user story quality.")
    parser.add_argument("--story", required=True, help="Raw user story text.")
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

    system_prompt = read_prompt("story_system.txt")
    result = call_claude(
        system_prompt=system_prompt,
        user_prompt=build_user_prompt(args.story),
        model=args.model,
        max_tokens=args.max_tokens,
    )

    if args.output:
        from pathlib import Path

        output_path = Path(args.output)
        output_path.write_text(result, encoding="utf-8")
        print(f"Refined story analysis written to: {output_path}")
        return

    print(result)


if __name__ == "__main__":
    main()
