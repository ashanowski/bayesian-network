from node import Node
from exceptions import *
from collections import Counter


class Graph:

    def __init__(self):
        self._nodes = []

    def __len__(self):
        return len(self._nodes)

    def __repr__(self):
        return str(self._nodes)

    def __str__(self):
        return "<Graph object with {} nodes>".format(len(self)) \
            if len(self) != 1 \
            else "<Graph object with 1 node>"

    @property
    def nodes(self):
        # return [node.name for node in self._nodes]
        return self._nodes

    @property
    def named_nodes(self):
        return [node.name for node in self._nodes]


    def add_node(self, node_name):
        if node_name not in self.named_nodes:
            self._nodes.append(Node(node_name))
        else:
            error = "Node '{}' already exists in this graph".format(node_name)
            raise NodeExistsException(error)

    def probability_count(self):
        """ Return dictionary with nodes as keys and number
            of probability table rows
        """

        # create all childs list in current graph (contains redunds)
        child_list = list()
        for node in self._nodes:
            for child in node.childs:
                child_list.append(child)

        probability_count = Counter()

        # count occurences of given node as a child
        for node in self._nodes:
            for child in child_list:
                if node == child:
                    probability_count[child] += 1

        # add missing nodes' parents value as zeros
        for node in self._nodes:
            if node not in probability_count.keys():
                probability_count[node] = 0
            
        # define how big should probability table be
        for node, parents in probability_count.items():
            probability_count[node] = 2 ** parents


        return probability_count