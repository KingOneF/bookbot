import sys
from stats import get_chars_dict, count_words, dict_to_sorted_list


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = dict_to_sorted_list(chars_dict)

    print("=========== BOOKBOT ===========")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()
print(sys.argv) 

if __name__ == "__main__":
    main()


