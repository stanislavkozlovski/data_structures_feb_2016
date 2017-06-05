# a MAX heap
class BinaryHeap
  attr_accessor :elements
  def initialize
    @elements = []
  end

  def add_element(el)
    @elements << el
    heapify_up @elements.length-1
  end

  def heapify_up(idx)
    if idx == 0
      return
    end
    el = @elements[idx]
    parent_idx = (idx - 1) / 2
    parent = @elements[parent_idx]
    if el > parent
      @elements[parent_idx], @elements[idx] = @elements[idx], @elements[parent_idx]
      heapify_up parent_idx
    end
  end

  def heapify_down(idx)
    el = @elements[idx]
    left_idx = idx * 2 + 1
    right_idx = left_idx + 1

    if right_idx < @elements.length
      if @elements[right_idx] > @elements[left_idx] && @elements[right_idx] > el
        # swap with right
        @elements[right_idx], @elements[idx] = @elements[idx], @elements[right_idx]
        heapify_down right_idx
      elsif @elements[left_idx] > el
        @elements[left_idx], @elements[idx] = @elements[idx], @elements[left_idx]
        heapify_down left_idx
      end
    else
      if left_idx < @elements.length && @elements[left_idx] > el
        # swap with left
          @elements[left_idx], @elements[idx] = @elements[idx], @elements[left_idx]
          heapify_down left_idx
      end
    end
  end

  def remove_max
    el = @elements[0]
    last_el = @elements[-1]
    if last_el == el
      @elements.pop
      return el
    end

    @elements[0] = last_el
    @elements.pop
    heapify_down 0

    return el
  end
end

bh = BinaryHeap.new
bh.add_element 2
bh.add_element 15
bh.add_element 1
bh.add_element 3
p bh.elements
p bh.remove_max
p bh.elements
p bh.remove_max
p bh.remove_max
p bh.remove_max
p bh.remove_max

