def count_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = len(str.split(file_contents))
    return word_count

def count_characters(filepath):
    with open(filepath) as f:
        char_list = []
        char_dict = {}
        char_set = set()
        file_cont = str.lower(f.read())
        for char in file_cont:
            if char not in char_set:
                char_set.add(char)
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        keys = char_dict.keys()
        for k in keys:
            char_list.append({"character": k, "number": char_dict[k]})
        return char_list
