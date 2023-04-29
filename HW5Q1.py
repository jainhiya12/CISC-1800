#define a function with paramater arr being a list of integers
def max_subarray_sum(arr):
#check if input array is empty, if so return 0
  if len(arr) == 0:
    return 0
#initialise two variables to the first element of the array
  max_sum = current_sum = arr[0]
#loops through the rest of the elements in the array starting from the second one
  for num in arr[1:]:
#update current sum by comparing num and the previous current_sum to find the larger of the two
    current_sum = max(num, current_sum + num)
#then compare current_sum to the presnt max_sum and update it as needed
    max_sum = max(max_sum, current_sum)
#max_sum stores the value of the largest contigous subarray 
  return max_sum

# Test case
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])) 
