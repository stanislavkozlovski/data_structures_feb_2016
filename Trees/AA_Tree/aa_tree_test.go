package AA_Tree

import (
	"testing"
    "github.com/stretchr/testify/assert"
)






func TestFunctionalTestTree(t *testing.T) {
	// add items to the tree consecutively and test it
	// the given names, e.g A, B are put for easier orientation and reference
	tree := AATree{}
	tree.Add(100)
	/*
			100(A) 1
	 */
	A := tree.root
	assert.Equal(t, tree.root.value, 100)
	assert.Equal(t, tree.root.level, 1)
	assert.Nil(t, tree.root.right)
	assert.Nil(t, tree.root.left)

	tree.Add(101)
	/*
	         100(A) 1
	            \
	            101(B) 1
	no problem yet
	 */
	B := tree.root.right
	assert.Equal(t, B.value, 101)
	assert.Equal(t, B.parent.value, 100)
	assert.Equal(t, B.level, 1)
	/*
		Add 99, which should cause a skew and split
		 100(A) 1                   99(C)1                           100(A)2
		 /   \      SKEW  =>           \            SPLIT=>         /     \
	  99(C)1  101(B)1                100(A) 1                    99(C)1   101(B)1
		                                \
		                              101(B)1
	 */
	tree.Add(99)
	C := tree.root.left
	assert.Equal(t, C.value, 99)
	assert.Equal(t, C.level, 1)
	assert.Equal(t, C.parent.value, 100)
	assert.Nil(t, C.right)
	assert.Equal(t, B.parent.value, 100)
	assert.Equal(t, B.value, 101)
	assert.Equal(t, B.level, 1)
	assert.Equal(t, A.level, 2)
	/*
		Add 102 for health
		100(A)2
		/    \
	99(C)1   101(B)1
		       \
		       102(D)1
    */
	tree.Add(102)
	D := B.right
	assert.Equal(t, D.value, 102)
	assert.Equal(t, D.parent.value, 101)
	/*
	Add 103 for a skew
	    100(A)2                           100(A)2
		/    \                           /      \
	99(C)1   101(B)1                   99(C)1  102(D)2
		       \          ==>                  /    \
		       102(D)1                     101(B)1  103(E)1
		       \
		       103(E)1
	 */
	tree.Add(103)
	E := D.right
	assert.Equal(t, E.value, 103)
	assert.Equal(t, D.level, 2)
	assert.Equal(t, D.left.value, 101)
	assert.Nil(t, B.right)
	assert.Equal(t, B.parent.value, 102)
	assert.Equal(t, A.right.value, 102)
	assert.Equal(t, D.parent.value, 100)
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

func TestSplitDeepTree(t *testing.T) {
	/*
	255 (A)(10)                                              256 (B) (11)
	  \                                                     /    \
	  256 (B)(10)                                        255(A) 257(C) (10)
	    \                                                        \
	    257 (C)(10)                                             300 (D)
	      \                                                    /   \
	      300 (D)(9)                                         209  302
	    /   \                                                      \
(5)  209(F) 302 (E)(8)                                            304
	         \
	        304 (G)(7)
	 */
	A := aaNode {value: 255}
	B := aaNode {value: 256, parent: &A}
	C := aaNode {value: 257, parent: &B}
	D := aaNode {value: 300, parent: &C}
	E := aaNode {value: 302, parent: &D}
	F := aaNode {value: 209, parent: &D}
	G := aaNode {value: 304, parent: &E}
	A.right = &B
	B.right = &C
	C.right = &D
	D.right = &E
	D.left = &F
	E.right = &G
	tree := AATree{root:&A}

	tree.split(&A, &B, &C)

	assert.Nil(t, B.parent)
	assert.Equal(t, tree.root.value, B.value, "Root is not B	") // new root
	assert.Equal(t, B.left.value, A.value)
	assert.Equal(t, A.parent.value, B.value)
	assert.Nil(t, A.right)
	assert.Equal(t, B.right.value, 257)
	assert.Equal(t, C.parent.value, 256)
	assert.Equal(t, C.right.value, 300)
	assert.Equal(t, D.parent.value, 257)
	assert.Equal(t, D.left.value, 209)
	assert.Equal(t, D.right.value, 302)
	// no need to check further
}

/*
Performs a skew operation, given the two needed nodes
	12(A) 1                11(B)1
	 / \                     \
	/ 14(C)1   ===>          \
  11(B) 1                   12(A)1
                             \
                            14(C)1
 This will be in the middle of an invalid position and would require a skew to fix
 */
func TestSkewNewRoot(t *testing.T) {
	A := aaNode{value:12}
	B := aaNode{value:11, parent: &A}
	C := aaNode{value:14, parent: &A}
	A.right = &C
	A.left = &B
	tree := AATree{root: &A}

	tree.skew(&A, &B)

	assert.Equal(t, tree.root.value, 11, "Incorrect Root")
	assert.Equal(t, B.right.value, 12)
	assert.Equal(t, A.parent.value, 11)
	assert.Equal(t, A.right.value, 14)
	assert.Equal(t, C.parent.value, 12)
}

/*
          14(A)                                    14(A)
          /  \                                       /  \
       12(B) 15(C)                               12(B) 15(C)
      /   \                                      /   \
   11(E)  13(D)                               11(E)  13(D)
   /                                          /
 10(F)                                      9(G)
 /                                            \
9(G)                                          10(F)
 */
func TestSkewDeepTree(t *testing.T) {
	A := aaNode{value:14}
	B := aaNode{value:12, parent: &A}
	C := aaNode{value:15, parent: &A}
	E := aaNode{value:11, parent: &B}
	D := aaNode{value:13, parent: &B}
	F := aaNode{value:10, parent: &E}
	G := aaNode{value:9, parent: &F}
	A.left = &B
	A.right = &C
	B.right = &D
	B.left = &E
	E.left = &F
	F.left = &G
	tree := AATree{root: &A}

	tree.skew(&F, &G)

	assert.Equal(t, F.parent.value, 9)
	assert.Nil(t, F.left)
	assert.Equal(t, G.right.value, 10)
	assert.Equal(t, G.parent.value, 11)
	assert.Equal(t, E.left.value, 9)
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