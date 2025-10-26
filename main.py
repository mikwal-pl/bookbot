from stats import count_words
from stats import count_characters

def main():
    number_words = count_words("books/frankenstein.txt")
    print(f"Found {number_words} total words")

def main2():
    number_char = count_characters("books/frankenstein.txt")
    for i in range(0, len(number_char)-1):
        if number_char[i]["character"].isalpha():
            print(f"{number_char[i]["character"]}: {number_char[i]["number"]}")
    #print(number_char)


print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
main()
print("--------- Character Count -------")
main2()
print("============= END ===============")
