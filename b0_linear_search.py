"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min = float('inf')
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
            ind = i
    return ind


if __name__ == "__main__":
    print(min_search([22, 4, 6, 888, 9]))
