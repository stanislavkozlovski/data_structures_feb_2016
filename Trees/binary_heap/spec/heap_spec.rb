require 'spec_helper'
require_relative '../binary_heap'
describe 'tank' do

  it 'Output max' do
    # populate heap
    bh = BinaryHeap.new
    nums = [51, 1341, 1, 2, -1, 5154, 13, 33, 3]
    nums.map {|a| bh.add_element a}

    sorted_nums = nums.sort.reverse
    sorted_nums.each {|num|
      max = bh.remove_max
      puts max
      puts num
      num.should == max
    }
  end
end