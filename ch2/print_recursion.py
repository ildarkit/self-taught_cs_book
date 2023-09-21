def print_recursion(n):
    if n > 1:
        print_recursion(n - 1)
    print(n)

if __name__ == '__main__':
    print_recursion(10)
