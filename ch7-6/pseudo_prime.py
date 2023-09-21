def is_pseudo_prime(n):
    return (2 << n - 2) % n == 1


if __name__ == '__main__':
    n = 17
    if is_pseudo_prime(n):
        print(f"Число {n} вероятно простое")
    else:
        print(f"Число {n} составное")
