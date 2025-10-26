from stats import count_words

def main():
    number_words = count_words("books/frankenstein.txt")
    print(f"Found {number_words} total words")

main()

