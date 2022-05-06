# An array based heap, or priority queue is used for queueing up values such
# that highest value is at front of queue regardless of how values are inserted
# into the queue.  Example - emergency room visitors arive at random times but
# seen based on injury severity.

# log(N) for delete and insert.
import random

class heap:
    def __init__(self):
        self.data = []

    def insert(self, val):
        # insert at end
        self.data.append(val)
        # trickle up the structure
        val_i = len(self.data)-1
        while val > self.data[self.parent(val_i)] and val_i > 0:
            self.data[self.parent(val_i)], self.data[val_i] = (
            self.data[val_i], self.data[self.parent(val_i)])
            val_i = self.parent(val_i)

        return

    def delete(self):
        # set first value to last value
        self.data[0] = self.data[-1]
        # delete last value
        self.data.pop()
        #trickle top value down to get high value in top positon
        val_i = 0
        while self.has_larger_child(val_i):
            self.data[self.larger_child_idx(val_i)], self.data[val_i] = (
            self.data[val_i], self.data[self.larger_child_idx(val_i)] )

    # determins if one the the nodes children are larger
    def has_larger_child(self, idx):
        left_larger = self.data[idx] < self.data[self.left_child(idx)]
        right_larger = self.data[idx] < self.data[self.right_child(idx)]
        return left_larger or right_larger

    def larger_child_idx(self, idx):
        left_idx = self.left_child(idx)
        right_idx = self.right_child(idx)
        left_val = self.data[left_idx]
        right_val = self.data[right_idx]
        return left_idx if left_val > right_val else right_val

    def root(self):
        return self.data[0]

    def last(self):
        return self.data[-1]

    def left_child(self, idx):
        return idx*2 + 1

    def right_child(self, idx):
        return idx*2 + 2

    def parent(self, idx):
        return (idx-1)//2

if __name__ == "__main__":
    min_rand = 0
    max_rand = 1000
    # reate list of input values for testing
    vals = random.sample(range(max_rand), 10)
    # initialize  heap
    queue = heap()
    # insert vals to heap
    for i in vals:
        queue.insert(random.randint(min_rand, max_rand))
    print(queue.data)

    queue.delete()

    print(queue.data)
