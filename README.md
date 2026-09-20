# Pythonic Text Analyzer

This project refactors an unpythonic text analyzer into a cleaner, more readable, and more maintainable Python program.

## Features

- Reads text from a file
- Converts text to lowercase and splits it into words
- Counts total and unique words
- Displays the five most frequent words
- Counts words longer than three characters

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run:

```bash
python text_analyzer.py
```

## Key Improvements

- Applied PEP 8 naming and formatting conventions
- Used a `with` statement for safer file handling
- Used a list comprehension to find words longer than three characters
- Used `collections.Counter` to count word frequencies
- Broke the original larger function into smaller, focused functions
- Used f-strings to make output statements cleaner and easier to read

## Screencast

<https://www.loom.com/share/14c5482ab840410384fafa446e369ce9>