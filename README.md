# data_structures_feb_2016
Exercises and Homework for SoftUni's Data Structures February 2016 course, in Python.

_Problems with an asterisk (*) are considered hard and optional._
# Lessons


1.[Data Structures, Algorithms and Complexity](/SoftUni/Algorithms and Complexity/)
------
Overview of the course, introduction to the Big-O notation and why algorithm speed matters.

### Exercises
* Given slow and fast functions, compare their speed.

### Homework
* Given functions, figure out their Big-O complexity.


2.[Linear Data Structures – Lists](/SoftUni/Linear Data Structures - Lists/)
-----
Linked List, how a List(Vector) works and how it differs from a traditional array.

### Exercises
* Implement a [Double-Linked List](/SoftUni/Linear Data Structures - Lists/exercises/)

### Homework
* [Get the sum and average of a list of integers](/SoftUni/Linear Data Structures - Lists/homework/sum_and_average.py)
* [Sort the words in a list](/SoftUni/Linear Data Structures - Lists/homework/sort_words.py)
* Find the [longest subsequence of equal numbers](/SoftUni/Linear Data Structures - Lists/homework/longest_subsequence.py) in an array
* [Remove odd occurrences](/SoftUni/Linear Data Structures - Lists/homework/remove_odd_occurences.py)
* [Count of occurrences](/SoftUni/Linear Data Structures - Lists/homework/count_of_occurences.py)
* __Implement a__ [__ReversedList__](/SoftUni/Linear Data Structures - Lists/homework/reversed_list_implementation.py)
* __Implement a__ [__LinkedList__](/SoftUni/Linear Data Structures - Lists/homework/linked_list.py)
* [__*Distance in Labyrinth__](/SoftUni/Linear Data Structures - Lists/homework/distance_in_labyrinth.py)


3.[Linear Data Structures – Stacks and Queues](/SoftUni/Linear Data Structures - Stacks and Queues/)
-----
Analysis of both data structures, their complexities and when to use which.

### Exercises
* Implement a [Circular Queue](/SoftUni/Linear Data Structures - Stacks and Queues/exercise/)

### Homework
* [Reverse numbers with a stack](/SoftUni/Linear Data Structures - Stacks and Queues/homework/reverse_numbers_with_stack.py)
* [Calculate sequence with a queue](/SoftUni/Linear Data Structures - Stacks and Queues/homework/calculate_sequence_with_a_queue.py)
* __Implement an__ [__Array-Based Stack__](/SoftUni/Linear Data Structures - Stacks and Queues/homework/array_based_stack.py)

    [Array-Based Stack Tests](/SoftUni/Linear Data Structures - Stacks and Queues/homework/tests_array_based_stack.py)
* __Implement a__ [__Linked Stack__](/SoftUni/Linear Data Structures - Stacks and Queues/homework/linked_stack.py)

    [Linked Stack Tests](/SoftUni/Linear Data Structures - Stacks and Queues/homework/tests_linked_stack.py)
* __Implement a__ [__Linked Queue__](/SoftUni/Linear Data Structures - Stacks and Queues/homework/linked_queue.py)

    [Linked Queue Tests](/SoftUni/Linear Data Structures - Stacks and Queues/homework/tests_linked_queue.py)
* [__*Sequence N-M__] (/SoftUni/Linear Data Structures - Stacks and Queues/homework/sequence_n_m.py)


4.[Trees and Tree-Like Structures](/SoftUni/Trees and Tree-Like Structures/)
--------------------------------------------------------------------
Introduction to Trees, Binary Trees, Balanced Binary Trees(AVL, AA, B, RB) and Graphs

### Exercises
* Implement a [tree](/SoftUni/Trees and Tree-Like Structures/exercises/tree_implementation.py). [tests](/SoftUni/Trees and Tree-Like Structures/exercises/tests_tree.py)
* Implement a [binary tree](/SoftUni/Trees and Tree-Like Structures/exercises/binary_tree_implementation.py). [tests](/SoftUni/Trees and Tree-Like Structures/exercises/tests_binary_tree.py)

### Homework
* [Play with Trees](/SoftUni/Trees and Tree-Like Structures/homework/play_with_trees.py), a program which can find
    * The root node
    *   All leaf nodes (in increasing order)
    *   All middle nodes (in increasing order)
    *   The longest path in the tree (the leftmost if several paths have the same longest length)
    *   All paths in the tree with given sum P of their nodes (from the leftmost to the rightmost)
    *   All subtrees with given sum S of their nodes (from the leftmost to the rightmost)
* [Traverse Directory](/SoftUni/Trees and Tree-Like Structures/homework/traverse_and_save_directory_contents.py) - Build a tree from directories and calculate the sum of file sizes.
* [__***Calculate Arithmetic Expression__](/SoftUni/Trees and Tree-Like Structures/homework/calculate_arithmetic_expression.py) - calculate arithmetic expressions using the Shunting Yard Algorithm

5.[Trees Traversal Algorithms](/SoftUni/Tree Traversal Algorithms - BFS and DFS/)
-------------------------------------------------------------------------
In-depth analysis of DFS and BFS

### Exercises
* [Find Connected Components](/SoftUni/Tree Traversal Algorithms - BFS and DFS/exercises/traverse_graph_find_connected_components.py) [tests](/SoftUni/Tree Traversal Algorithms - BFS and DFS/exercises/tests_traverse_graph.py)
* [Find Nearest Exit From Labyrinth](/SoftUni/Tree Traversal Algorithms - BFS and DFS/exercises/nearest_exit_labyrinth.py) [tests](/SoftUni/Tree Traversal Algorithms - BFS and DFS/exercises/tests_exit_labyrinth.py)

### Homework
* [Find the Root](/SoftUni/Tree Traversal Algorithms - BFS and DFS/homework/find_the_root.py) - Figure out if the given graph is a tree and find it's root
* [Round Dance](/SoftUni/Tree Traversal Algorithms - BFS and DFS/homework/round_dance.py) - Find the longest 'round dance'
* [Ride The Horse](/SoftUni/Tree Traversal Algorithms - BFS and DFS/homework/ride_the_horse.py) - Traverse matrix in a way a horse chesspiece would
* [Longest Path In Tree](/SoftUni/Tree Traversal Algorithms - BFS and DFS/homework/longest_path_in_tree.py) - Find the longest path in a tree from leaf to leaf by the sum of the nodes.
* [__*Sorting__](/SoftUni/Tree Traversal Algorithms - BFS and DFS/homework/sorting.py) - Each step, take K elements in the array and reverse them. Find the minimum number of such steps to completely sort the array.

6.[Dictionaries and Hash Tables](/SoftUni/Dictionaries and Hash Tables/)
----------------------------------------------------------------
Dictionary implementations, how hash-tables work (collision strategies) and set implementations.

### Exercises
* [Implement a Hash Table with Chaining](/SoftUni/Dictionaries and Hash Tables/exercises/chaining_hash_table.py) [tests](/SoftUni/Dictionaries and Hash Tables/exercises/test_chaining_hash_table.py)

### Homework (Use the Hash Table you created from the exercises)
* [Count Character Occurrences In Text](/SoftUni/Dictionaries and Hash Tables/homework/count_symbols.py)
* [Phonebook](/SoftUni/Dictionaries and Hash Tables/homework/phonebook.py)
* Implement an [Ordered Set](/SoftUni/Dictionaries and Hash Tables/homework/ordered_set.py) [tests](/SoftUni/Dictionaries and Hash Tables/homework/test_ordered_set.py)
* [**Balanced Ordered Set](/SoftUni/Dictionaries and Hash Tables/homework/balanced_ordered_set/ordered_set.py) [tests](/SoftUni/Dictionaries and Hash Tables/homework/balanced_ordered_set/ordered_set_tests.py)

7.[Collection Data Structures and Libraries](/SoftUni/Collection Data Structures and Libraries/)
----------------------------------------------------------------
Ordered dictionaries, multi-dictionaries, ordered multi-dictionaries, sets, ordered sets, bags, ordered bags, rope.
### Exercises
* [Simple String Editor Program](/SoftUni/Collection Data Structures and Libraries/exercises/efficient_string_editor.py/)
* [Events in given range](/SoftUni/Collection Data Structures and Libraries/exercises/events_in_given_range.py)

### Homework
* [Products in price range](/SoftUni/Collection Data Structures and Libraries/homework/products_in_price_range.py)
* [String Editor](/SoftUni/Collection Data Structures and Libraries/homework/string_editor.py)
* [__**Trie Data Struccture__](/SoftUni/Collection Data Structures and Libraries/homework/trie.py)
* [__****Rope Data Structure__](/SoftUni/Collection Data Structures and Libraries/rope.py)