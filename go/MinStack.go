package main

type MinStack struct {
  Stack []int
  Min int
}


/** initialize your data structure here. */
func Constructor() MinStack {
  return MinStack{make([]int, 0), int(^uint(0) >> 1)}
}


func (this *MinStack) Push(x int)  {
  if len(this.Stack) == 0 || x < this.Min {
    this.Min = x
  }
  this.Stack = append(this.Stack, x)
}


func (this *MinStack) Pop()  {
  if this.Top() == this.Min {
    this.Stack = this.Stack[:len(this.Stack) - 1]
    this.Min = int(^uint(0) >> 1)
    for _, v := range this.Stack {
      if v < this.Min {
        this.Min = v
      }
    }
  } else {
    this.Stack = this.Stack[:len(this.Stack) - 1]
  }
}


func (this *MinStack) Top() int {
  return this.Stack[len(this.Stack) - 1]
}


func (this *MinStack) GetMin() int {
  return this.Min
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
