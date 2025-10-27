from stats import count_words, count_characters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    number_words = count_words(sys.argv[1])
    print(f"Found {number_words} total words")

def main2():
    number_char = count_characters(sys.argv[1])
    for i in range(0, len(number_char)-1):
        if number_char[i]["character"].isalpha():
            print(f"{number_char[i]["character"]}: {number_char[i]["number"]}")
    #print(number_char)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
main()
print("--------- Character Count -------")
main2()
print("============= END ===============")
