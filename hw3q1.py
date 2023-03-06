# using a while loop that includes a input statement
while True:
    num_input = int(input("Enter a positive integer: "))
# placing mesures for an erros statement and exiting while loop using break 
    if num_input > 0:
        break
    print("Invalid input. Please enter a positive integer.")
#printing output
for num in range(1, num_input+1):
    print(num)
