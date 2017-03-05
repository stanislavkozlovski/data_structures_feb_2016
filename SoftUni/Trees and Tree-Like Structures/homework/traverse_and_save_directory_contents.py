"""
Define two classes to keep files and folders:
File { string name, int size }
Folder { string name, File[] files, Folder[] childFolders }
Write a program to build a tree keeping all files and folders from the hard drive starting from C:\WINDOWS.
You may use the .NET directory listing APIs: DirectoryInfo.GetFiles() and DirectoryInfo.GetDirectories().

Implement a method that calculates the sum of the file sizes in given subtree of the tree and test it accordingly.
Use recursive tree traversal.
"""
import os


class File:
    """ Holds both files and directories, holding their name and overall size"""
    def __init__(self, name, size):
        self.name = name
        self.size = size


class TreeNode:
    def __init__(self, value, children):
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

    def add_child(self, child):
        self.children.append(child)


starting_directory = "/home/netherblood/PycharmProjects/hackbulgaria_python/week06"


def create_file_tree(start_dir):
    # recursively traverse the directories and create a Tree of them, starting at the start_dir
    main_obj = TreeNode(value=None, children=[])

    def walk_dir(directory, parent_obj):
        nonlocal main_obj
        for file in os.scandir(directory):
            abs_file_path = os.path.abspath(file.path)
            file_obj = File(name=file.name, size=os.stat(abs_file_path).st_size)
            tree_obj = TreeNode(value=file_obj, children=[])

            if file.is_dir():
                file_obj.size = 0  # don't store directory sizes like that
                walk_dir(abs_file_path, tree_obj)  # recursively go down and fill our object with it's files/dirs

            parent_obj.add_child(tree_obj)

    walk_dir(start_dir, main_obj)
    return main_obj


def calculate_filesize_sum_of_subtree(file_node):
    return sum([file.size for file in file_node])

directory_tree = create_file_tree(starting_directory)
random_subtree = directory_tree.children[3]  # 01 directory
print("File size of {} is {}".format(random_subtree.value.name, calculate_filesize_sum_of_subtree(random_subtree)))

random_subtree = directory_tree.children[2]  # __pycache__ directory
print("File size of {} is {}".format(random_subtree.value.name, calculate_filesize_sum_of_subtree(random_subtree)))