#[derive(Debug)]
#[derive(PartialEq)]
enum Color {
    BLACK,
    RED,
    NIL,
}

#[derive(Debug)]
struct Node {
    value: Option<i32>,
    color: Color,
    parent: Option<Box<Node>>,
    left_child: Option<Box<Node>>,
    right_child: Option<Box<Node>>,
}


impl Node {
    fn add_node(&mut self, new_value: i32) {
        match self.value {
            Some(value) => {
                if value == new_value {
                    panic!("There already isa  value {:?} in the tree!", value);
                } else if value > new_value {
                    println!("{:?} is bigger than {:?}, so the new node goes to the left!", value, new_value);
                    match self.left_child {
                        Some(ref mut child) => {
                            child.add_node(new_value);
                        }
                        _ => {panic!("Node with color {:?} and value {:?} should have a left child!", self.color, self.value);}
                    }
                } else {
                    println!("{:?} is smaller than {:?}, so the new node goes to the right!", value, new_value);
                    match self.right_child {
                        Some(ref mut child) => {
                            child.add_node(new_value);
                        }
                        _ => {panic!("Node with color {:?} and value {:?} should have a right child!", self.color, self.value);}
                    }
                }
            }
            None => {
                // create a new node
                self.color = Color::RED;
                self.value = Some(new_value);
                self.left_child = Some(Box::new(LEAF));
                self.right_child = Some(Box::new(LEAF));
                // TODO: Check for reorder

                // if self.parent.unwrap().color == Color::RED {
                //     // need to reorder
                // }
            }
        }
    }
}
const LEAF: Node = Node {
    value: None,
    color: Color::NIL,
    parent: None,
    left_child: None,
    right_child: None,
};

fn main() {
    println!("Hello, world!");
}

#[cfg(test)]
mod tests {
    use super::Color;
    use super::LEAF;
    use super::Node;
    
    #[test]
    fn test_binary_tree_ordering() {
        /* Add a couple of nodes and assert that they are on the right place! */
        let mut root = Node { value: Some(5), color: Color::RED, parent: None, left_child: Some(Box::new(LEAF)), right_child: Some(Box::new(LEAF))};
        root.add_node(2);
        root.add_node(1);
        root.add_node(6);
        // Should construct the following tree
        /*
                    5
                  /   \
                2      6
               /
             1       
        */
        assert_eq!(root.left_child.as_ref().unwrap().value.as_ref().unwrap().clone(), 2);
        assert_eq!(root.left_child.as_ref().unwrap().left_child.as_ref().unwrap().value.as_ref().unwrap().clone(), 1);
        
        assert_eq!(root.right_child.as_ref().unwrap().value.as_ref().unwrap().clone(), 6);
        
    }
}