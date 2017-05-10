package linked_list

import "errors"

type linkedListNode struct {
	value int
	next *linkedListNode
}

type LinkedList struct {
	root *linkedListNode
	tail *linkedListNode
	length int
}

func (ll *LinkedList) Add(newVal int) {
	newNode := new(linkedListNode)
	newNode.value = newVal
	if ll.length == 0 {
		ll.root = newNode
		ll.root.next = nil
	} else if ll.length == 1 {
		ll.tail = newNode
		ll.root.next = ll.tail
	} else {
		ll.tail.next = newNode
		ll.tail = newNode
	}

	ll.length++
}

func (ll *LinkedList) RemoveFirst() (err error) {
	if ll.length == 0 {
		return errors.New("There is nothing to remove!")
	} else if ll.length == 1 {
		ll.root = nil
	} else if ll.length == 2 {
		ll.root = ll.tail
		ll.tail = nil
	} else {
		ll.root = ll.root.next
	}

	ll.length--
	return
}

func (ll* LinkedList) PeekLast() (val int, err error) {
	if ll.length == 0 {
		return 0, errors.New("There is nothing to peek!")
	} else if ll.length == 1 {
		val = ll.root.value
	} else {
		val = ll.tail.value
	}

	return val, nil
}

