from collections import deque
initial_capacity = 16


class KeyValue:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def __hash__(self):
        return self.__combine_hash_codes(hash(self.key), hash(self.value))

    def __str__(self):
        return 'KeyValue - Key: {key} | Value: {val}'.format(
            key=self.key, val=self.value
        )

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value

    def __combine_hash_codes(self, h1: int, h2: int):
        return ((h1 << 5) + h1) ^ h2

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class HashTable():
    def __init__(self, capacity=initial_capacity):
        self.slots = deque([None] * capacity)
        self.count = 0

    def __iter__(self):
        for slot in self.slots:
            if slot is not None:
                for key_val in slot:
                    yield key_val

    def add(self, key, value):
        key_val = KeyValue(key, value)
        self.grow_if_needed()
        index = self.get_key_index(key)

        if self.slots[index] is None:
            self.slots[index] = deque([key_val])
        else:
            for taken_slot in self.slots[index]:
                if taken_slot.key == key_val.key:
                    raise Exception('The key {} is taken!'.format(key_val.key))

            self.slots[index].append(key_val)
            self.count += 1

    def find(self, key):
        """ Try to find a value with the given key. If no such exists, return false"""
        index = self.get_key_index(key)
        if not self.slots[index]:
            return None
        for slot in self.slots[index]:
            print(slot)
            if slot.key == key:
                return slot
        return None

    def grow_if_needed(self):
        capacity = len(self.slots)
        if self.count / capacity < 0.65:
            return  # not over the fill factor

        # double the capacity
        new_hash_table = self.__rehash_elements(HashTable(self.capacity * 2))
        self.slots = new_hash_table.slots
        self.count = new_hash_table.count

    def __rehash_elements(self, new_hash_table):
        for element in self:
            new_hash_table.add(element.key, element.value)

        return new_hash_table

    def get_key_index(self, key):
        index = abs(hash(key) % len(self.slots))
        return index

    @property
    def capacity(self):
        return len(self.slots)
