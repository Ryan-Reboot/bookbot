# create a function that takes a path to file and reads the text of the file into a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count():
    book = get_book_text("books/frankenstein.txt")
    words_list = book.split()
    num_words = len(words_list)
    return(num_words)

# create a main function, which returns a word count from the book
def main():
    print(f"{get_word_count()} words found in the document")

main()
