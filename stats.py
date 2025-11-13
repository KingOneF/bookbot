def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item: dict) -> int:
    return item["num"]

def dict_to_sorted_list(char_counts: dict[str, int]) -> list[dict]:
    items = [{"char": ch, "num": cnt} for ch, cnt in char_counts.items() if ch.isalpha()]
    items.sort(key=sort_on, reverse=True)
    return items

