class BinaryHeap:
    def __init__(self, elements=None):
        self._elements = []
        self.count = 0
        if elements is not None and isinstance(elements, list):
            for el in elements:
                self.insert(el)

    def __len__(self):
        return self.count

    def insert(self, value):
        """ Add the value at the end and heapify up from there """
        self._elements.append(value)
        new_value_idx = len(self._elements) - 1
        self._heapify_up(new_value_idx)
        self.count += 1

    def extract_max(self):
        """ Remove the max element by placing the last element on it's place and heapifying down"""
        max_el = self._elements[0]
        last_idx = len(self._elements) - 1

        self._elements[0] = self._elements[last_idx]
        self._elements = self._elements[:last_idx]
        self._heapify_down(0)
        self.count -= 1

        return max_el

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        if idx < 0 or parent_idx < 0:
            return
        if self._elements[parent_idx] < self._elements[idx]:
            # swap
            self._elements[parent_idx], self._elements[idx] = self._elements[idx], self._elements[parent_idx]
            self._heapify_up(parent_idx)

    def _heapify_down(self, idx):
        """
        Heapify the value down by getting it's bigger child and swapping values. Then continue heapifying down
        until we find children that are not bigger than the value.
        """
        l_child_idx, r_child_idx = (idx*2) + 1, (idx*2) + 2

        if l_child_idx < len(self._elements):
            # get the index of the bigger child
            if r_child_idx < len(self._elements) and self._elements[r_child_idx] > self._elements[l_child_idx]:
                max_idx = r_child_idx
            else:
                max_idx = l_child_idx
            # check if the child is bigger than the value, if not, stop
            if self._elements[max_idx] <= self._elements[idx]:
                return

            # swap
            self._elements[idx], self._elements[max_idx] = self._elements[max_idx], self._elements[idx]
            self._heapify_down(max_idx)
