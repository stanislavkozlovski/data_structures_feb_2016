:BLACK
:RED
:NIL_C
:LEFT
:RIGHT

# Contain combinations of directions
DIRECTIONS = {
    [:LEFT, :RIGHT] => 'LR',
    [:RIGHT, :LEFT] => 'RL',
    [:RIGHT, :RIGHT] => 'RR',
    [:LEFT, :LEFT] => 'LL'
}

class Node
  attr_accessor :value, :color, :parent, :left, :right

  def initialize(value, color, parent, left, right)
    @value = value
    @color = color
    @parent = parent
    @left = left
    @right = right
  end

  def ==(other)
    if self.color == :NIL_C && other.color==self.color
      return true
    end
    same_parents = false
    if self.parent.nil? || other.parent.nil?
      same_parents = self.parent.nil? && other.parent.nil?
    else
      same_parents = self.parent.value == other.parent.value
    end

    self.value == other.value && self.color == other.color && same_parents
  end

  def has_children?
    self.get_children_count != 0
  end

  def get_children_count
    if self.color == COLORS[:NIL_C]
      return 0
    end

    if self.left.color != COLORS[:NIL_C] && self.right.color != COLORS[:NIL_C]
      return 2
    elsif self.left.color != COLORS[:NIL_C] || self.right.color != COLORS[:NIL_C]
      return 1
    else
      return 0
    end
  end

  def to_s
    "#{@color} #{@value}"
  end
  def inspect
    to_s
  end
end


class RedBlackTree
  @@nil_leaf = Node.new(value=NIL, color=:NIL_C, parent=NIL, left=NIL, right=NIL)
  attr_accessor :count, :root
  def initialize
    @count = 0
    @root = NIL
  end

  def add(value)
    if @root.nil?
      @root = Node.new(value=value, color=:BLACK, parent=NIL, left=@@nil_leaf, right=@@nil_leaf)
      @count += 1
      return
    end

    parent, direction = find_parent value
    if direction.nil?
      return  # value is in the tree
    end

    new_node = Node.new(value=value, color=:RED, parent=parent, left=@@nil_leaf, right=@@nil_leaf)
    if direction == :LEFT
      parent.left = new_node
    else
      parent.right = new_node
    end

    try_rebalance new_node
    @count += 1
  end

  def try_rebalance(new_node)
    parent = new_node.parent
    value = new_node.value

    if parent.nil? ||  # what the fuck?
        parent.parent.nil? || # parent is root
        parent.color != :RED  # no red-red, no problem :)
      return
    end

    grandfather = parent.parent
    direction = if parent.value > new_node.value then :LEFT else :RIGHT end
    parent_direction = if grandfather.value > parent.value then :LEFT else :RIGHT end
    uncle = if parent_direction == :LEFT then grandfather.right else grandfather.left end
    general_direction = DIRECTIONS[[direction, parent_direction]]

    if uncle == @@nil_leaf || uncle.color == :BLACK
      if general_direction == 'LL'
        # LL => Right rotation
        right_rotation(new_node, parent, grandfather, to_recolor=true)
      elsif general_direction == 'RR'
        # RR => Left rotation
        left_rotation(new_node, parent, grandfather, to_recolor=true)
      elsif general_direction == 'LR'
        # LR => Right rotation, left rotation
        right_rotation(NIL, new_node, parent, to_recolor=false)
        # due to the right rotation, parent and new_node positions have switched
        left_rotation(parent, new_node, grandfather, to_recolor=true)
      elsif general_direction == 'RL'
        # RL => Left rotation, right rotation
        left_rotation(NIL, new_node, parent, to_recolor=false)
        # due to the left rotation, parent and new_node positions have switches
        right_rotation(parent, new_node, grandfather, to_recolor=true)
      end
    else
      # uncle is red, simply recolor
      recolor(grandfather)
    end

  end

  def right_rotation(node, parent, grandfather, to_recolor=false)
    grand_grandfather = grandfather.parent
    # grandfather will become the right child of parent
    update_parent(node=parent, parent_old_child=grandfather, new_parent=grand_grandfather)

    old_right = parent.right
    parent.right = grandfather
    grandfather.parent = parent
    grandfather.left = old_right
    old_right.parent = grandfather

    if to_recolor  # recolor the nodes after a move to preserve invariants
      parent.color = :BLACK
      node.color = :RED
      grandfather.color = :RED
    end
  end

  def left_rotation(node, parent, grandfather, to_recolor=false)
    grand_grandfather = grandfather.parent
    # grandfather will become the left child of parent
    update_parent(node=parent, parent_old_child=grandfather, new_parent=grand_grandfather)

    old_left = parent.left
    parent.left = grandfather
    grandfather.parent = parent
    grandfather.right = old_left
    old_left.parent = grandfather

    if to_recolor
      parent.color = :BLACK
      grandfather.color = :RED
      node.color = :RED
    end
  end

  # recolors the grandfather red, coloring his children black
  def recolor(grandfather)
    grandfather.left.color = :BLACK
    grandfather.right.color = :BLACK
    if @root != grandfather
      grandfather.color = :RED
    end

    try_rebalance grandfather
  end

  # our node 'switches' place with the old child, assigning a new parent to the node
  # if the new_parent is NIL, this means that our node becomes the root of the tree
  def update_parent(node, parent_old_child, new_parent)
    node.parent = new_parent
    if not new_parent.nil?
      # determine the old child's position to put the node there
      if new_parent.value > parent_old_child.value
        new_parent.left = node
      else
        new_parent.right = node
      end
    else
      @root = node
    end
  end

  # finds a place for the value in the binary tree, returning the node and the direction it should go in
  def find_parent(value)
    find = lambda do |node|
      if node.value == value
        return
      elsif node.value > value
        # go left
        if node.left.color == :NIL_C
          # no more to go
          return node, :LEFT
        end

        return find.call node.left
      else
        # go right
        if node.right.color == :NIL_C
          # no more to go
          return node, :RIGHT
        end
        return find.call node.right
      end
    end

    find.call @root
  end

  public :add
  private :find_parent
  # end

  def self.get_nil_leaf
    return @@nil_leaf
  end
end

# root = Node.new(value=1, color=:RED, parent=NIL, left=NIL,  right=NIL)
# left = Node.new(value=0, color=:RED, parent=root, left=RedBlackTree.get_nil_leaf, right=RedBlackTree.get_nil_leaf)
rbt = RedBlackTree.new
rbt.add 1
rbt.add 2
rbt.add 3
rbt.add 4
rbt.add 5
rbt.add 6
rbt.add 10
# root.left=left
# rbt.root = root
# p rbt.send(:find_parent, -1)
