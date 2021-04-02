def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n <= 0:
        raise ValueError("Несоответствующее значение")
    else:
        if n - 1 <= 1:
            return 1
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n <= 0:
        raise ValueError("Несоответствующее значение")
    else:
        num1 = 1
        num2 = 1
        for i in range(n - 2):
            num3 = num1 + num2
            num1 = num2
            num2 = num3

        return num2


if __name__ == '__main__':
    print(fib_recursive(8))
    print(fib_iterative(8))
