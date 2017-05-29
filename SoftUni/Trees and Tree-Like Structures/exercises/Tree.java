
import java.util.*;
import java.util.function.Consumer;

public class Tree<T> {
    private ArrayList<Tree<T>> children;
    public T value;
    public Tree(T value, Tree<T>... children) {
        this.value = value;
        this.children = new ArrayList<Tree<T>>();
        if (children.length > 0) {
            for (Tree<T> child: children) {
                this.children.add(child);
            }
        }

    }

    public String print(int indent, StringBuilder builder) {
        // Create a string with white spaces
        char[] charArray = new char[indent*2];
        Arrays.fill(charArray, ' ');
        String str = new String(charArray);

        builder.append(str);
        builder.append(this.value);
        builder.append('\n');
        for (Tree<T> child: this.children) {
            child.print(indent+1, builder);
        }
        return builder.toString();
    }

    public void each(Consumer<T> consumer) {
        consumer.accept(this.value);
        for (Tree<T> child: this.children) {
            child.each(consumer);
        }
    }

    public Iterable<T> orderDFS() {
        ArrayList<T> items = new ArrayList<T>();
        this.dfs(items);
        return items;
    }
    public void dfs(ArrayList<T> itemsToFill) {
        for (Tree<T> ch: this.children) {
            ch.dfs(itemsToFill);
        }
        itemsToFill.add(this.value);
    }

    public Iterable<T> orderBFS() {
        ArrayList<T> items = new ArrayList<T>();

        Queue<Tree<T>> nodes = new ArrayDeque<>();
        nodes.add(this);
        while (!nodes.isEmpty()) {
            Tree<T> currNode = nodes.poll();
            items.add(currNode.value);
            for (Tree<T> child : currNode.children) {
                nodes.add(child);
            }
        }
        return items;
    }

}