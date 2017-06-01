//package com.company;

import java.io.InvalidObjectException;
import java.util.Deque;
import java.util.LinkedList;
import java.util.function.Consumer;

public class BinarySearchTree<T extends Comparable<T>> {
    private Node root;
    private int nodesCount;

    public BinarySearchTree() {
    }

    private BinarySearchTree(Node root) {
        this.preOrderCopy(root);
    }

    private void preOrderCopy(Node node) {
        if (node == null) {
            return;
        }

        this.insert(node.value);
        this.preOrderCopy(node.left);
        this.preOrderCopy(node.right);
    }

    public Node getRoot() {
        return this.root;
    }

    public int getNodesCount() {
        return this.nodesCount;
    }

    public void insert(T value) {
        this.nodesCount++;

        if (this.root == null) {
            this.root = new Node(value, null);
            return;
        }

        Node parent = null;
        Node current = this.root;
        while (current != null) {
            parent = current;
            parent.childrenCount++;

            if (value.compareTo(current.value) < 0) {
                current = current.left;
            } else if (value.compareTo(current.value) > 0) {
                current = current.right;
            } else {
                return;
            }
        }

        Node newNode = new Node(value, parent);
        if (value.compareTo(parent.value) < 0) {
            parent.left = newNode;
        } else {
            parent.right = newNode;
        }
    }

    public boolean contains(T value) {
        Node current = this.root;
        while (current != null) {
            if (value.compareTo(current.value) < 0) {
                current = current.left;
            } else if (value.compareTo(current.value) > 0) {
                current = current.right;
            } else {
                break;
            }
        }

        return current != null;
    }

    public BinarySearchTree<T> search(T item) {
        Node current = this.root;
        while (current != null) {
            if (item.compareTo(current.value) < 0) {
                current = current.left;
            } else if (item.compareTo(current.value) > 0) {
                current = current.right;
            } else {
                break;
            }
        }

        return new BinarySearchTree<>(current);
    }

    public void eachInOrder(Consumer<T> consumer) {
        this.eachInOrder(this.root, consumer);
    }

    private void eachInOrder(Node node, Consumer<T> consumer) {
        if (node == null) {
            return;
        }

        this.eachInOrder(node.left, consumer);
        consumer.accept(node.value);
        this.eachInOrder(node.right, consumer);
    }

    public Iterable<T> range(T from, T to) {
        Deque<T> queue = new LinkedList<>();
        this.range(this.root, queue, from, to);
        return queue;
    }

    private void range(Node node, Deque<T> queue, T startRange, T endRange) {
        if (node == null) {
            return;
        }

        int compareStart = startRange.compareTo(node.value);
        int compareEnd = endRange.compareTo(node.value);
        if (compareStart < 0) {
            this.range(node.left, queue, startRange, endRange);
        }
        if (compareStart <= 0 && compareEnd >= 0) {
            queue.addLast(node.value);
        }
        if (compareEnd > 0) {
            this.range(node.right, queue, startRange, endRange);
        }
    }

    private T minValue(Node root) {
        T minv = root.value;
        while (root.left != null) {
            minv = root.left.value;
            root = root.left;
        }

        return minv;
    }

    public void deleteMin() {
        if (this.root == null) {
            throw new IllegalArgumentException("Tree is empty!");
        }

        Node min = this.root;
        Node parent = null;

        while (min.left != null) {
            parent = min;
            parent.childrenCount--;
            min = min.left;
        }

        if (parent == null) {
            this.root = this.root.right;
        } else {
            parent.left = min.right;
        }

        this.nodesCount--;
    }

    public void deleteMax() {
        if (this.root == null) {
            throw new IllegalArgumentException("Tree is empty!");
        }

        Node rightestNode = root;
        while (rightestNode.getRight() != null) {
            rightestNode = rightestNode.getRight();
        }
        Node parent = rightestNode.parent;
        parent.setRight(rightestNode.left);
        if (rightestNode.getLeft() != null) {
            rightestNode.left.parent = parent;
        }

        this.nodesCount--;
    }

    public T ceil(T element) {
        Node currNode = this.root;
        T lastValue = null;
        while (true) {
            if (currNode == null) {
                return lastValue;
            }

            if (currNode.value == element) {
                return currNode.value;
            } else if (currNode.isBiggerThan(element)) {
                // save this one and go left, trying to find a smaller one that's still a ceil
                lastValue = currNode.getValue();
                currNode = currNode.getLeft();
            } else {
                // current element is smaller, strictly go right
                currNode = currNode.getRight();
            }
        }
    }

    public T floor(T element) {
        Node currNode = this.root;
        T lastVal = null;
        while (true) {
            if (currNode == null) {
                return lastVal;
            }
            if (currNode.value == element) {
                return currNode.value;
            }
            else if (currNode.isBiggerThan(element)) {
                // we're at a bigger element, so we strictly want to go left
                currNode = currNode.getLeft();
            }
            else {
                // we're at a smaller element, we either want to return this element or go right
                // trying to find a bigger one that's still a floor
                if (currNode.getRight() == null) {
                    return currNode.value;
                }
                lastVal = currNode.value;
                currNode = currNode.getRight();
            }
        }

    }

    public void delete(T key) {
        // find the node
        Node wantedNode = this.find(this.root, key);
        if (wantedNode == null) {
            // TODO: throw smth
            return;
        }
        if (wantedNode.getLeft() == null && wantedNode.getRight() == null) {
            Node parent = wantedNode.parent;
            if (parent.getLeft() == wantedNode) {
                parent.setLeft(null);
            } else {
                parent.setRight(null);
            }
        } else {
            // some kind of middle node
            if (wantedNode.hasSuccessor()) {
                // swap with successor, easy
                wantedNode.setValue(wantedNode.getSuccessor().getValue());
                // remove successor from tree
                Node successor = wantedNode.getSuccessor();
                successor.parent.setLeft(null);
            } else if (wantedNode.hasPredecessor()) {
                // swap with predecessor, easy
                Node predecessor = wantedNode.getPredecessor();
                wantedNode.setValue(predecessor.getValue());
                predecessor.parent.setRight(null);
            } else {
                // neither has a proper predecessor nor a successor
                if (wantedNode.getRight() != null) {
                    // swap with right
                    Node righterNode = wantedNode.getRight().getRight();
                    wantedNode.setValue(wantedNode.getRight().value);
                    wantedNode.setRight(righterNode);
                    if (righterNode != null) {
                        righterNode.parent = wantedNode;
                    }
                } else if (wantedNode.getLeft() != null) {
                    // swap with left
                    Node lefterNode = wantedNode.getLeft().getLeft();
                    wantedNode.setValue(wantedNode.getLeft().value);
                    wantedNode.setLeft(lefterNode);
                    if (lefterNode != null) {
                        lefterNode.parent = wantedNode;
                    }
                } else {
                    // this is the root
                    this.root = null;
                }
            }
        }
    }

    private Node find(Node currNode, T key) {
        if (currNode == null) {
            return null;
        }
        if (currNode.value == key) {
            return currNode;
        }
        if (currNode.isBiggerThan(key)) {
            return find(currNode.getLeft(), key);
        } else {
            return find(currNode.getRight(), key);
        }
    }

    public int rank(T item) {
        /*
        * Implement a method which returns the count of elements smaller than a given value.
        * */
        int currentCount = 0;
        Node currNode = this.root;
        while (currNode != null) {
            if (currNode.getValue() == item) {
                // this is the exact item, take its left count
                if (currNode.getLeft() != null) {
                    currentCount += currNode.getLeft().getCount();
                }
                break;
            }
            if (currNode.isBiggerThan(item)) {
                currNode = currNode.getLeft();
            } else {
                // we're at a smaller node, take its left's count + 1 and go right
                // go right
                if (currNode.getLeft() != null) {
                    currentCount += currNode.getLeft().getCount();
                }
                currentCount += 1;
                currNode = currNode.getRight();
            }
        }

        return currentCount;
    }

    public T select(int n) {
        Node currNode = this.root;
        int smallerNodesCount = 0; // holds the total amount of nodes we've encountered that have a select less than N
        // this is because we need to take them into account when we recurse deeper

        while (true) {
            int currCount = 0;
            if (currNode.getLeft() != null) {
                currCount += currNode.getLeft().getCount();
            }
            if (currCount + smallerNodesCount > n) {
                // go left
                currNode = currNode.getLeft();
            } else if (currCount + smallerNodesCount < n) {
                // go right
                smallerNodesCount += currCount + 1;
                currNode = currNode.getRight();
            } else {
                return currNode.value;
            }
        }
    }

    class Node {
        private T value;
        private Node left;
        private Node right;
        public Node parent;

        private int childrenCount;

        public Node(T value, Node parent) {
            this.value = value;
            this.childrenCount = 1;
            this.parent = parent;
        }

        public boolean hasPredecessor() {
            /* Returns a boolean indicating if the current node has a predecessor */
            return this.left != null && this.left.right != null;
        }

        public boolean hasSuccessor() {
            /* Returns a boolean indicating if the current node has a successor */
            return this.right != null && this.right.left != null;
        }

        public Node getPredecessor() {
            Node currNode = this.left;
            while (currNode.getRight() != null) {
                currNode = currNode.getRight();
            }
            return currNode;
        }

        public Node getSuccessor() {
            Node currNode = this.right;
            while (currNode.getLeft() != null) {
                currNode = currNode.getLeft();
            }
            return currNode;
        }

        public T getValue() {
            return this.value;
        }

        public void setValue(T value) {
            this.value = value;
        }

        public Node getLeft() {
            return this.left;
        }

        public void setLeft(Node left) {
            this.left = left;
        }

        public Node getRight() {
            return this.right;
        }

        public void setRight(Node right) {
            this.right = right;
        }

        public int getCount() {
            int overallCount = 1;
            if (this.left != null) {
                overallCount += this.left.getCount();
            }
            if (this.right != null) {
                overallCount += this.right.getCount();
            }

            return overallCount;
        }

        public boolean isBiggerThan(Node other) {
            return this.value.compareTo(other.getValue()) > 0;
        }
        public boolean isBiggerThan(T other) {
            return this.value.compareTo(other) > 0;
        }

        @Override
        public String toString() {
            return this.value + "";
        }
    }
}

