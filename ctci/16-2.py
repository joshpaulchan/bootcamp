# 16.2 Word Frequencies - Design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times?

# def find_frequencies(book: list[str], word: str):
#   frequencies = {}
#   for word in book:
#     if not word in frequencies:
#       frequencies[word] = 0

#     frequencies[word] += 1
  
#   return frequencies[word]

# def build_indexes(book):
#   frequencies = {}
#   for word in book:
#     if not word in frequencies:
#       frequencies[word] = 0

#     frequencies[word] += 1
#   return frequencies

# def query_word_frequency(index, word):
#   return index.get(word, 0)

# def main():
#   frequencies = build_indexes(book)

#   for word in ["cat", "bat", "etc"]:
#     query_word_frequency(frequencies, word)