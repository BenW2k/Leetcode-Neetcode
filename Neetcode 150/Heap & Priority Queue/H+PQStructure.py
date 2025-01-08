# Build Min Heap (Heapify)
# Time: O(n), Space: O(1)

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq
heapq.heapify(A)

# Heap Push (Insert element)
# Time: O(log n)

heapq.heappush(A, 4) # how you insert an element, and at which index


# Heap Pop (Extract min)
# Time: O(log n)

minn = heapq.heappop(A) # this is how you extract the first value.

# Heap Push Pop: Time: O(log n)

heapq.heappushpop(A, 99) # this is basically pushing the value 99 into the list whilst simultaneously popping the first element of A out of the list

# Peak at Min: Time O(1)
A[0]


# Heap Sort
# Time: O(n log n), Space: O(n)
# Note: O(1) Space is possible via swapping, but this is complex

def heapsort(arr): # takes in an array
  heapq.heapify(arr) # we then heapify it
  n = len(arr)
  new_list = [0] * n # make a new list which is the size the original array

  for i in range(n):
    minn = heapq.heappop(arr) # finds the minimum and adds it to the list in that order, basically sorting the list in ascending order.
    new_list[i] = minn

  return new_list

# Max Heap (heapq only really supports min heap by default, we can achieve a max heap by just negating the values)

B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)

for i in range(n):
  B[i] = -B[i]

heapq.heapify(B)
# this creates a heap where all of the values have been multiplied by negative 1, so in order to return the number as intended you would neeed to return a minus operation, like below
largest = -heapq.heappop(B)

#Insert element into max heap - this case 7

heapq.heappush(B, -7)

# Build heap from scratch - Time: O(n log n)

C = [-5, 4, 2, 1, 7, 0, 3]

heap = []

for x in C:
  heapq.heappush(heap, x)
  print(heap, len(heap)) # Check size of heap


# Putting tuples of items on the heap

D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter

counter = Counter(D)

counter

heap = []

for k, v in counter.items():
  heapq.heappush(heap, (v, k))

heap

