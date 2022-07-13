# Backtracking is an algorithmic-technique for solving problems recursively by
# trying to build a solution incrementally, one piece at a time, removing those
# solutions that fail to satisfy the constraints of the problem at any point of
# time
import time

# find k intigers that sum to target.
class simpleBackTrack:
    def __init__(self):
        self.ans = []
        self.operation_count = 0

    def solve(self, k, target, pos, vals):
        self.operation_count += 1
        if pos == k:
            if sum(vals) == target:
                self.ans.append(vals[:])
            else:
                return
        for i in range(vals[-1]+1 if vals else 1, 10):
            vals.append(i)
            self.solve(k, target, pos+1, vals)
            vals.pop()

    def sumK(self, k, target):
        vals = []
        self.solve(k, target, 0, vals)
        print(self.operation_count)
        return self.ans

def simpleBackTrack_test():
    timer = time.process_time_ns()
    test = simpleBackTrack()
    print(test.sumK(8, 30))
    print(f"Execution time: {(time.process_time_ns()-timer)/1e9}")

class fourSum:
    def __init__(self):
        self.ans = []
        self.operation_count = 0

    def solve(self, nums, target, pos, vals):
        self.operation_count += 1
        if vals and nums[vals[-1]] > 0:
            if sum([nums[i] for i in vals]) > target:
                return
        if pos == 4:
            if sum([nums[i] for i in vals]) == target:
                hold = [nums[i] for i in vals]
                if not self.ans:
                    self.ans.append(hold)
                if self.ans and hold != self.ans[-1]:
                    self.ans.append(hold)
            else:
                return
        if pos < 4:
            for i in range(vals[-1]+1 if vals else 0, len(nums)):
                vals.append(i)
                self.solve(nums, target, pos+1, vals)
                vals.pop()

    def sum(self, nums, target):
        vals = []
        nums.sort()
        self.solve(nums, target, 0, vals)
        print('Operational Count: ', self.operation_count)
        return self.ans

def fourSum_test():
    timer = time.process_time_ns()
    test = fourSum()
    print(test.sum([-495,-477,-464,-424,-411,-409,-363,-337,-328,-328,-325,-320,-310,-285,-278,-235,-208,-151,-149,-147,-144,-132,-115,-107,-101,-98,-83,-58,-58,-56,-51,-46,-45,-7,0,4,4,21,51,52,57,60,104,109,124,141,158,205,206,241,278,278,291,314,379,416,437,447,452,496], -1371))
    print(f'Execution time: {(time.process_time_ns()-timer)/1e9}')

if __name__ == '__main__':
    # simpleBackTrack_test()
    fourSum_test()
