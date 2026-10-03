"""
Participation Activity 4: StopIteration Exception
Sarah Estes
To cause and handle a StopIteration exception.
10/2/26
"""

word_iterator = iter(["red", "green", "purple", "blue"])

try:
    while True:
        print(next(word_iterator))
except StopIteration:
    print("No more words.")
