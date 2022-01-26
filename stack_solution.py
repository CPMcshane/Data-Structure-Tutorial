"""
Stack example solution.
"""

word_stack = []

def get_word():
    print(word_stack.pop())

def add_word():
    word = input("Type word: ")
    word_stack.append(word)

add_word()
add_word()
add_word()
get_word()
print(word_stack)
get_word()
print(word_stack)
get_word()
print(word_stack)
