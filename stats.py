def count_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = len(str.split(file_contents))
    return word_count