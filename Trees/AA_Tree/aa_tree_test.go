package AA_Tree

import (
	"testing"
    "github.com/stretchr/testify/assert"
	"fmt"
)






func TestFunctionalTestTree(t *testing.T) {
	// add items to the tree consecutively and test it
	// the given names, e.g A, B are put for easier orientation and reference
	fmt.Println("")  // so that I don't have to always remove the "fmt" import
	tree := AATree{}
	tree.Add(100)
	assert.Equal(t, tree.count, 1)


	/*
			100(A) 1
	 */
	A := tree.root
	assert.Equal(t, tree.root.value, 100)
	assert.Equal(t, tree.root.level, 1)
	assert.Nil(t, tree.root.right)
	assert.Nil(t, tree.root.left)

	tree.Add(101)
	assert.Equal(t, tree.count, 2)
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
	assert.Equal(t, tree.count, 3)

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
	assert.Equal(t, tree.count, 4)

	D := B.right
	assert.Equal(t, D.value, 102)
	assert.Equal(t, D.parent.value, 101)
	/*
	Add 103 for a split
	    100(A)2                           100(A)2
		/    \                           /      \
	99(C)1   101(B)1                   99(C)1  102(D)2
		       \          ==>                  /    \
		       102(D)1                     101(B)1  103(E)1
		       \
		       103(E)1
	 */
	tree.Add(103)
	assert.Equal(t, tree.count, 5)

	E := D.right
	assert.Equal(t, E.value, 103)
	assert.Equal(t, D.level, 2)
	assert.Equal(t, D.left.value, 101)
	assert.Nil(t, B.right)
	assert.Equal(t, B.parent.value, 102)
	assert.Equal(t, A.right.value, 102)
	assert.Equal(t, D.parent.value, 100)

	/*
	Add 104
		   100(A)2
		  /      \
		99(C)1  102(D)2
				/    \
			101(B)1  103(E)1
			           \
			          104(F)1
	 */
	tree.Add(104)
	assert.Equal(t, tree.count, 6)

	F := E.right
	assert.Equal(t, F.value, 104)
	assert.Equal(t, F.parent.value, 103)
	assert.Equal(t, E.level, 1)
	assert.Nil(t, E.left)

	/*
	Add 105 for a split                               This should cause another split
		   100(A)2								100(A)2										         ---102(D)3---
		  /      \						        /     \												/            \
		99(C)1  102(D)2				==>		99(C)1	  102(D)2				==>				     100(A)2	     104(F)2
				/    \								/       \									/	\			 /    \
			101(B)1  103(E)1        		     101(B)1   104(F)2							99(C)1  101(B)1	 103(E)1  105(H)1
			           \									/   \
			          104(F)1							103(E)1  105(H)1
			             \
			             105(H)1
	 */
	tree.Add(105)
	assert.Equal(t, tree.count, 7)

	H := F.right
	assert.Equal(t, H.value, 105)
	assert.Equal(t, H.parent.value, 104)
	assert.Equal(t, tree.root.value, 102)
	assert.Equal(t, tree.root.level, 3)
	assert.Nil(t, tree.root.parent)

	assert.Equal(t, A.parent.value, 102)
	assert.Equal(t, A.right.value, 101)
	assert.Equal(t, A.left.value, 99)
	assert.Equal(t, A.level, 2)

	assert.Equal(t, B.parent.value, 100)
	assert.Equal(t, C.parent.value, 100)

	assert.Nil(t, E.left)
	assert.Nil(t, E.right)
	assert.Equal(t, F.level, 2)
	assert.Equal(t, F.left.value, 103)
	assert.Equal(t, F.right.value, 105)

	/*
	Add 130
		 ---102(D)3---
		/            \
     100(A)2	     104(F)2
	/	\			 /    \
99(C)1  101(B)1	 103(E)1  105(H)1
                             \
                             130(I)1
	 */
	tree.Add(130)
	assert.Equal(t, tree.count, 8)

	I := H.right
	assert.Equal(t, I.value, 130)
	assert.Equal(t, I.parent.value, 105)
	assert.Equal(t, H.level, 1)

	/*
	Add 129 for a skew
		 ---102(D)3---                             	         ---102(D)3---
		/            \                             	        /              \
     100(A)2	     104(F)2                            100(A)2	         104(F)2
	/	\			 /    \                          	/	\			  /    \
99(C)1  101(B)1	 103(E)1  105(H)1    ==>           99(C)1  101(B)1	 103(E)1  105(H)1
                             \                                                  \
                             130(I)1                                            129(J)1
                             /                                                     \
                           129(J)1                                                 130(I)1

                           Which causes a split

               ---102(D)3---
  	        /              \
       100(A)2	         104(F)2
    	/	\			  /    \
  99(C)1  101(B)1	 103(E)1  129(J)2
                              /     \
                          105(H)1   130(I)1
	 */
	tree.Add(129)
	assert.Equal(t, tree.count, 9)

	J := F.right
	assert.Equal(t, J.value, 129)
	assert.Equal(t, J.level, 2)
	assert.Equal(t, J.left.value, 105)
	assert.Equal(t, J.right.value, 130)
	assert.Equal(t, H.parent.value, 129)
	assert.Equal(t, I.parent.value, 129)

	assert.Nil(t, I.left)
	assert.Nil(t, I.right)
	assert.Nil(t, H.left)
	assert.Nil(t, H.right)

	/*
	Add 108

		____102(D)3______
	   /                 \
   100(A)2              104(F)2
   /    \               /     \
99(C)1  101(B)1     103(E)1   129(J)2
                              /      \
                           105(H)1   130(I)1
                              \
                              108(K)1
	 */
	tree.Add(108)
	assert.Equal(t, tree.count, 10)

	K := H.right
	assert.Equal(t, K.value, 108)
	assert.Equal(t, K.level, 1)
	assert.Equal(t, K.parent.value, 105)
	assert.Equal(t, H.level, 1)

	/*
	Add 109, now it gets scary

			________102(D)3______________
		  /                             \
	   100(A)2                         104(F)2
	  /      \                       /        \
   99(C)1   101(B)1 	         103(E)1      129(J)2
                                             /       \
                                         105(H)1      130(I)1
                                             \
                                            108(K)1
                                               \
                                               109(L)1

	This triggers a split in between H, K and L
			________102(D)3______________
		  /                             \
	   100(A)2                         104(F)2
	  /      \                       /        \
   99(C)1   101(B)1 	         103(E)1      129(J)2
                                             /       \
                                         108(K)2      130(I)1
                                         /    \
                                    105(H)1  109(L)1
    This triggers a skew in between K and J, since they're the same level

    	    ________102(D)3______________
		  /                             \
	   100(A)2                         104(F)2
	  /      \                       /        \
   99(C)1   101(B)1 	         103(E)1      108(K)2
                                             /       \
                                         105(H)1     129(J)2
                                                     /      \
                                                 109(L)1     130(I)1
    This should cause a split in between J, K and F
      	    ________102(D)3______
		  /                      \
	   100(A)2                  __108(K)3__
	  /      \                /            \
 99(C)1   101(B)1 	      104(F)2         129(J)2
                         /   \              /    \
                   103(E)1  105(H)1      109(L)1  130(I)1
	 */
	// test the whole left subtree
	tree.Add(109)
	assert.Equal(t, tree.count, 11)
	L := J.left

	assert.Equal(t, tree.root.right.value, 108)
	assert.Equal(t, K.parent.value, 102)
	assert.Equal(t, K.level, 3)
	assert.Equal(t, K.left.value, 104)
	assert.Equal(t, K.right.value, 129)

	// test F subtree
	assert.Equal(t, F.parent.value, 108)
	assert.Equal(t, F.left.value, 103)
	assert.Equal(t, F.right.value, 105)
	assert.Equal(t, E.parent.value, 104)
	assert.Equal(t, H.parent.value, 104)
	assert.Nil(t, H.left)
	assert.Nil(t, H.right)
	assert.Nil(t, E.left)
	assert.Nil(t, E.right)

	// test J subtree
	assert.Equal(t, J.parent.value, 108)
	assert.Equal(t, J.level, 2)
	assert.Equal(t, J.left.value, 109)  // TODO: FAILS
	assert.Equal(t, J.right.value, 130)
	assert.Equal(t, I.parent.value, 129)
	assert.Equal(t, L.parent.value, 129)

	assert.Nil(t, L.left)
	assert.Nil(t, L.right)
	assert.Nil(t, I.left)
	assert.Nil(t, I.right)
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
			129(J)2                                  108(K)2
         /       \                                 /       \
     108(K)2      130(I)1  ==>                  105(H)1     129(J)2
     /    \                                                  /   \
105(H)1  109(L)1                                        109(L)  130(I)1
Assert that the L node was preserved
 */
func TestSkewPreserveRightChild(t *testing.T) {
	J := aaNode{value: 129, level:2}
	K := aaNode{value: 108, level:2, parent:&J}
	I := aaNode{value: 130, level:1, parent:&J}
	J.left = &K
	J.right= &I
	H := aaNode{value: 105, level:1, parent: &K}
	L := aaNode{value: 109, level:1, parent:&K}
	K.left = &H
	K.right = &L
	tree := AATree{root:&J}

	tree.skew(&J, &K)

	assert.Equal(t, tree.root.value, 108)
	assert.Equal(t, K.left.value, 105)
	assert.Equal(t, K.right.value, 129)
	assert.Equal(t, J.parent.value, 108)

	assert.Equal(t, J.left.value, 109) // important
	assert.Equal(t, J.right.value, 130)

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