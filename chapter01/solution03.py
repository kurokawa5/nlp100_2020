# Split the sentence “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics”.
# into words, and create a list whose element presents the number of alphabetical letters in the corresponding word.

# (1) コンマ(,)、ピリオド(.)を置換する
# (2) 文を単語に分割する
# (3) 各単語の文字数をカウントする

original_text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
replaced_text = original_text.replace('.', '').replace(',', '')
ans = [len(word) for word in replaced_text.split()]
print(ans)