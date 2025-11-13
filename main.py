from stats import get_chars_dict, count_words

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = get_chars_dict(text)
    print(f"Found {num_words} total words")
    print(chars_dict)

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    main()


