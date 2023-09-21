def merge_sort(values):
    if len(values) > 1:
        mid = len(values) // 2
        left_part = values[:mid]
        right_part = values[mid:]

        merge_sort(left_part)
        merge_sort(right_part)

        left_ind = right_ind = ind = 0

        while left_ind < len(left_part) and right_ind < len(right_part):
            if left_part[left_ind] <= right_part[right_ind]:
                values[ind] = left_part[left_ind]
                left_ind += 1
            else:
                values[ind] = right_part[right_ind]
                right_ind += 1
            ind += 1
        
        while left_ind < len(left_part):
            values[ind] = left_part[left_ind]
            left_ind += 1
            ind += 1

        while right_ind < len(right_part):
            values[ind] = right_part[right_ind]
            right_ind += 1
            ind += 1


if __name__ == '__main__':
    l = [4, 2, 7, 6, 6, 5, 3, 4]
    merge_sort(l)
    print(l)
