# Implement a function that obtains n-grams from a given sequence object (e.g., string and list).
# Use this function to obtain word bi-grams and letter bi-grams from the sentence “I am an NLPer”

def n_gram(target, n):
    return [target[idx:idx + n] for idx in range(len(target) - n + 1)]

text = 'I am an NLPer'
for i in range(1, 4):
    print(n_gram(text, i))#空白を含めた文字
    print(n_gram(text.split(' '), i))#単語
