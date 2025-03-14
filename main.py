# create a function that takes a path to file and reads the text of the file into a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

# create a main function, which provides the path for the get_book_text function
def main():
    result = get_book_text("books/frankenstein.txt")
    print(result)

main()
