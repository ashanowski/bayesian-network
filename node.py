from exceptions import *


class Node:

    def __init__(self, name):
        self._name = name
        self._childs = None
        self._probability_table = None

    def __repr__(self):
        return "<Node {}>".format(self._name)

    def __str__(self):
        return self._name

    def prob_len(self):
        if self._probability_table is None:
            return 0
        return len(self._probability_table)

    @property
    def name(self):
        return self._name

    @property
    def childs(self):
        if self._childs is None:
            return []
        else:
            return self._childs

    @property
    def named_childs(self):
        if self._childs is None:
            return []
        else:
            return [node.name for node in self._childs]

    @property
    def probability_table(self):
        if self._probability_table is None:
            return []
        else:
            return self._probability_table

    def add_child(self, child):
        if self._childs is None:
            # if isinstance(childs, str):
            #     self._childs =\
            #         [Node(child_name) for child_name in childs.split(',')]
            # if isinstance(childs, list):
            #     self._childs =\
            #         [Node(child_name) for child_name in childs]
            if isinstance(child, Node):
                self._childs = [child]
            else:
                raise NodeNotInGraphException

        elif isinstance(self._childs, list):
            self._childs.append(child)

    def add_probability(self, prob):
        if self._probability_table is None:
            if isinstance(prob, float):
                self._probability_table = [ [prob, 1 - prob] ]
        
        elif isinstance(self._probability_table, list):
            if isinstance(prob, float):
                self._probability_table.append([prob, 1 - prob])

