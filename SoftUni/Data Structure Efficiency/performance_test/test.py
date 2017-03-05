from datetime import datetime
import sys
from performance_test.asizeof import asizeof
from performance_test.ordered_set import OrderedSet
from sortedcontainers import SortedSet


test_count = 10000

# test with different elements, add, remove and search
sset_start = datetime.now()

sset = SortedSet()
for i in range(test_count):
    sset.add(i)
    assert i in sset
sset_memory = asizeof(sset)
for i in range(test_count):
    sset.remove(i)
    assert i not in sset

sset_end = datetime.now()

#########################

ordered_set_start = datetime.now()

ordered_set = OrderedSet()
for i in range(test_count):
    ordered_set.add(i)
    assert ordered_set.contains(i)
ordered_set_memory = asizeof(ordered_set)
for i in range(test_count):
    ordered_set.remove(i)
    assert not ordered_set.contains(i)

ordered_set_end = datetime.now()


print("Sorted Set elapsed time: {}".format(sset_end-sset_start))
print("Sorted Set memory: {}".format(sset_memory))
print("Ordered Set elapsed time: {}".format(ordered_set_end-ordered_set_start))
print("Ordered Set memory: {}".format(ordered_set_memory))
"""
Sorted Set elapsed time: 0:00:00.380138
Ordered Set elapsed time: 0:00:06.590211
Hell, mine is quite slower.
"""