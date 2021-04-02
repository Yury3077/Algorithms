"""
My little Stack
"""
from typing import Any

l = []


def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    global l
    l.append(elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    global l
    if len(l) == 0:
        return None
    else:
        last = l[len(l) - 1]
        l.pop(len(l) - 1)
    return last


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    global l
    if ind >= len(l):
        return None
    else:
        return l[(len(l) - 1) - ind]


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    global l
    l = []
    return None


if __name__ == "__main__":
    push(4)
    push(7)
    print(push(5))
    clear()
    print(l)
