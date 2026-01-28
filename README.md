# Hello World

A robust hello world project demonstrating Python best practices.

## Features

- Command-line interface with argument parsing
- Type hints for better code clarity
- Comprehensive docstrings with examples
- Unit tests with good coverage
- Proper project structure

## Installation

No external dependencies required. Uses Python 3.10+.

```bash
git clone <repository-url>
cd test_cursor
```

## Usage

### Basic Usage

```bash
python hello.py
# Output: Hello, World!
```

### Custom Name

```bash
python hello.py --name Alice
# Output: Hello, Alice!
```

### Custom Greeting

```bash
python hello.py --name Bob --greeting Hi
# Output: Hi, Bob!
```

### Repeat Greeting

```bash
python hello.py --count 3
# Output:
# Hello, World!
# Hello, World!
# Hello, World!
```

### All Options

```bash
python hello.py -n Alice -g "Good morning" -c 2
# Output:
# Good morning, Alice!
# Good morning, Alice!
```

### Help

```bash
python hello.py --help
```

## Running Tests

```bash
python -m unittest test_hello.py -v
```

## Project Structure

```
test_cursor/
├── hello.py          # Main application
├── test_hello.py     # Unit tests
├── README.md         # This file
└── requirements.txt  # Dependencies (none required)
```

## License

MIT License
