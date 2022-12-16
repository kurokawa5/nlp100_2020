# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

def n_gram(target, n=2):
    return [target[idx:idx + n] for idx in range(len(target) - n + 1)]

text1 = 'paraparaparadise'
text2 = 'paragraph'

X = n_gram(text1)
Y = n_gram(text2)

#print(f'和集合: {set(X) | set(Y)}')
print(f'和集合: {set(X).union(set(Y))}')

#print(f'積集合: {set(X) & set(Y)}')
print(f'積集合: {set(X).intersection(set(Y))}')

#print(f'差集合: {set(X) - set(Y)}')
print(f'差集合: {set(X).difference(set(Y))}')

print('se' in (set(X) & set(Y)))
