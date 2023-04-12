#defining a function that takes the two lists as arguments
def common_elements(list1, list2):
#attaching list arguments to the set data type
    set1 = set(list1)
    set2 = set(list2)
 #manimuplating the set data type using the .intersection function   
    common_numbers = set1.intersection(set2)
    return common_numbers


#test case:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = common_elements(list1, list2)
print(result)
