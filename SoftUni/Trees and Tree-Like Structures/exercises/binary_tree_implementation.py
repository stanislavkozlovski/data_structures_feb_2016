class BinaryTree:
    def __init__(self, value, left: 'BinaryTree'=None, right: 'BinaryTree'=None, iterable_strategy: str="inorder"):
        """
        :param iterable_strategy: A string denoting the desired iterator strategy
            - Supported strategies are: preorder, inorder, postorder
        """
        self.value = value
        self.left = left
        self.right = right
        self.iterable_strategy = iterable_strategy
        self.__validate_strategy()

    def __iter__(self):
        if self.iterable_strategy == "preorder":
            yield self.value
            yield from self.left.__iter__()
            yield from self.right.__iter__()
        elif self.iterable_strategy == "inorder":
            yield from self.left.__iter__()
            yield self.value
            yield from self.right.__iter__()
        elif self.iterable_strategy == "postorder":
            yield from self.left.__iter__()
            yield from self.right.__iter__()
            yield self.value

    def print_indented_pre_order(self, indent: int=0):
        print("{indent}{node}".format(indent=" " * indent,
                                       node=self.value))
        if self.left:
            self.left.print_indented_pre_order(indent + 1)
        if self.right:
            self.right.print_indented_pre_order(indent + 1)

    def __validate_strategy(self):
        """
        This function validates that the iterable_strategies of each child (left and right)
        are the same as the parents
        """
        if ((self.left and self.left.iterable_strategy != self.iterable_strategy)
                or (self.right and self.right.iterable_strategy != self.iterable_strategy)):
            raise Exception("Children must have the same iterable strategy")
