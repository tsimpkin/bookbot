frankenstein_path = "books/frankenstein.txt"

def read_file(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def count_words(text_input):
    words = text_input.split()
    return len(words)

def count_letters(text_input):
    letter_dictionary = {}
    for letter in text_input:
        if letter.isalpha():
            if letter.lower() in letter_dictionary.keys():
                letter_dictionary[letter.lower()] += 1
            else:
                letter_dictionary[letter.lower()] = 1
    return letter_dictionary

def print_report(file_path, word_count, letter_counts):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()
    sorted_letters = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
    for letter in sorted_letters.keys():
        print(f"The '{letter}' character was found {sorted_letters[letter]} times")
    print("--- End report ---")



def main():
    file_contents = read_file(frankenstein_path)
    word_count = count_words(file_contents)
    character_count = count_letters(file_contents)
    print_report(frankenstein_path, word_count, character_count)

main()