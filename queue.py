# Queues are abstract data structures similar to stacks.  The hold temporary data.
# when data consumed it is gone.
# new data goes at end of queue
# oldest data comes out the
# only oldest data (front of queue) can be read.

# leetCode 232 Impliment queue using stacks
class MyQueue:

    def __init__(self):
        self.__queue = []

    def push(self, x: int) -> None:
        self.__queue.append(x)

    def pop(self) -> int:
        if not self.__queue:
            return None
        stack = [self.__queue.pop() for i in range(len(self.__queue)-1)]
        rsp = self.__queue.pop()
        while stack:
            self.__queue.append(stack.pop())
        return rsp

    def peek(self) -> int:
        if not self.__queue:
            return None
        stack = [self.__queue.pop() for i in range(len(self.__queue)-1)]
        rsp = self.__queue.pop()
        stack.append(rsp)
        while stack:
            self.__queue.append(stack.pop())
        return rsp

    def empty(self) -> bool:
        if self.__queue:
            return False
        return True

if __name__ == '__main__':
    q = MyQueue()
    q.push(4)
    q.push(3)
    q.push(9)
    print(q.peek())
    q.pop()
    print(q.peek())
    q.empty()
    print(q.peek())
