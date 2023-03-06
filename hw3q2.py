# taking input
user_input = input("Enter a list of integers separated by commas: ")
# seprating input using split
num_list = user_input.split(",")
#initialising list to 0
total = 0

# looping through the list
for num in num_list:
# picking out error messages
    while not num.isdigit():
        print("Invalid input")
        user_input = input("Enter a list of integers separated by commas: ")
        num_list = user_input.split(",")
        num = num_list[0]
#summing the numbers
    total += int(num)

# printing the output
print("The sum of all the integers in the list is:", total)
