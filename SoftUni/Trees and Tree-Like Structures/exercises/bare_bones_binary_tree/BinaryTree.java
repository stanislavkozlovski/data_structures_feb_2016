//package com.company;

import java.util.Arrays;
import java.util.function.Consumer;

public class BinaryTree<T extends Comparable<T>> {
    private T value;
    BinaryTree<T> left;
    BinaryTree<T> right;
    public BinaryTree(T value) {
        this.value = value;
    }

    public BinaryTree(T value, BinaryTree<T> child) {
        this.value = value;
        if (child.value.compareTo(this.value) == 1) {
            this.right = child;
        } else {
            this.left = child;
        }
    }

    public BinaryTree(T value, BinaryTree<T> leftChild, BinaryTree<T> rightCHild) {
        this.value = value;
        this.left = leftChild;
        this.right = rightCHild;
    }

    // append output to builder
    public String printIndentedPreOrder(int indent, StringBuilder builder) {
        char[] charArray = new char[indent*2];
        Arrays.fill(charArray, ' ');
        String str = new String(charArray);

        builder.append(str);
        builder.append(this.value);
        builder.append('\n');
        if (this.left != null) {
            this.left.printIndentedPreOrder(indent+1, builder);
        }
        if (this.right != null) {
            this.right.printIndentedPreOrder(indent+1, builder);
        }

        return builder.toString();
    }

    public void eachInOrder(Consumer<T> consumer) {
        if (this.left != null) {
            this.left.eachInOrder(consumer);
        }
        consumer.accept(this.value);

        if (this.right != null) {
            this.right.eachInOrder(consumer);
        }
    }

    public void eachPostOrder(Consumer<T> consumer) {
        if (this.left != null) {
            this.left.eachPostOrder(consumer);
        }
        if (this.right != null) {
            this.right.eachPostOrder(consumer);
        }
        consumer.accept(this.value);
    }
}
