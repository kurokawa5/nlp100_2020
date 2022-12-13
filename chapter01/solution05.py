# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
def n_gram(target, n):
    return [target[idx:idx + n] for idx in range(len(target) - n + 1)]

text = 'I am an NLPer'
for i in range(1, 4):
    print(n_gram(text, i))#文字
    print(n_gram(text.split(' '), i))#単語
