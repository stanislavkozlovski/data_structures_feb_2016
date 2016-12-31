from sortedcontainers import SortedDict, SortedSet
from collections import OrderedDict
from sortedcontainers import SortedListWithKey


class ElementWrapper:
    def __init__(self, value):
        self.value = value
        self.count = 1

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return '{} {}'.format(self.value, self.count)


class ElementOrderWrapper:
    def __init__(self, value, occurence):
        self.value = value
        self.occurence = occurence

    def __hash__(self):
        return hash(str(self.value) + str(self.occurence))

    def __eq__(self, other):
        return (str(self.value) + str(self.occurence)) == (str(other.value) + str(other.occurence))

    # def __gt__(self, other):
    #     return self.overall_occurence > other.overall_occurence
    #
    # def __lt__(self, other):
    #     return self.overall_occurence < other.overall_occurence
    #
    def __repr__(self):
        return '{} {}'.format(self.value, self.occurence)


class FirstLastList:
    def __init__(self):
        self.sorted_elements = SortedSet()
        self.ordered_elements = OrderedDict()

    def count(self):
        return len(self.ordered_elements)

    def clear(self):
        self.sorted_elements = SortedSet()
        self.ordered_elements = OrderedDict()

    def add(self, element):
        # add in the sorted container
        sorted_element = ElementWrapper(element)
        if sorted_element in self.sorted_elements:
            # increment his count
            sorted_element_idx = self.sorted_elements.index(sorted_element)
            self.sorted_elements[sorted_element_idx].count += 1
        else:
            self.sorted_elements.add(sorted_element)

        element_occurence = self.sorted_elements[self.sorted_elements.index(sorted_element)].count
        # add in the ordered container
        ordered_element = ElementOrderWrapper(element, element_occurence)
        self.ordered_elements[ordered_element] = True

    def min(self, count):
        count_left = count
        min_items = []
        to_break = False
        for i in range(len(self.sorted_elements)):
            min_obj = self.sorted_elements[i]
            for _ in range(min_obj.count):
                count_left -= 1
                min_items.append(min_obj.value)
                if count_left == 0:
                    to_break = True
                    break
            if to_break:
                break

        return min_items

    def max(self, count):
        count_left = count
        max_items = []
        to_break = False
        for i in range(1, len(self.sorted_elements)+1):
            max_obj = self.sorted_elements[-i]
            for _ in range(max_obj.count):
                count_left -= 1
                max_items.append(max_obj.value)
                if count_left == 0:
                    to_break = True
                    break
            if to_break:
                break

        return max_items

    def first(self, count):
        return list(self.ordered_elements.keys())[:count]

    def last(self, count):
        start = len(self.ordered_elements) - count
        if start < 0:
            start = 0
        keys = list(self.ordered_elements.keys())
        return [keys[i] for i in reversed(range(start, len(keys)))]

    def remove_all(self, element):
        el_obj = ElementWrapper(element)
        if el_obj not in self.sorted_elements:
            return 0
        # remove from the sorted collection
        el_idx = self.sorted_elements.index(el_obj)
        element_obj = self.sorted_elements[el_idx]
        self.sorted_elements.remove(element_obj)

        # remove from the order collection
        for occurence in range(1, element_obj.count + 1):
            el_wrapper = ElementOrderWrapper(element, occurence)
            del self.ordered_elements[el_wrapper]

        return element_obj.count


ls = FirstLastList()
ls.add(5)
ls.add(1)
ls.add(2.5)
ls.add(2)
ls.add(2)
ls.add(2)
ls.add(2)
ls.add(2)


print(ls.min(5))
print(ls.max(4))

print(ls.first(2))
print(ls.last(2))

print('BEFORE REMOVE' + '-'*100)
print(ls.remove_all(2))


print(ls.min(5))
print(ls.max(2))

print(ls.first(2))
print(ls.last(2))