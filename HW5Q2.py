# define a function with parameter (lst) for list of integers
def is_sorted(lst):
# loops through the list starting from first element to the second to last element (last will be automatically compared)
  for i in range(len(lst) - 1):
# check if current element is greater than the next element which means that it is not sorted   
    if lst[i] > lst[i + 1]:
      return False
  return True

# Test cases
print(is_sorted([1, 2, 3, 4, 5]))  # Expected output: True
print(is_sorted([1, 3, 2, 4, 5]))  # Expected output: False
