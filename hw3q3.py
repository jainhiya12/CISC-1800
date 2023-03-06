# taking input string
user_input = input("enter a string of letters: ")
# taking input character
char_input = input("enter a character to count: ")
#initialising count to 0
count = 0

# finging edge cases
if len(user_input) == 0 or char_input not in user_input:
  print ("error: user input not found")
else:
# counting string characters using .count and outputting using print
  count = user_input.count(char_input)
  print ("the number of times", char_input, "occurs in string is", count, "times")
