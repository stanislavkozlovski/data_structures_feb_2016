package AA_Tree

import (
	"log"
)

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
}

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
			if node.level <= newNode.level {
				// skew
				tree.skew(node, &newNode)
				// check for split, our parent (node) would now be the middle element
				if node.right != nil {
					grandParent := node.parent
					if grandParent != nil && node.right.isRightGrandChild(grandParent) && grandParent.level <= node.right.level {
						// need to split
						tree.split(grandParent, node, node.right)
					}
				}
			}
		} else {
			tree.add(value, node.left)
		}
	} else {
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
			if newNode.parent.level < newNode.level {
				log.Fatal("New Right Node's parent cannot have a lesser level than him!")
			}

			grandParent := newNode.getGrandparent()
			if grandParent != nil && newNode.isRightGrandChild(grandParent) && grandParent.level <= newNode.level {
				// need to split
				tree.split(grandParent, node, &newNode)
			}
		} else {
			tree.add(value, node.right)
		}
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
	// fix grandgrandparent link
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
	leaf.parent = grandParent
	leaf.right = parent
	parent.left = nil
	parent.parent = leaf
}