from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            return f.read()
    except FileNotFoundError:
        print("File nos found")
        sys.exit(1)

def get_alpha(characters):
    alpha_characters = {}
    for character, count in characters.items():
        if character.isalpha():
            alpha_characters[character] = count
    return alpha_characters

def print_report(filepath, words, characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for character in characters:
        print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

def get_filepath():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]

def main():
    filepath = get_filepath()
    text = get_book_text(filepath)
    words = count_words(text)
    all_characters = count_characters(text)
    alpha_characters = get_alpha(all_characters)
    sorted_characters = sort_characters(alpha_characters)
    print_report(filepath, words, sorted_characters)

main()