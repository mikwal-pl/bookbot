def count_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = len(str.split(file_contents))
    return word_count

def count_characters(filepath):
    with open(filepath) as f:
        char_dict = {}
        file_cont = str.lower(f.read())
        for char in file_cont:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        return char_dict

