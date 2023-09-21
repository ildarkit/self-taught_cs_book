def check_min_heap(binary_tree):
    i = 0
    while 2*i + 2 < len(binary_tree):
        key = binary_tree[i]
        if not (key <= binary_tree[2*i + 1] and
            key <= binary_tree[2*i + 2]):
            return False
        i += 1
    return True


if __name__ == '__main__':
    binary_tree = ['c', 'e', 'd', 'h', 'r', 't', 'l']
    assert check_min_heap(binary_tree)
    binary_tree = ['c', 'e', 'l', 'h', 'r', 't', 'd']
    assert not check_min_heap(binary_tree)
