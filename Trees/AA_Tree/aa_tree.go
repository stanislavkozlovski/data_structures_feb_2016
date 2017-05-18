package AA_Tree

import "fmt"

type aaNode struct {
	parent *aaNode
	left *aaNode
	right *aaNode
	value int
	level int
}

type AATree struct {
	root *aaNode
	count int
}
func (node *aaNode) getGrandparent() *aaNode {
	parent := node.parent
	if parent == nil {
		return nil
	}
	grandParent := parent.parent
	return grandParent
}

/*
Returns a boolean indicating if the given aaNode is the right grandchild
1								5
 \								 \
  2								  7
   \							 /
    3 							6
 In the above example, 3 is a right grandchild of 1.
 6 is not a right grandchild of 5
 */
func (node *aaNode) isRightGrandChild(grandParent *aaNode) bool {
	return grandParent.right != nil && grandParent.right.right != nil && grandParent.right.right == node
}

/* Adds a value into the tree */
func (tree *AATree) Add(value int) {
	if tree.root == nil {
		// No root, create new one
		newNode := aaNode{
			parent: nil,
			left: nil,
			right: nil,
			value: value,
			level: 1,
		}
		tree.root = &newNode
	} else {
		tree.add(value, tree.root)
	}

	tree.count++
}

/* The internal add function, which traverses the trees nodes until it lands at the correct node,
left/right of which the new node should be inserted.
 Backtracing from the recursion, we check if we should perform a split or skew operation*/
func (tree *AATree) add(value int, node *aaNode) {
	if value < node.value {
		// go left
		if node.left == nil {
			// new left aaNode
			newNode := aaNode{
				parent: node,
				left: nil,
				right: nil,
				value: value,
				level: 1,
			}
			node.left = &newNode

			// We've added a left node, check for a need to skew
			tree.checkSkew(&newNode, true)
		} else {
			tree.add(value, node.left)
		}
	} else if value > node.value {
		// go right
		if node.right == nil {
			// new right aaNode
			newNode := aaNode{
				parent: node,
				left: nil,
				right: nil,
				value: value,
				level: 1,
			}
			node.right = &newNode

			// We've added a right node, check for a need to split
			tree.checkSplit(&newNode)
		} else {
			tree.add(value, node.right)
		}
	} else {
		panic("Equal elements are unsupported!")
	}

	// Backtracking through the path, check for skews and splits
	tree.checkSkew(node, true)
	tree.checkSplit(node)
}
//
func (tree *AATree) Remove(value int) {
	if tree.root == nil {
		panic("There is nothing to remove!")
	}

	tree.remove(value, tree.root)
	tree.count--
}

 //TODO: Implement level decrementation
func (tree *AATree) remove(value int, node *aaNode) {
	if node == nil {
		// Maybe pass silently
		tree.count++
		panic("There is no such element in the tree!")
	}

	if node.value != value {
		// recurse downwards until we find the right node
		if node.value > value {
			// go left
			tree.remove(value, node.left)
		} else {
			// go right
			tree.remove(value, node.right)
		}
	} else {
		// were at the value we want
		// TODO: Remove
		if node.left == nil && node.right == nil {
			// we're at a leaf, simply remove
			parent := node.parent
			if parent.left == node {
				parent.left = nil
			} else {
				parent.right = nil
			}
		} else if node.left == nil {
			// there is a right node, get the predecessor
			predecessor := node.right
			for predecessor.left != nil {
				predecessor = predecessor.left
			}
			// swap both nodes
			// TODO: Right child of predecessor might get lost?
			node.value = predecessor.value
			//node.level = predecessor.level
			predParent := predecessor.parent
			// Remove the predecessor from the tree
			if predParent.right == predecessor {
				predParent.right = nil
			} else {
				predParent.left = nil
			}
		} else  {
			// there is a left node
			// TODO: This is predecessor
			sucessor := node.left
			for sucessor.right != nil {
				sucessor = sucessor.right
			}

			// swap both nodes
			// TODO: Left child of successor might get lost?
			node.value = sucessor.value
			//node.level = sucessor.level
			sucParent := sucessor.parent
			// Remove the successor from the tree
			if sucParent.right == sucessor {
				sucParent.right = nil
			} else {
				sucParent.left = nil
			}
		}
	}

	//  The node is removed, fix levels
	/*
		if (root->link[0]->level < root->level - 1 || root->link[1]->level < root->level - 1)
		{
			if (root->link[1]->level > --root->level)
			{
				root->link[1]->level = root->level;
			}

			root = skew(root);
			root->link[1] = skew(root->link[1]);
			root->link[1]->link[1] = skew(root->link[1]->link[1]);
			root = split(root);
			root->link[1] = split(root->link[1]);
		}
	*/

	// left node should be exactly one level less
	leftLevelIsWrong := (node.left != nil && node.left.level < node.level - 1) ||
			(node.left == nil && node.level > 1)  // if we dont have a left node, our level should be 1

	 // right level should be exactly one less or equal
	rightLevelIsWrong := (node.right != nil && node.right.level < node.level - 1) ||
			(node.right == nil && node.level > 1)  // if we dont have a right node, our level should be 1

	// If there is no break in the levels there is no need  to do rebalance operations
	if leftLevelIsWrong || rightLevelIsWrong {
		node.level--  // decrease level
		if node.right != nil && node.right.level > node.level {
			// right node had the equal level and is now bigger after our decrease, so we reset its level
			node.right.level = node.level
		}
		//if (node.value == 2) {
		//	fmt.Println("WERE AT THE ROOT")
		//}
		tree.checkSkew(node, false)
		if node.left != nil {
			 tree.checkSkew(node.left, false)
		}
		if node.right != nil {
			tree.checkSkew(node.right, false)
		}
		//if node.value == 2 {
		//fmt.Println("Root right is", node.right.value, "with level", node.right.level)
		//
		//}
		if node.right != nil && node.right.left != nil {
			//fmt.Println("checking skew", node.right.left.value, "with level", node.right.left.level)
			tree.checkSkew(node.right.left, false)
			//fmt.Println(node.right.value)
		}
		if node.right != nil && node.right.right != nil {
			tree.checkSkew(node.right.right, false)
		}
		//if node.right != nil && node.right.right != nil && node.right.right.left != nil {
		//	tree.checkSkew(node.right.right.left)
		//}
		tree.checkSplit(node)

		if node.right != nil && node.right.right != nil {
			tree.checkSplit(node.right.right)
		}
		if node.right != nil {
			tree.checkSplit(node.right)
		}
		//if node.right != nil && node.right.right != nil && node.right.right.right != nil {
		//	tree.checkSplit(node.right.right.right)
		//}
	}

}

/*
Performs a split operation, given the three needed nodes
11(R)                	12
  \			    	   /  \
   12(P)   ===>		 11    13
    \
     13(C)
     P becomes the new root, where any leaf that was left of P is now to the right of R
     i.e if 12 had a left child 11.5, 11.5 should become the right child of the new 11
 */
func (tree *AATree) split(grandParent, parent, leaf *aaNode) {
	// fixes grandgrandparent's link
	GGParent := grandParent.parent
	if GGParent != nil {
		if GGParent.left == grandParent {
			GGParent.left = parent
		} else {
			GGParent.right = parent
		}
	}

	if grandParent == tree.root {
		// we now have a new root
		tree.root = parent
	}
	parent.parent = GGParent  // R parent is now some upwards node
	grandParent.parent = parent  // R parent is now P
	grandParent.right = parent.left
	if parent.left != nil {
		parent.left.parent = grandParent
	}

	parent.left = grandParent
	parent.level++
}

/* Given a node, check if a Split operation should be performed, by checking the node's grandparent level
	The node we're given would be the downmost one in the split operation */
func (tree *AATree) checkSplit(node *aaNode) {
	grandParent := node.getGrandparent()
	if grandParent != nil && node.isRightGrandChild(grandParent) && grandParent.level <= node.level {
		tree.split(grandParent, node.parent, node)
	}
}

/*
Performs a skew operation, given the two needed nodes
	12(A) 1                11(B)1
	/          ===>          \
  11(B) 1                   12(A)1
 */
func (tree *AATree) skew(parent, leaf *aaNode) {
	grandParent := parent.parent
	//if leaf.value == 4 {	fmt.Println("grandparent is", grandParent.value)
//}
	if grandParent != nil {
		if grandParent.value < parent.value {
			// new GP right
			//if leaf.value == 4 {	fmt.Println("grandparent is", grandParent.value) }
			grandParent.right = leaf
			//fmt.Println(leaf.value)
			//fmt.Println(grandParent.right.value)
		} else {
			// new GP left
			grandParent.left = leaf
		}
	} else {
		// new root
		tree.root = leaf
	}

	// figure out where the LEAF
	leaf.parent = grandParent
	oldRight := leaf.right
	leaf.right = parent
	parent.left = oldRight
	if oldRight != nil {
		oldRight.parent = parent
	}
	parent.parent = leaf
}

/* Given a node, check is a Skew operation should be performed by checking if its a left child
		and if its level is bigger or equal to his parent's
	param: checkForSplit - a boolean indicating if we want to split if it's ok to split after the skew
			We generally don't want to do that in deletions, as in the example on the TestFunctionalTestTreeRemoval function
			where we remove 1 from the tree
	*/
func (tree *AATree) checkSkew(node *aaNode, checkForSplit bool) {
	parent := node.parent
	if parent != nil && parent.left == node && parent.level <= node.level {
		tree.skew(parent, node)
		// check for split, our parent would now be the middle element
		if parent.right != nil && checkForSplit {
			grandParent := node
			if grandParent != nil && parent.right.isRightGrandChild(grandParent) && grandParent.level <= parent.right.level {
				tree.split(grandParent, parent, parent.right)
			}
		}
	}
}