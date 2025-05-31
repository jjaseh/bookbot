from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    words = count_words(text)
    print(f"{words} words found in the document")
    characters = count_characters(text)
    print(characters)

main()