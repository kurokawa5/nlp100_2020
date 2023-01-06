"""
Write a program with the specification:
 - Receive a word sequence separated by space
 - For each word in the sequence:
    - If the word is no longer than four letters, keep the word unchanged
    - Otherwise,
        - Keep the first and last letters unchanged
        - Shuffle other letters in other positions (in the middle of the word)

Observe the result by giving a sentence, e.g., “I couldn’t believe that
I could actually understand what I was reading : the phenomenal power of the human mind “.
"""
import random

def typoglycemia(word):
    if len(word) <= 4:
        return word
    else:
        start = word[0]
        end = word[-1]
        others = random.sample(list(word[1:-1]), len(word[1:-1]))
        return ''.join([start] + others + [end])

text = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
ans = [typoglycemia(word) for word in text.split()]
print(' '.join(ans))