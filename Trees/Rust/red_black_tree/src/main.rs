
/*
TODO: Learn Rust borrowing and then continue!
*/

use std::rc::Rc;
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
    parent: Option<Rc<Node>>,
    left_child: Option<Rc<Node>>,
    right_child: Option<Rc<Node>>,
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
                            Rc::make_mut(child).unwrap().add_node(new_value);
                        }
                        _ => {panic!("Node with color {:?} and value {:?} should have a right child!", self.color, self.value);}
                    }
                }
            }
            None => {
                // create a new node
                self.color = Color::RED;
                self.value = Some(new_value);
                self.left_child = Some(Rc::new(LEAF));
                self.right_child = Some(Rc::new(LEAF));
                // TODO: Check for reorder
                
                self.check_reorder();
                
            }
        }
    }

    fn change_color(&mut self, color: Color) {
        self.color = color;
    }

    // fn recolor(&mut self, sibling: &Rc<Node>, grandfather: &Rc<Node>) {
    //     sibling.color = Color::BLACK;
    //     let mut parent = self.parent.as_mut().unwrap();
    //     parent.change_color(Color::BLACK);
    //     grandfather.color = Color::RED;
    // }

    // fn to_recolor(&mut self) -> bool {
    //     /* Returns a boolean indicating if the node is valid for a recolor. */
    //     let mut parent_is_left = false;
    //     if let Some(grandfather) = self.parent.as_mut().unwrap().parent.as_mut() {
    //         if grandfather.value.unwrap() > self.parent.unwrap().value.unwrap() {
    //             parent_is_left = true;
    //         }

    //         if parent_is_left {
    //             if let Some(sibling) = grandfather.right_child.as_ref() {
    //                 if sibling.color == Color::RED{
    //                     self.recolor(sibling, grandfather);
    //                     return true;
    //                 }
    //             } else if let Some(sibling) = grandfather.left_child.as_ref() {
    //                 if sibling.color == Color::RED {
    //                     return true;
    //                 }
    //             }
    //         }
    //     }
    //     // If no grandfather, return false
    //     false
    // }

    fn check_reorder(&mut self) {
        if let Some(parent) = self.parent.as_ref() {
            if parent.color == Color::RED {
                // need to reorder
                // check for recolor
                // determine parent - grandfather relationship    
                
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
        let mut root = Node { value: Some(5), color: Color::RED, parent: None, left_child: Some(Rc::new(LEAF)), right_child: Some(Rc::new(LEAF))};
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