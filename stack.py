
# A stack is a linear data structur with last in first out (LIFO) storage.
# In python stacks can be lists, colletion.deque, queue.LifoQueue, lists run
# into performance issues due to lists allocating in continuous memory blocks.
# stack only uses empty, size, top, push(ie append for list), pop.

# Stacks are efficient.
# Once data is consumes from stack, it is off the stack
# Stacks are good for reversing data.

# Reference
# https://www.geeksforgeeks.org/stack-in-python/

from collections import deque

# List stack
def basic_stack():
    print('Basic Stack from list')
    myStack = []
    myStack.append(1)
    myStack.append(2)
    print(myStack)
    myStack.pop()
    print(myStack)
    print(len(myStack))

def stack_reverse():
    print('Reverse Stack')
    myStack = [1,2,3,4,5]
    print(myStack)
    new = []
    for i in range(5):
        new.append(myStack.pop())
        print(f"myStack: {myStack} new: {new}")

#swap two valuees in a stack, O(n)
def swap(stack, ai, bi): # swap a and b, a and b are values. ai, bi index
    hold = []
    range__ = len(stack)
    a = 0
    b = 0
    # get a and b values
    for i in range(range__):
        item = stack.pop()
        if i == range__-1-ai:
            a = item
        if i == range__-1-bi:
            b = item
        hold.append(item)

    for i in range(range__):
        if i == bi:
            stack.append(a)
            hold.pop()
        elif i == ai:
            stack.append(b)
            hold.pop()
        else:
            stack.append(hold.pop())
    return stack

# Get value by the index of the stack, O(n)
def get_value_by_index(stack, idx):
    range__ = len(stack)
    value = 0
    hold = []
    for i in range(range__):
        item = stack.pop()
        if i == range__-1-idx:
            value = item
        hold.append(item)

    for i in range(range__): # reverse back stack
        stack.append(hold.pop())
    return value

# copy one stack to another
def copy(stack1, stack2):
    hold = []
    range2__ = len(stack2)
    range1__ = len(stack1)
    for i in range(range1__):
        stack1.pop()
    for i in range(range2__):
        stack1.append(stack2.pop())

# Selection Sort
# at the end of the stack. O(n^2) but due to stack indexing O(n^3)
def stack_selection_sort(stack):
    lowest = 0;
    range__ = len(stack)
    for i in range(range__):
        lowest = get_value_by_index(stack, i)
        lowest_i = i
        for j in range(range__-i):
            if get_value_by_index(stack, j+i) < lowest:
                lowest = get_value_by_index(stack, j+i)
                lowest_i = j+i
        swap(stack, lowest_i, i)
    return stack

# collections deque
#thread safe, memory efficient, pop O(1) efficency
def basic_collections_stack():
    myStack = deque(range(10))
    myStack.append(99)
    print(f'myStack: {myStack}')
    myStack.pop()
    print(f'myStack: {myStack}')
    myStack.popleft()
    print(f'myStack: {myStack}')


# leetcode 155 min stack
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return min(self.stack)

# leetcode 496
# validate stack sequences
class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        pops = 0
        for i in pushed:
            stack.append(i)
            for  j in popped[pops:]:
                if stack and j == stack[-1]:
                    stack.pop()
                    pops += 1
                else:
                    break
        return len(stack) == 0

# Data structures and algorithms 148, q4
def reverse(stack):
    rsp = [stack.pop() for i in range(len(stack))]
    return rsp


print(reverse([1,2,3,4]))
