package linked_list

import (
	"testing"
	"fmt"
)

func TestLengthIncreasesOnAdd(t *testing.T) {
	var linkedList LinkedList
	for _, i := range []int{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15} {
		linkedList.Add(i)
		if i != linkedList.length {
			fmt.Printf("%v was not equal to expected length %v", linkedList.length, i)
			t.Fail()
		}
	}
}

func TestRemoveFirstDecreasesLength(t *testing.T) {
	var linkedList LinkedList
	removedElements := 0
	for _, i := range []int{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15} {
		linkedList.Add(i)
		if i % 5 == 0 {
			linkedList.RemoveFirst()
			removedElements++
			if i-removedElements != linkedList.length{
				fmt.Printf("%v was not equal to expected length %v\n", linkedList.length, i)
				t.Fail()
			}
		}
	}
}

func TestRemoveFirstReturnErrOnNoElements(t *testing.T) {
	var linkedList LinkedList
	err := linkedList.RemoveFirst()
	if err == nil {
		fmt.Println("Should not be able to remove anything on an empty list")
		t.Fail()
	}
}

func TestPeekLastNoElementsReturnsErr(t *testing.T) {
	var linkedList LinkedList
	_, err := linkedList.PeekLast()
	if err == nil {
		fmt.Println("Should not be able to peek anything on an empty list")
		t.Fail()
	}
}

func TestPeekLastElementOnOneElement(t *testing.T) {
	var linkedList LinkedList
	linkedList.Add(2)
	val, err := linkedList.PeekLast()
	if err != nil {
		fmt.Println(err)
		t.Fail()
	}

	if val != 2 {
		fmt.Printf("PeekLast returned %v, expected %v", val, 2)
		t.Fail()
	}
}

func TestPeekLastElementOnMultipleElements(t *testing.T) {
	var linkedList LinkedList
	for _, i := range []int{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15} {
		linkedList.Add(i)
		lastVal, err := linkedList.PeekLast()
		if err != nil {
			fmt.Println(err)
			t.Fail()
		}
		if i != lastVal{
			fmt.Printf("%v was not equal to expected last element %v\n", lastVal, i)
			t.Fail()
		}
	}
}

func TestPeekLastElementDoesNotChangeLength(t *testing.T) {
	var linkedList LinkedList
	for _, i := range []int{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15} {
		linkedList.Add(i)
		linkedList.PeekLast()
		if i != linkedList.length {
			fmt.Printf("%v was not equal to expected length %v", linkedList.length, i)
			t.Fail()
		}
	}
}