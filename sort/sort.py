# Studying of sorting methods.

import random
import time

#helper funciton for qucksort and quickselect.
def partition(arr, left_pointer, right_pointer):
    if len(arr) <= 1:
        return arr
    pivot = right_pointer
    right_pointer -= 1

    while True:
        while arr[left_pointer] < arr[pivot]:
            left_pointer += 1
        while arr[right_pointer] > arr[pivot]:
            right_pointer -= 1
        if left_pointer > right_pointer:
            break
        else:
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
        left_pointer += 1
    arr[pivot], arr[left_pointer] = arr[left_pointer], arr[pivot]

    return left_pointer

# selection sort
# O(n^2)
# Start at beginning of lst, read through entire lst, remember lowest value,
# swap with address, move to next address and repeat the process until you are
# at the end of the list
def selection_sort(lst):
    lowest = 0
    for i in range(len(lst)):
        lowest = lst[i]
        lowest_i = i
        for j in range(len(lst)-i):
            if lst[j+i] < lowest:
                lowest = lst[j]
                lowest_i = j+i
        lst[i], lst[lowest_i] = lst[lowest_i], lst[i]
    return lst

# Start at begging of list, compare each value to next if vale +1 smaller then swap
# do this list length number of times. O(n^2)
def bubble_sort(lst):
    range__ = len(lst)
    sorted = False
    for i in range(range__):
        sorted = True
        for j in range(range__-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                sorted = False
        if sorted:
            break
    return lst

# Start at index 1 compare to vale to its left, if value(index) < left value then
# swap else break and check index 2 and so on, do until you are at end of list
# O(n^2) but will be faster since breaks loop when min found so only if list is in
# worst case order will selection sort be faster, otherwise insertion sort is faster.
def insertion_sort(lst):
    range__ = len(lst)

    for i in range(1, range__):
        val = lst[i]
        idx = i - 1
        while idx >= 0:
            if lst[idx] > val:
                lst[idx+1] = lst[idx]
                idx -= 1
            else:
                break
        lst[idx+1] = val

    return lst

# python lists have a built in method
# modifies list in place
def native_sort(lst):
    lst.sort()
    return lst

# python also has built in function, builds new sorted list from iterable
def native_dict_sort(dct):
    mykey = lambda item: item[1]
    return sorted(dct.items(), key=mykey)

# recursivly break the list into its individual components the put back together
# in order. O(nlong(n))
# reference https://www.geeksforgeeks.org/merge-sort/
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        L = lst[:mid]
        R = lst[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i+=1
            else:
                lst[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            lst[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            lst[k] = R[j]
            j+=1
            k+=1
    return lst

def quick_sort(lst, left_index, right_index):
    if right_index - left_index <= 0:
        return
    pivot = partition(lst, left_index, right_index)
    quick_sort(lst, left_index, pivot-1)
    quick_sort(lst, pivot+1, right_index)

range__ = 100000
samples = 10000

mydct = {"a": 4, "z": 2, "b":3}
print(native_dict_sort(mydct))

mylst = random.sample(range(range__), k=samples)
print(len(mylst))
timer = time.process_time_ns()
native_sort(mylst)
print(f"native timer: {(time.process_time_ns()-timer)/1e9}")

mylst = random.sample(range(range__), k=samples)
print(len(mylst))
timer = time.process_time_ns()
bubble_sort(mylst)
print(f"bubble timer: {(time.process_time_ns()-timer)/1e9}")

mylst = random.sample(range(range__), k=samples)
print(len(mylst))
timer = time.process_time_ns()
selection_sort(mylst)
print(f"selection timer: {(time.process_time_ns()-timer)/1e9}")

mylst = random.sample(range(range__), k=samples)
print(len(mylst))
timer = time.process_time_ns()
insertion_sort(mylst)
print(f"insertion timer: {(time.process_time_ns()-timer)/1e9}")

mylst = random.sample(range(range__), k=samples)
print(len(mylst))
timer = time.process_time_ns()
merge_sort(mylst)
print(f"merge timer: {(time.process_time_ns()-timer)/1e9}")

mylst = random.sample(range(range__), k=samples)
print(len(mylst))
timer = time.process_time_ns()
index = len(mylst)-1
quick_sort(mylst, 0, index)
print(f"quicksort timer: {(time.process_time_ns()-timer)/1e9}")
