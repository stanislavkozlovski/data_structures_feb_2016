class BinaryHeap:
    def __init__(self, elements=None):
        self._elements = []
        self.count = 0
        if elements is not None:
            pass

    def __len__(self):
        return self.count

    def insert(self, value):
        self._elements.append(value)
        new_value_idx = len(self._elements) - 1
        self._heapify_up(new_value_idx)

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        if idx < 0 or parent_idx < 0:
            return
        if self._elements[parent_idx] < self._elements[idx]:
            # swap
            self._elements[parent_idx], self._elements[idx] = self._elements[idx], self._elements[parent_idx]
            self._heapify_up(parent_idx)

    def extract_max(self):
        pass
