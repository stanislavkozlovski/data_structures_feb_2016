package AA_Tree

import (
	"testing"
    "github.com/stretchr/testify/assert"
	"fmt"
)





/* // add items to the tree consecutively and test it */
func TestFunctionalTestTree(t *testing.T) {
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


/* Remove items from the tree consecutively and test it */
func TestFunctionalTestTreeRemoval(t *testing.T) {
	// Given this tree
	/*
	     ___3(A)3___
        /           \
     1(B)2         5(C)2
    /   \           /   \
0(D)1  2(E)1     4(F)1 6(G)1
	 */
	// Construct the tree
	A := aaNode{value: 3, level: 3}
	B := aaNode{value: 1, level: 2, parent: &A}
	C := aaNode{value: 5, level: 2, parent: &A}
	A.left = &B
	A.right = &C
	D := aaNode{value: 0, level: 1, parent: &B}
	E := aaNode{value: 2, level: 1, parent: &B}
	B.left = &D
	B.right = &E
	F := aaNode{value: 4, level: 1, parent: &C}
	G := aaNode{value: 6, level: 1, parent: &C}
	C.left = &F
	C.right = &G
	tree := AATree{root: &A}

	// Remove 0(D)1 from the tree
	/*
	Removing O(D)1 will cause a level discrepancy between B and B's left child,
	lowering B's level to 1. That in turn will cause a level discrepancy between A and B,
	lowering A's level to 2
	     ___3(A)2___
        /           \
     1(B)1         5(C)2
       \           /   \
      2(E)1     4(F)1 6(G)1
	 */
	// TODO: Test same with G level being 2, requiring a split in A, C, G
	tree.Remove(0)
	assert.Equal(t, A.level, 2)
	assert.Equal(t, B.level, 1)
	assert.Nil(t, B.left)

	// Remove 3(A)2 *the root* from the tree
	/*
	This will exchange 3(A)2 with 2(E)1 and remove the leaf
	2E takes the level of the removed node
	    ___2E(2)___
        /           \
     1(B)1         5(C)2
                   /   \
                4F(1)  6(G)1
      No rebalancing is required
	*/
	// Rename the nodes, since internally the A node is still alive, simply had its value switched
	tree.Remove(3)
	E = *tree.root
	B = *E.left
	C = *E.right
	F = *C.left
	G = *C.right

	assert.Equal(t, tree.root.value, 2)
	assert.Nil(t, tree.root.parent)
	assert.Equal(t, E.level, 2)
	assert.Equal(t, B.value, 1)
	assert.Equal(t, B.level, 1)
	assert.Equal(t, B.parent.value, 2)
	assert.Nil(t, B.right)
	assert.Equal(t, C.value, 5)
	assert.Equal(t, C.level, 2)
	assert.Equal(t, C.parent.value, 2)

	// Remove 1(B)1
	/*
	This will reduce E's level to 1 and
	2E takes the level of the removed node
	    ___2(E)1___                                            __2(E)1__
                   \                                                    \
                   5(C)1  This now causes a                           4(F)1
                   /   \   skew from C and F                              \
                4F(1)  6(G)1                                             5(C)1
                														   \
                														  6(G)1
	Which then causes a split in E, F and C

	   		__4(F)2__
	   	   /         \
	   	2(E)1       5(C)1
	   	   	           \
	   	   	          6(G)1
	*/
	tree.Remove(1)
	F = *tree.root
	E = *F.left
	C = *F.right
	G = *C.right

	// Assert that we assigned the right values to the variables
	// this is getting annoying but gotta do what you gotta do
	assert.Equal(t, F.value, 4)
	assert.Equal(t, E.value, 2)
	assert.Equal(t, C.value, 5)
	assert.Equal(t, G.value, 6)

	assert.Equal(t, tree.root.value, 4)
	assert.Equal(t, tree.root.level, 2)
	assert.Equal(t, C.value, 5)
	assert.Equal(t, C.level, 1)
	assert.Equal(t, C.parent.value, 4)
	assert.Nil(t, C.left)
	assert.Equal(t, E.level, 1)
	assert.Equal(t, E.parent.value, 4)
	assert.Nil(t, E.right)
	assert.Nil(t, E.left)
}


func TestRemovalWorstCase(t *testing.T) {
	/*
	The worst case when removing a node from the tree requires at most
	3 skews and 2 splits down the tree
	This showcases the worst possible imbalance in an AA tree
                	__2(A)2__
                   /        \
                1(Z)1      5(B)2
                         /      \
                      3(E)1     6(C)1
                         \          \
                          4(F)1     7(D)1
    					                      */
	// build the tree
	A := aaNode{value: 2, level: 2}
	Z := aaNode{value: 1, level: 1, parent: &A}
	B := aaNode{value: 5, level: 2, parent: &A}
	A.left = &Z
	A.right = &B
	E := aaNode{value: 3, level: 1, parent: &B}
	C := aaNode{value: 6, level: 1, parent: &B}
	B.left = &E
	B.right = &C

	F := aaNode{value: 4, level: 1, parent: &E}
	E.right = &F

	D := aaNode{value: 7, level: 1, parent: &C}
	C.right = &D

	tree := AATree{root: &A}
	/*
       Removing Z should cause the following:
       A be level 2 and not have 2 children, so its level will be reduced to 1, B will be a bigger level so
       its level would also be reduced to 1
     __2(A)1__         This causes a skew at 5B and 3E   __2(A)1__
*******      \                                                   \
*1(Z)1*     5(B)1                                               3(E)1
*******   /      \                                                  \
       3(E)1     6(C)1                                              5(B)1
          \          \                                             /   \
           4(F)1     7(D)1                                     4(F)1   6(C)1
                                                                         \
                                                                        7(D)1
                      This causes a skew at 5B and 4F now
   __2(A)1__       Followed by a split in A, E, F
        \                                                    3(E)2
       3(E)1                                               /      \
          \                                             2(A)1    4(F)1
          4(F)1                                                    \
            \                                                     5(B)1
           5(B)1                                                     \
              \                                                      6(C)1
              6(C)1                                                    \
                \                                                     7(D)1
               7(D)1
                  Followed by a split in F, B, C
                            3(E)2
                           /      \
                        2(A)1    5(B)2
                                 /   \
                            4(F)1    6(C)1
                                       \
                                      7(D)1

	 */
	tree.Remove(1)

	assert.Equal(t, tree.root.value, 3)
	assert.Equal(t, E.level, 2)
	assert.Nil(t, E.parent)
	assert.Equal(t, A.parent.value, 3)
	assert.Equal(t, A.level, 1)
	assert.Nil(t, A.left)
	assert.Nil(t, A.right)
	assert.Equal(t, B.level, 2)
	assert.Equal(t, B.parent.value, 3)
	assert.Equal(t, B.left.value, 4)
	assert.Equal(t, B.right.value, 6)
	assert.Equal(t, F.parent.value, 5)
	assert.Equal(t, F.level, 1)
	assert.Nil(t, F.left)
	assert.Nil(t, F.right)
	assert.Equal(t, C.parent.value, 5)
	assert.Equal(t, C.level, 1)
	assert.Equal(t, C.right.value, 7)
	assert.Nil(t, C.left)
	assert.Equal(t, D.parent.value, 6)
	assert.Equal(t, D.level, 1)
	assert.Nil(t, D.left)
	assert.Nil(t, D.right)
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
				Split on R, P, G
				the node A should be preserved
         11(R)                        15(P)
        /  \                         /     \
    10(K)   15(P)   ===“          11(R)    17(G)
          /   \                  /   \
       12(A) 17(G)            10(K)  12(A)
 */
func TestSplitPreservesLeftChild(t *testing.T) {
	R := aaNode{value: 11}
	K := aaNode{value: 10, parent: &R}
	P := aaNode{value: 15, parent: &R}
	A := aaNode{value: 12, parent: &P}
	G := aaNode{value: 17, parent: &P}
	R.left = &K
	R.right = &P
	P.left = &A
	P.right = &G
	tree := AATree{root: &R}
	tree.split(&R, &P, &G)

	assert.Equal(t, tree.root.value, 15)
	assert.Nil(t, tree.root.parent)
	assert.Equal(t, P.left.value, 11)
	assert.Equal(t, P.right.value, 17)
	assert.Equal(t, G.parent.value, 15)
	assert.Equal(t, R.parent.value, 15)
	assert.Equal(t, R.left.value, 10)
	assert.Equal(t, R.right.value, 12)  // important
	assert.Equal(t, A.parent.value, 11)
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
			129(J)2         			129(J)2
         /       \                   /       \
     108(K)2      130(I)1        108(K)2      130(I)1
     /    \                      /
105(H)1  109(L)1            105(H)1
 */
//func TestTreeRemoveLeaf(t *testing.T) {
//	J := aaNode{value: 129, level:2}
//	K := aaNode{value: 108, level:2, parent:&J}
//	I := aaNode{value: 130, level:1, parent:&J}
//	J.left = &K
//	J.right= &I
//	H := aaNode{value: 105, level:1, parent: &K}
//	L := aaNode{value: 109, level:1, parent:&K}
//	K.left = &H
//	K.right = &L
//	tree := AATree{root:&J}
//	tree.count = 5
//	tree.Remove(109)
//
//	assert.Equal(t, tree.count, 4)
//	assert.Nil(t, K.right)
//}

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