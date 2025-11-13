def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"Found {num_words} total words")


def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def count_words(text: str) -> int:
   # Splits on any whitespace (spaces, newlines, tabs), which is perfect for word counting
    return len(text.split())

if __name__ == "__main__":
    main()




