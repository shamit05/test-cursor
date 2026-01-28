#!/usr/bin/env python3
"""
Hello World Application

A robust hello world project demonstrating Python best practices
including type hints, docstrings, argument parsing, and proper structure.
"""

import argparse
import sys
from typing import Optional


def greet(name: str = "World", greeting: str = "Hello") -> str:
    """
    Generate a greeting message.

    Args:
        name: The name to greet. Defaults to "World".
        greeting: The greeting word to use. Defaults to "Hello".

    Returns:
        A formatted greeting string.

    Examples:
        >>> greet()
        'Hello, World!'
        >>> greet("Alice")
        'Hello, Alice!'
        >>> greet("Bob", "Hi")
        'Hi, Bob!'
    """
    return f"{greeting}, {name}!"


def parse_args(args: Optional[list[str]] = None) -> argparse.Namespace:
    """
    Parse command-line arguments.

    Args:
        args: List of arguments to parse. If None, uses sys.argv.

    Returns:
        Parsed argument namespace.
    """
    parser = argparse.ArgumentParser(
        description="A friendly greeting application",
        epilog="Example: python hello.py --name Alice --greeting Hi",
    )
    parser.add_argument(
        "-n", "--name",
        type=str,
        default="World",
        help="Name to greet (default: World)",
    )
    parser.add_argument(
        "-g", "--greeting",
        type=str,
        default="Hello",
        help="Greeting word to use (default: Hello)",
    )
    parser.add_argument(
        "-c", "--count",
        type=int,
        default=1,
        help="Number of times to repeat the greeting (default: 1)",
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="%(prog)s 1.0.0",
    )
    return parser.parse_args(args)


def main() -> int:
    """
    Main entry point for the application.

    Returns:
        Exit code (0 for success, non-zero for errors).
    """
    try:
        args = parse_args()
        message = greet(name=args.name, greeting=args.greeting)
        
        for _ in range(args.count):
            print(message)
        
        return 0
    except KeyboardInterrupt:
        print("\nGoodbye!")
        return 130
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
