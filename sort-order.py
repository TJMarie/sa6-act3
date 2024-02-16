words = ["order", "cat", "bat", "laptop", "bask", "bait", "movie"]

print(sorted(words, key=lambda x: (len(x), x)))