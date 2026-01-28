"""Unit tests for the hello module."""

import unittest
from hello import greet, parse_args


class TestGreet(unittest.TestCase):
    """Test cases for the greet function."""

    def test_default_greeting(self) -> None:
        """Test default greeting returns 'Hello, World!'."""
        self.assertEqual(greet(), "Hello, World!")

    def test_custom_name(self) -> None:
        """Test greeting with a custom name."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_custom_greeting(self) -> None:
        """Test greeting with a custom greeting word."""
        self.assertEqual(greet("Bob", "Hi"), "Hi, Bob!")

    def test_empty_name(self) -> None:
        """Test greeting with an empty name."""
        self.assertEqual(greet(""), "Hello, !")

    def test_special_characters(self) -> None:
        """Test greeting handles special characters."""
        self.assertEqual(greet("O'Brien"), "Hello, O'Brien!")


class TestParseArgs(unittest.TestCase):
    """Test cases for argument parsing."""

    def test_default_args(self) -> None:
        """Test parsing with no arguments uses defaults."""
        args = parse_args([])
        self.assertEqual(args.name, "World")
        self.assertEqual(args.greeting, "Hello")
        self.assertEqual(args.count, 1)

    def test_name_argument(self) -> None:
        """Test parsing the name argument."""
        args = parse_args(["--name", "Alice"])
        self.assertEqual(args.name, "Alice")

    def test_short_name_argument(self) -> None:
        """Test parsing the short name argument."""
        args = parse_args(["-n", "Bob"])
        self.assertEqual(args.name, "Bob")

    def test_greeting_argument(self) -> None:
        """Test parsing the greeting argument."""
        args = parse_args(["--greeting", "Hi"])
        self.assertEqual(args.greeting, "Hi")

    def test_count_argument(self) -> None:
        """Test parsing the count argument."""
        args = parse_args(["--count", "3"])
        self.assertEqual(args.count, 3)

    def test_all_arguments(self) -> None:
        """Test parsing all arguments together."""
        args = parse_args(["-n", "Alice", "-g", "Hi", "-c", "5"])
        self.assertEqual(args.name, "Alice")
        self.assertEqual(args.greeting, "Hi")
        self.assertEqual(args.count, 5)


if __name__ == "__main__":
    unittest.main()
