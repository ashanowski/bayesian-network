from node import Node
from exceptions import *


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
