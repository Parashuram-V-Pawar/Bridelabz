# Problem Statement:
# Count the total number of vowels in a given sentence (case-insensitive).
#
# Input:
# sentence   # a string containing words, spaces, punctuation, etc.
#
# Output:
# vowel_count   # total number of vowels (a, e, i, o, u) in the sentence
#
# Function to count number of vowels in a sentence
def vowel_frequency_analyzer(sentence):
  count = 0
  # Iterating through all the characters in string and checking condition
  # If character is vowel increase count
  for ch in sentence:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u": #ch in "aeiou"
      count += 1
  # Returning count after iterating through the string
  return count

# Input statement, takes string as input
sentence = input("Enter a sentence: ")
# Prints the number of times vowels are present in string
print(vowel_frequency_analyzer(sentence.lower()))
