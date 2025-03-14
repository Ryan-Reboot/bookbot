# a function that counts the words in a given text
def get_word_count(text):
    words_list = text.split()
    num_words = len(words_list)
    return(num_words)

# a function that counts instances of each character, including symbols and spaces
def get_character_count(text):
    dictionary = {}
    lower_case = text.lower()
    for char in lower_case:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

# A function that takes a dictionary and returns the value of "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

# a function that takes a dictionary of characters and frequency, and returns a sorted
# list of dictionaries
def get_sorted_list(input_dict):
    # Convert dictionary to a list of dictionaries with "letter" and "num" structure
    list_of_dicts = [{"letter": key, "num": value} for key, value in input_dict.items()]
    # Sort that list
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts


