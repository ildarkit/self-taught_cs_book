def remove_duplicate_word(text):
    words = set()
    result = []
    for w in text.split():
        clean_word = w.rstrip(',.;?!]})')
        if not clean_word in words:
            words.add(clean_word)
            result.append(w)
        elif len(clean_word) < len(w):
            result.append(w[len(clean_word):])
    return ' '.join(result)


if __name__ == '__main__':
    s = """
    I am a self-taught programmer looking for a job as a programmer.
    """
    print(remove_duplicate_word(s))
