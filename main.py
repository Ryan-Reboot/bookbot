from stats import get_word_count

# create a function that takes a path to file and reads the text of the file into a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

# create a main function, which returns a word count from the book
def main():
    book = get_book_text("books/frankenstein.txt")
    words = get_word_count(book)
    print(f"{words} words found in the document")

main()
