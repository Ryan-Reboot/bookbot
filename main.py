import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import get_word_count
from stats import get_character_count
from stats import get_sorted_list

# create a function that takes a path to file and reads the text of the file into a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

# create a main function, which returns a word count from the book
def main():
    book = get_book_text(sys.argv[1])
    words = get_word_count(book)
    char_count = get_character_count(book)
    sorted_list = get_sorted_list(char_count)
    print(f"============ BOOKBOT ============\n"
    f"Analyzing book found at {sys.argv[1]}...\n"
    f"----------- Word Count ----------\n"
    f"Found {words} total words\n"
    f"--------- Character Count -------")
    for d in sorted_list:
        if d["letter"].isalpha():
            print(f"{d["letter"]}: {d["num"]}")

main()
