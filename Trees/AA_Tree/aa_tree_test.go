package AA_Tree

import (
	"testing"
    "github.com/stretchr/testify/assert"
)


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
func TestSplitVanilla(t *testing.T) {
	/*
	 255                     255
	 /                       /
	11(R)                	13
     \			    	   /  \
    13(P)   ===>		 11    14
   /    \                 \
12(L) 14(C)               12
	 */
	// build sample tree
	testParent := aaNode{value:255}
	R := aaNode{value: 11, parent: &testParent}
	P := aaNode{value: 13, parent: &R}
	L := aaNode{value: 12, parent: &P}
	C := aaNode{value: 14, parent: &P}
	testParent.left = &R
	R.right = &P
	P.left = &L
	P.right = &C

	tree := AATree{root: &testParent}
	tree.split(&R, &P, &C)

	assert.Equal(t, R.value, L.parent.value, "L's parent is not R")
	assert.Equal(t, R.right.value, L.value, "R's right child is not L")
	assert.Nil(t, R.left)
	assert.Equal(t, R.parent, &P, "R's parent is not P")
	assert.Equal(t, P.left, &R, "P's left child is not R")
	assert.Equal(t, P.right, &C, "P's right child is not P")
	assert.Equal(t, C.parent, &P, "C's parent is not P")
	assert.Equal(t, P.parent, &testParent, "R's parent is not the testParent root")
	assert.Equal(t, testParent.left, &P, "testParent's left child is not P")
	// assert all levels are the same except for P's
	assert.Equal(t, P.level, 1)
	assert.Equal(t, C.level, 0)
	assert.Equal(t, L.level, 0)
	assert.Equal(t, R.level, 0)
	assert.Equal(t, testParent.level, 0)
}

/*
Returns a boolean indicating if the given aaNode is the right grandchild
1								5					10
 \								 \				  /
  2								  7				5
   \							 /				 \
    3 							6				  9
 In the above example, 3 is a right grandchild of 1.
 6 is not a right grandchild of 5
 9 is not a right grandchild of 9
 */
func TestIsRightGrandchild(t *testing.T) {
	rightGrandChild := aaNode {value: 3}
	middleChild := aaNode {value: 2, right: &rightGrandChild}
	root := aaNode {value: 1, right: &middleChild}
	middleChild.parent = &root
	rightGrandChild.parent = &middleChild

	if !rightGrandChild.isRightGrandChild(&root) {
		t.Fail()
	}
}

func TestIsRightGrandchildReturnsFalse(t *testing.T) {
	rightGrandChild := aaNode {value: 6}
	middleChild := aaNode {value: 7, left: &rightGrandChild}
	root := aaNode {value: 5, right: &middleChild}
	middleChild.parent = &root
	rightGrandChild.parent = &middleChild

	if rightGrandChild.isRightGrandChild(&root) {
		t.Fail()
	}
}

func TestIsRightGrandchildWithLeftGrandchild(t *testing.T) {
	leftGrandChild := aaNode {value: 5}
	middleChild := aaNode {value: 6, left: &leftGrandChild}
	root := aaNode {value: 7, left: &middleChild}
	middleChild.parent = &root
	leftGrandChild.parent = &middleChild

	if leftGrandChild.isRightGrandChild(&root) {
		t.Fail()
	}
}