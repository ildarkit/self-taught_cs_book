def first_even_sort(values):
    even_index = 0
    for index, n in enumerate(values):
        # even
        if not n & 1:
            (values[even_index],
                values[index]) = n, values[even_index]
            even_index += 1


if __name__ == '__main__':
    values = [3, 5, 4, 0, 4, 2, 1, 6, 7, 8]
    first_even_sort(values)
    print(values)

