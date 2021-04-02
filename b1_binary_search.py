from typing import Sequence, Optional

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    left = 0
    right = len(arr)

    while right - left > 1:
        mid = (left + right) // 2
        if elem > arr[mid]:
            left = mid
        else:
            right = mid
    if elem == arr[left]:
        return left
    elif elem == arr[right]:
        return right
    else:
        return None


if __name__ == '__main__':
    print(binary_search(3, [1, 2, 3, 3, 3, 6, 7, 8, 9]))
