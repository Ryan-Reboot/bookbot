""" a function that counts the words in a given text"""
def get_word_count(text):
    words_list = text.split()
    num_words = len(words_list)
    return(num_words)

""" a function that counts instances of each character, including symbols and spaces"""
def get_character_count(text):
    dictionary = {}
    lower_case = text.lower()
    for char in lower_case:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

