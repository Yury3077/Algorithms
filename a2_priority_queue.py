"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

l3 = []
l4 = []


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global l3
    while len(l3) < priority + 1:
        l3.append([])
    l3[priority].append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    global l3
    if len(l3) == 0:
        return None
    else:
        for i in range(len(l3)):
            if len(l3[i]) > 0:
                start = l3[i].pop(0)
                break
        return start


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global l3, l4
    for i in range(len(l3)):
        for k in range(len(l3[i])):
            if l3[i][k] != None:
                l4.append(l3[i][k])
    if ind > len(l4) - 1:
        return None
    else:
        return l4[ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global l3
    l3 = []
    return None


if __name__ == "__main__":
    enqueue(1, 2)
    enqueue(44, 2)
    enqueue(84, 10)
    enqueue(5, 0)
    print(l3)
    print(peek(4))
