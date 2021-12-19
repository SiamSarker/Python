import math as m
from queue import PriorityQueue

nodes = 5
edge = 6
goalnode = 5

adj_list = [[],
            [[2, 3], [3, 3]],
            [[1, 3], [3, 2], [4, 2]],
            [[1, 3], [2, 2], [5, 2]],
            [[2, 2], [5, 1]],
            [[3, 2], [4, 1]]]

for node in range(1, nodes + 1):
    print(node, adj_list[node])

h = [0, 5, 4, 3, 1, 0]


class minQ:
    def __init__(self, nodenum):
        self.node_number = nodenum
        self.parent = None
        self.actual_cost = m.inf
        self.totalcost = m.inf

    def setparent(self, parentval):
        self.parent = parentval

    def update_cost(self, costval):
        self.actual_cost = costval

    def total_cost(self, costval, nodenum):
        self.totalcost = costval + h[nodenum]


from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


def AstarNode(src_node):
    src_node_obj = minQ(src_node)
    src_node_obj.update_cost(0)
    src_node_obj.total_cost(0, src_node)

    E = []

    pq = PriorityQueue()
    pq.put(PrioritizedItem(0 + h[src_node], src_node_obj))

    while not pq.empty():
        item = pq.get()
        new_obj = item.item
        new_node_number = new_obj.node_number

        if new_node_number == goalnode:
            path = []
            goal_node_obj = new_obj
            while goal_node_obj is not None:
                path.append(goal_node_obj.node_number)
                goal_node_obj = goal_node_obj.parent

            path.reverse()
            print("The Solution Path: ", end="")
            for p in path:
                print(p, end="   ")
            print()
            print("Actual cost: ", new_obj.actual_cost)
            break

        if new_node_number in E:
            continue
        else:
            E.append(new_node_number)

            new_adj_list = adj_list[new_node_number]
            for adj in new_adj_list:
                adj_node_number = adj[0]
                edge_weight = adj[1]

                adj_obj = minQ(adj_node_number)
                adj_obj.setparent(new_obj)
                adj_obj.update_cost(new_obj.actual_cost + edge_weight)
                adj_obj.total_cost(new_obj.actual_cost, new_node_number)

                pq.put(PrioritizedItem(adj_obj.totalcost, adj_obj))


AstarNode(1)
