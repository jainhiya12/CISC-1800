# Hiya Jain
# Lab 09: Bubble Sort
# CISC 1800 - Introduction to Computer Programming

def bubble_sort (arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

# test case 
arr = [2, 5,7,1,3,4,6]
bubble_sort(arr)
print(arr)
