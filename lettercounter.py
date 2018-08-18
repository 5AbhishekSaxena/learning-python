from collections import Counter

word = "Hello"
counts = Counter(word)  # Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
for i in sorted(set(word)):
    print(i, counts[i])