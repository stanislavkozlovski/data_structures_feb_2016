# data_structures_feb_2016
Exercises and Homework for SoftUni's Data Structures February 2016 course, in Python.

_Problems with an asterisk (*) are considered hard and optional._
# Lessons


1.[Data Structures, Algorithms and Complexity](/Algorithms and Complexity/)
------
Overview of the course, introduction to the Big-O notation and why algorithm speed matters.

### Exercises
* Given slow and fast functions, compare their speed.

### Homework
* Given functions, figure out their Big-O complexity.


2.[Linear Data Structures – Lists](/Linear Data Structures - Lists/)
-----
Linked List, how a List(Vector) works and how it differs from a traditional array.

### Exercises
* Implement a [Double-Linked List](/Linear Data Structures - Lists/exercises/)

### Homework
* [Get the sum and average of a list of integers](/Linear Data Structures - Lists/homework/sum_and_average.py)
* [Sort the words in a list](/Linear Data Structures - Lists/homework/sort_words.py)
* Find the [longest subsequence of equal numbers](/Linear Data Structures - Lists/homework/longest_subsequence.py) in an array
* [Remove odd occurrences](/Linear Data Structures - Lists/homework/remove_odd_occurences.py)
* [Count of occurrences](/Linear Data Structures - Lists/homework/count_of_occurences.py)
* __Implement a__ [__ReversedList__](/Linear Data Structures - Lists/homework/reversed_list_implementation.py)
* __Implement a__ [__LinkedList__](/Linear Data Structures - Lists/homework/linked_list.py)
* [__*Distance in Labyrinth__](/Linear Data Structures - Lists/homework/distance_in_labyrinth.py)


3.[Linear Data Structures – Stacks and Queues](/Linear Data Structures - Stacks and Queues/)
-----
Analysis of both data structures, their complexities and when to use which.

### Exercises
* Implement a [Circular Queue](/Linear Data Structures - Stacks and Queues/exercise/)

### Homework
* [Reverse numbers with a stack](/Linear Data Structures - Stacks and Queues/homework/reverse_numbers_with_stack.py)
* [Calculate sequence with a queue](/Linear Data Structures - Stacks and Queues/homework/calculate_sequence_with_a_queue.py)
* __Implement an__ [__Array-Based Stack__](/Linear Data Structures - Stacks and Queues/homework/array_based_stack.py)

    [Array-Based Stack Tests](/Linear Data Structures - Stacks and Queues/homework/tests_array_based_stack.py)
* __Implement a__ [__Linked Stack__](/Linear Data Structures - Stacks and Queues/homework/linked_stack.py)

    [Linked Stack Tests](/Linear Data Structures - Stacks and Queues/homework/tests_linked_stack.py)
* __Implement a__ [__Linked Queue__](/Linear Data Structures - Stacks and Queues/homework/linked_queue.py)

    [Linked Queue Tests](/Linear Data Structures - Stacks and Queues/homework/tests_linked_queue.py)
* [__*Sequence N-M__] (/Linear Data Structures - Stacks and Queues/homework/sequence_n_m.py)


4.[Trees and Tree-Like Structures](/Trees and Tree-Like Structures/)
--------------------------------------------------------------------
Introduction to Trees, Binary Trees, Balanced Binary Trees(AVL, AA, B, RB) and Graphs

### Exercises
* Implement a [tree](/Trees and Tree-Like Structures/exercises/tree_implementation.py). [tests](/Trees and Tree-Like Structures/exercises/tests_tree.py)
* Implement a [binary tree](/Trees and Tree-Like Structures/exercises/binary_tree_implementation.py). [tests](/Trees and Tree-Like Structures/exercises/tests_binary_tree.py)

### Homework
* [Play with Trees](/Trees and Tree-Like Structures/homework/play_with_trees.py), a program which can find
    * The root node
    *   All leaf nodes (in increasing order)
    *   All middle nodes (in increasing order)
    *   The longest path in the tree (the leftmost if several paths have the same longest length)
    *   All paths in the tree with given sum P of their nodes (from the leftmost to the rightmost)
    *   All subtrees with given sum S of their nodes (from the leftmost to the rightmost)
* [Traverse Directory](/Trees and Tree-Like Structures/homework/traverse_and_save_directory_contents.py) - Build a tree from directories and calculate the sum of file sizes.
* [__***Calculate Arithmetic Expression__](/Trees and Tree-Like Structures/homework/calculate_arithmetic_expression.py) - calculate arithmetic expressions using the Shunting Yard Algorithm

5.[Trees Traversal Algorithms](/Tree Traversal Algorithms - BFS and DFS/)
-------------------------------------------------------------------------
In-depth analysis of DFS and BFS

### Exercises
* [Find Connected Components](/Tree Traversal Algorithms - BFS and DFS/exercises/traverse_graph_find_connected_components.py) [tests](/Tree Traversal Algorithms - BFS and DFS/exercises/test_traverse_graph.py)
* [Find Nearest Exit From Labyrinth](/Tree Traversal Algorithms - BFS and DFS/exercises/nearest_exit_labyrinth.py) [tests](/Tree Traversal Algorithms - BFS and DFS/exercises/tests_exit_labyrinth.py)

### Homework
* [Find the Root](/Tree Traversal Algorithms - BFS and DFS/homework/find_the_root.py) - Figure out if the given graph is a tree and find it's root
* [Round Dance](/Tree Traversal Algorithms - BFS and DFS/homework/round_dance.py) - Find the longest 'round dance'
* [Ride The Horse](/Tree Traversal Algorithms - BFS and DFS/homework/ride_the_horse.py) - Traverse matrix in a way a horse chesspiece would
* [Longest Path In Tree](/Tree Traversal Algorithms - BFS and DFS/homework/longest_path_in_tree.py) - Find the longest path in a tree from leaf to leaf by the sum of the nodes.
* [__*Sorting__](/Tree Traversal Algorithms - BFS and DFS/homework/sorting.py) - Each step, take K elements in the array and reverse them. Find the minimum number of such steps to completely sort the array.
