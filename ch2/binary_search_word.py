def binary_search(word, words):
    first = 0
    last = len(words) - 1
    while last >= first:
        mid = (first + last) // 2
        if words[mid] == word:
            return (True, mid)
        elif word < words[mid]:
            last = mid - 1
        else:
            first = mid + 1
    pos = mid if word < words[mid] else mid + 1
    return (False, pos)


if __name__ == '__main__':
    words = ['basic', 'c', 'fortran', 'python', 'rust']
    word = 'fortram'
    is_founded, pos = binary_search(word, words)
    not_str = '' if is_founded else ' не'
    res_str = f'Слово "{word}"{not_str} было найдено в позиции {pos}'
    print(res_str)
