def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n <= 0:
        raise ValueError("Несоответствующее значение")
    else:
        if n <= 1:
            return 1
        return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n <= 0:
        raise ValueError("Несоответствующее значение")
    else:
        zn = 1
        for i in range(1, n + 1):
            zn = zn * i
        return zn


if __name__ == '__main__':
    print(factorial_recursive(3))
    print(factorial_iterative(3))
