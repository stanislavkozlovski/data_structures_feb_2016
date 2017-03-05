class Tree:
    def __init__(self, value, children: list=[]):
        self.value = value
        self.children = children

    def __iter__(self):
        yield self.value
        for child in self.children:
            yield from child.__iter__()

    def print(self, indent: int=0):
        print('{space} {node}'.format(space=' ' * indent,
                                      node=self.value))
        for child in self.children:
            child.print(indent + 1)

