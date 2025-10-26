from stats import count_words
from stats import count_characters

def main():
    number_words = count_words("books/frankenstein.txt")
    print(f"Found {number_words} total words")

def main2():
    test = count_characters("books/frankenstein.txt")
    print(test)

main2()

