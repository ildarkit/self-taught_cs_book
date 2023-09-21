def insertion_sort(values):
    for i in range(1, len(values)):
        value = values[i]
        while i > 0 and values[i - 1] > value:
            values[i] = values[i - 1]
            i -= 1
        values[i] = value
    return values


if __name__ == '__main__':
    l = [6, 5, 8, 2, 9, 9, 3, 1]
    print(insertion_sort(l))
