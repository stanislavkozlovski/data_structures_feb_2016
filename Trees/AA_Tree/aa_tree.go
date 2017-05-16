package AA_Tree


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
			tree.checkSkew(&newNode)
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
	tree.checkSkew(node)
	tree.checkSplit(node)
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
	if grandParent != nil {
		if grandParent.value < parent.value {
			// new GP right
			grandParent.right = leaf
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
		and if its level is bigger or equal to his parent's*/
func (tree *AATree) checkSkew(node *aaNode) {
	parent := node.parent
	if parent != nil && parent.left == node && parent.level <= node.level {
		tree.skew(parent, node)
		// check for split, our parent would now be the middle element
		if parent.right != nil {
			grandParent := node
			if grandParent != nil && parent.right.isRightGrandChild(grandParent) && grandParent.level <= parent.right.level {
				// TODO: We never get in here, not sure if it works
				// I'm not even sure it's possible to get here
				tree.split(grandParent, parent, parent.right)
			}
		}
	}
}