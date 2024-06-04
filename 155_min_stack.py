"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:

    -2^31 <= val <= 2^31 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""


class MinStack:

    def __init__(self):
        self.items = []
        self.mins = []
        self.min = None

    def push(self, val: int) -> None:
        self.items.append(val)
        if self.min is None or val < self.min:
            self.min = val
        self.mins.append(self.min)

    def pop(self) -> None:
        _ = self.items.pop()
        _ = self.mins.pop()
        if len(self.mins) == 0:
            self.min = None
        else:
            self.min = self.mins[len(self.mins)-1]

    def top(self) -> int:
        return self.items[len(self.items)-1]

    def getMin(self) -> int:
        return self.mins[len(self.mins)-1]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    output = stack.getMin()
    assert output == -3
    stack.pop()
    output = stack.top()
    assert output == 0
    output = stack.getMin()
    assert output == -2

    stack = MinStack()
    stack.push(0)
    stack.push(1)
    stack.push(0)
    output = stack.getMin()
    assert output == 0
    stack.pop()
    output = stack.getMin()
    assert output == 0

    stack = MinStack()
    stack.push(2147483646)
    stack.push(2147483646)
    stack.push(2147483647)
    output = stack.top()
    assert output == 2147483647
    stack.pop()
    output = stack.getMin()
    assert output == 2147483646
    stack.pop()
    output = stack.getMin()
    assert output == 2147483646
    stack.pop()
    stack.push(2147483647)
    output = stack.top()
    assert output == 2147483647
    output = stack.getMin()
    assert output == 2147483647
    stack.push(-2147483648)
    output = stack.top()
    assert output == -2147483648
    output = stack.getMin()
    assert output == -2147483648
    stack.pop()
    output = stack.getMin()
    assert output == 2147483647

    stack = MinStack()
    stack.push(-10)
    stack.push(14)
    output = stack.getMin()
    assert output == -10
    output = stack.getMin()
    assert output == -10
    stack.push(-20)
    output = stack.getMin()
    assert output == -20
    output = stack.getMin()
    assert output == -20
    output = stack.top()
    assert output == -20
    output = stack.getMin()
    assert output == -20
    stack.pop()
    stack.push(10)
    stack.push(-7)
    output = stack.getMin()
    assert output == -10
    stack.push(-7)
    stack.pop()
    output = stack.top()
    assert output == -7
    output = stack.getMin()
    assert output == -10
    stack.pop()
