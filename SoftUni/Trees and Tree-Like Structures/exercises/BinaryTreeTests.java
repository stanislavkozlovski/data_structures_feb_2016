package com.company;

/**
 * Created by netherblood on 29.05.17.
 */
import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public class BinaryTreeTests {

    @Test
    public void buildBinaryTree_forEachTraversal_inOrder_shouldWorkCorrectly() {
        // Arrange
        BinaryTree<String> binaryTree =
                new BinaryTree<>("*",
                        new BinaryTree<>("+",
                                new BinaryTree<>("3"),
                                new BinaryTree<>("2")),
                        new BinaryTree<>("-",
                                new BinaryTree<>("9"),
                                new BinaryTree<>("6")));

        // Act
        List<String> nodes = new ArrayList<>();
        binaryTree.eachInOrder(nodes::add);
        String[] actualResult = new String[nodes.size()];
        for (int i = 0; i < nodes.size(); i++) {
            actualResult[i] = nodes.get(i);
        }

        // Assert
        String[] expectedNodes = new String[] { "3", "+", "2", "*", "9", "-", "6" };
        Assert.assertArrayEquals(expectedNodes, actualResult);
    }

    @Test
    public void buildBinaryTree_forEachTraversal_postOrder_shouldWorkCorrectly() {
        // Arrange
        BinaryTree<String> binaryTree =
                new BinaryTree<>("*",
                        new BinaryTree<>("+",
                                new BinaryTree<>("3"),
                                new BinaryTree<>("2")),
                        new BinaryTree<>("-",
                                new BinaryTree<>("9"),
                                new BinaryTree<>("6")));

        // Act
        List<String> nodes = new ArrayList<>();
        binaryTree.eachPostOrder(nodes::add);
        String[] actualResult = new String[nodes.size()];
        for (int i = 0; i < nodes.size(); i++) {
            actualResult[i] = nodes.get(i);
        }

        // Assert
        String[] expectedNodes = new String[] { "3", "2", "+", "9", "6", "-", "*" };
        Assert.assertArrayEquals(expectedNodes, actualResult);
    }

    @Test
    public void buildBinaryTree_printIndentedPreOrder_shouldWorkCorrectly() {
        // Arrange
        BinaryTree<String> binaryTree =
                new BinaryTree<>("*",
                        new BinaryTree<>("-",
                                new BinaryTree<>("+",
                                        new BinaryTree<>("3"),
                                        new BinaryTree<>("2")),
                                new BinaryTree<>("*",
                                        new BinaryTree<>("9"),
                                        new BinaryTree<>("6"))),
                        new BinaryTree<>("8"));

        // Act
        String output = binaryTree.printIndentedPreOrder(0, new StringBuilder());

        // Assert
        String expectedOutput = "*\n  -\n    +\n      3\n      2\n    *\n      9\n      6\n  8\n";
        Assert.assertEquals(expectedOutput, output);
    }
}

