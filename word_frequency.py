from collections import defaultdict

phrase = input("Give me a phrase to count: ")
counting = defaultdict(int)

word_count = phrase.split()

for word in word_count:
    counting[word] += 1

for word, count in counting.items():
  print(word + " " + str(count))
