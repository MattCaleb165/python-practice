import re

word = input("Provide a word and I'll check if it's a palidrome: ")

word_check = re.sub('[^A-Za-z0-9]+', '', word).lower()

if word_check[::-1] == word_check:
  print(f"{word} is a palidrome.")
else:
  print(f"{word} is not a palindrome.")