# BookBot AI Coding Instructions

## Project Overview
BookBot is a text analysis tool that processes books from the `books/` directory. This is a Boot.dev learning project focused on building Python fundamentals through practical text processing.

## Architecture & Code Organization
- **Single-file application**: All code lives in `main.py` - no module separation needed
- **Data location**: Text files are stored in `books/` directory (gitignored)
- **Entry point**: `main()` function orchestrated by `if __name__ == "__main__"` guard

## Code Patterns & Conventions

### Text File Handling
Always use UTF-8 encoding when opening files:
```python
with open(path, encoding="utf-8") as f:
    return f.read()
```

### Function Style
- Use type hints for clarity (e.g., `def count_words(text: str) -> int:`)
- Keep functions pure and single-purpose
- Add inline comments to explain non-obvious implementation choices
- Example from codebase: `count_words()` includes comment explaining why `.split()` works for word counting

### Reporting Pattern
Print analysis results in a readable format:
```python
print(f"Found {num_words} total words")
```

## Development Workflow

### Running the Program
```bash
python main.py
```

### Adding New Analysis Features
1. Create a new function following the pattern: `def analyze_<feature>(text: str) -> <return_type>:`
2. Call it from `main()` after getting the book text
3. Print results in a user-friendly format

### Working with Books
- Default book is `books/frankenstein.txt`
- To analyze different books, modify the `book_path` variable in `main()`
- Books directory is gitignored - add sample texts locally as needed

## Key Files
- `main.py` - All application logic
- `books/frankenstein.txt` - Default sample text for analysis
- `README.md` - Project context and Boot.dev reference
