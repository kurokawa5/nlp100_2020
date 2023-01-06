# Let the sets of letter bi-grams from the words “paraparaparadise” and “paragraph” $X$ and $Y$,
# respectively. Obtain the union, intersection, difference of the two sets.
# In addition, check whether the bigram “se” is included in the sets $X$ and $Y$

def n_gram(target, n=2):
    return [target[idx:idx + n] for idx in range(len(target) - n + 1)]

text_x = 'paraparaparadise'
text_y = 'paragraph'

X = n_gram(text_x)
Y = n_gram(text_y)

#print(f'和集合: {set(X) | set(Y)}')
print(f'和集合: {set(X).union(set(Y))}')

#print(f'積集合: {set(X) & set(Y)}')
print(f'積集合: {set(X).intersection(set(Y))}')

#print(f'差集合: {set(X) - set(Y)}')
print(f'差集合: {set(X).difference(set(Y))}')

print('se' in (set(X) & set(Y)))
