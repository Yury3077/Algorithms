from typing import Hashable, List
import networkx as nx
from Tasks.a1_my_queue import enqueue, dequeue, peek
import matplotlib.pyplot as plt

b = nx.Graph()
b.add_node("A")
b.add_node("B")
b.add_node("C")
b.add_node("D")
b.add_node("E")
b.add_edge("A", "E")
b.add_edge("A", "C")
b.add_edge("D", "C")
b.add_edge("E", "C")
b.add_edge("D", "B")


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    list_of_vizit = []
    enqueue(start_node)
    list_of_vizit.append(start_node)
    while peek(0) != None:
        node_now = dequeue()
        neighbor_list = list(g.neighbors(node_now))
        for i in neighbor_list:
            if i in list_of_vizit:
                pass
            else:
                enqueue(i)
                list_of_vizit.append(i)

    return list_of_vizit


if __name__ == '__main__':
    print(bfs(b, "A"))
