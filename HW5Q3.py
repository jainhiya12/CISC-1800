# define a function that takes two lists of integers as parameters (lst1, lst2))
def merge_sorted_lists(lst1, lst2):
#initialise an empty list results to store the merge sorted lists
  result = []
#two index variables that each track the the positions of hte two respective lists
  i = j = 0
#while loop that iterates through the lists as long as they as variables are within the bounds of hte lists
  while i < len(lst1) and j < len(lst2):
#compare current elements of the two lists and append them as needed during the comparision
    if lst1[i] < lst2[j]:
      result.append(lst1[i])
      i += 1
    else:
      result.append(lst2[j])
      j += 1
#using the extend method to append the remaining elements to the results list
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result

# Test cases
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
print(merge_sorted_lists(list1, list2))  
