# Testing StopIteration Exception

word_iterator = iter(["red", "green", "purple", "blue"])

try:
    while True:
        print(next(word_iterator))
except StopIteration:
    print("No more words.")