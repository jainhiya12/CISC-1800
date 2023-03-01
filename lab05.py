# Hiya Jain
# Lab 05: Iterative Binary Search
# CISC 1800 - Introduction to Computer Programming


def binarySearch(arr, l, r, x):
  while l <= r:
    mid = (l + r) // 2
    if arr[mid] == x:
      return mid
    elif arr[mid] < x:
      l = mid + 1
    elif arr[mid] > x:
      r = mid - 1

  return -1

#test case/input
list_one = [10, 20, 30, 40, 50]
target = 20
print(binarySearch(list_one, 0, len(list_one)-1, target))
