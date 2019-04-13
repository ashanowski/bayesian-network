from exceptions import *


class Node:

    def __init__(self, name):
        self._name = name
        self._childs = None

    def __repr__(self):
        return "<Node {}>".format(self._name)

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def childs(self):
        return self._childs

    @property
    def named_childs(self):
        if self._childs is None:
            return []
        else:
            return [node.name for node in self._childs]

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
