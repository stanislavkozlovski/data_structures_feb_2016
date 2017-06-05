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
for i in (3..1)
  puts i
end
def heap_sort(arr)
  heapify_down = lambda do |array, idx, border|
    puts "IDX is #{idx} and BORDER IS #{border}"
    while idx < border/2
      left_idx = idx*2 + 1
      right_idx = left_idx+1

      greater_idx = if right_idx < border && array[right_idx] > array[left_idx] then right_idx else left_idx end
      if array[greater_idx] > array[idx]
        array[idx], array[greater_idx] = array[greater_idx], array[idx]
        idx = greater_idx
      else
        break
      end
    end
  end
  n = arr.length
  (0..n/2).reverse_each {|i|
    heapify_down.call arr, i, arr.length
  }
    puts"AA, NO FEAR #{arr}"

  (1..n-1).reverse_each {|i|
    arr[i], arr[0] = arr[0], arr[i]
    puts "#{arr}"
    heapify_down.call arr, 0, i
    puts "#{arr}"
  }

  puts "should be sorted #{arr}"
end


puts heap_sort [5, 139, 3, -1, 41341, 1, 4]
# puts heap_sort [1,2,3, 4]