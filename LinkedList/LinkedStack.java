public class LinkedStack<E> {

    private Node<E> firstNode;
    private int size;


    public int size() {
        return this.size;
    }

    private void setSize(int size) {
        this.size = size;
    }

    public void push(E element) {
        Node<E> newNode = new Node<E>(element, this.firstNode);
        this.firstNode = newNode;
        this.size++;
    }

    public E pop() {
        E el = this.firstNode.value;
        this.firstNode = this.firstNode.nextNode;
        this.size--;
        return el;
    }

    public E[] toArray() {
        E tkn[] = (E[])new Object[this.size];
        if (firstNode == null) {
            return tkn;
        }
        int idx = 0;
        while (firstNode.nextNode != null) {
            tkn[idx] = firstNode.value;
            firstNode = firstNode.nextNode;
            idx++;
        }
        tkn[idx] = firstNode.value;
        return tkn;
    }

    private class Node<E> {

        private E value;
        private Node<E> nextNode;

        public Node(E value) {
            this.value = value;
            this.nextNode = null;
        }

        public Node(E value, Node<E> nextNode) {
            this.value = value;
            this.nextNode = nextNode;
        }

        public Node<E> getNextNode() {
            return this.nextNode;
        }

        public void setNextNode(Node<E> nextNode) {
            this.nextNode = nextNode;
        }
    }
}