#defining a new function with one argument called words
def group_words_by_first_letter (words):
#creating an empty dictionary
  word_dictionary = {}
#looping through each word in the list
  for word in words:
  #getting the first letter by using 0 to index for it
      first_letter = word[0]
      if first_letter not in word_dictionary:
#in this case we are creating a new key that can store the values of words staring with that letter
        word_dictionary[first_letter] = []
      word_dictionary[first_letter].append(word)
  #returning results/output
  return(word_dictionary)

#testcase:
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grapefruit", "honeydew"]
result = group_words_by_first_letter(words)
print(result)
