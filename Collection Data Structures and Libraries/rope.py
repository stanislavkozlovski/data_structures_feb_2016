from math import floor


class Rope:
    MAX_NODE_LENGTH = 4
    MIN_NODE_LENGTH = 3  # the minimum amount of charachters a node should store
    REBALANCE_RATIO = 1.2

    def __init__(self, value: str):
        self._value = value
        self._left, self._right = None, None
        self.length = len(value)
        self._reorder()

    def __str__(self):
        if self._value is not None:
            return self._value
        else:
            # recursively get the resulting string using post-order traversal
            return str(self._left) + str(self._right)

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        if isinstance(key, slice):
            if self._value is not None:
                return self._value[key.start:key.stop:key.step]
            else:
                start = key.start if key.start is not None else 0
                if start < 0:
                    start += self.length
                end = key.stop if key.stop is not None else self.length
                if end < 0:
                    end += self.length
                step = key.step if key.step is not None else 1
                to_reverse = False
                if step < 0:
                    to_reverse = True
                    step = abs(step)
                left_len = len(self._left)
                left_start = min(start, left_len)  # 5, 10, start from 5
                left_end = min(end, left_len)  # 15, 10, end at 10

                right_len = len(self._right)
                right_start = max(0, min(start - left_len, right_len))
                right_end = max(0, min(end - left_len, right_len))
                val = ''
                if left_start < left_len:
                    val += self._left[left_start:left_end:step]
                if right_end > 0:
                    val += self._right[right_start:right_end:step]
                if to_reverse:
                    val = val[::-1]
                return val

        if key >= self.length:
            raise Exception('Key is out of range!')
        if self._value is not None:
            return self._value[key]
        else:
            left_len = len(self._left)
            if key < 0:
                key += self.length
            if key < left_len:
                return self._left[key]
            else:
                return self._right[key-left_len]

    def remove(self, start: int, end: int):
        """
        Remove the substring from the start index to the end index.
        :param start: The start index to remove characters from - INCLUSIVE
        :param end: The end index of the substring we want to remove - EXCLUSIVE
        """
        if 0 > start or start > self.length:
            raise Exception('Start index is out of bounds!')
        elif 0 > end or end > self.length:
            raise Exception('End index is out of bounds!')
        elif start > end:
            raise Exception('The start index cannot be bigger than the end index.')

        if self._value is not None:
            self._value = self._value[:start] + self._value[end:]
            self.length = len(self._value)
        else:
            # find the node
            left_len = len(self._left)
            # get the indexes we should start/end from in the left subtree
            """
            Example: start:5, end: 15, left_len:10
            We should start from index 5 at the left subtree and remove everything in it (up until index 10),
            then we should start from index 0 in the right subtree up until index 5
            """
            left_start = min(start, left_len)  # 5, 10, start from 5
            left_end = min(end, left_len)  # 15, 10, end at 10

            right_len = len(self._right)
            # some arithmetic here, just study closely with sample values
            """
            Example: start:5, end:15, left_len:10, right_len:10,
            start-left_len = -5, so we get the MAX(0, MIN(-5, 10)), which is MAX(0, -5) = 0
            Obviously, since we started from the left subtree and want to continue from the right subtree,
            we need to start at index 0.
            second line - end-left_len = 5, so we get the MAX(0, MIN(5, 10)), which is MAX(0, 5) = 5
            So we have the right_start = 0 and right_end = 5
            """
            right_start = max(0, min(start - left_len, right_len))
            right_end = max(0, min(end-left_len, right_len))

            if left_start < left_len:
                self._left.remove(left_start, left_end)
            if right_end > 0:
                # we want to remove from the right subtree too
                self._right.remove(right_start, right_end)
            # update length
            self.length = len(self._left) + len(self._right)
        self._reorder()

    def insert(self, pos: int, value: str):
        if pos < 0 or pos > self.length:
            raise Exception('Position {pos} is out of bounds!'.format(pos=pos))
        if self._value is not None:
            self._value = self._value[:pos] + value + self._value[pos:]
            self.length = len(self._value)
        else:
            left_len = len(self._left)
            if pos < left_len:
                self._left.insert(pos, value)
                self.length = len(self._left) + len(self._right)  # might not want it to be here?
            else:
                self._right.insert(pos-left_len, value)
        self._reorder()

    def _reorder(self):
        """
        splits/joins long/short nodes
        """
        if self._value is not None:
            if self.length > self.MAX_NODE_LENGTH:
                # leaf node is too big, split it into two
                middle = floor(self.length / 2)

                self._left = Rope(self._value[:middle])
                self._right = Rope(self._value[middle:])
                self._value = None
        else:
            # we don't have a value, therefore we are not a leaf
            # and the _left and _right nodes have been filled
            if self.length < self.MIN_NODE_LENGTH:
                # join the child nodes into one leaf node
                self._value = str(self._left) + str(self._right)
                self._left = None
                self._right = None

    def _rebuild_subtree(self):
        """
        Rebuilds the tree from this node downwards,
            getting the string value of the subtree and
            calling reorder on it, creating children as long as we are to split.
            The result is a better balanced subtree.
        Note: Only call this function when there is a reason to! Example:
        The rebalance ration is has been tipped
                """
        if self._value is None:
            self._value = str(self._left) + str(self._right)
            self._left = None
            self._right = None
            self._reorder()

    def rebalance_subtree(self):
        """
        Check the balance ratio of each NON-LEAF node and rebuild the subtree if the balance ratio
        is tipped
        """
        if self._value is None:
            left_len = len(self._left)
            right_len = len(self._right)
            if max(left_len, right_len) / min(left_len, right_len) > self.REBALANCE_RATIO:
                # the balance has been tipped, so we need to rebuild the subtree
                self._rebuild_subtree()
            else:
                # recursively go downwards to check for rebalancing
                self._left.rebalance_subtree()
                self._right.rebalance_subtree()





vuje = Rope('The brown stanislav')
vuje.insert(5, 'lala')
print(vuje)
print(vuje[:3:-1])
