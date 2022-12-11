# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
# (1) コンマ(,)、ピリオド(.)を置換し、文を単語に分割する
# (2) 各単語の文字数をカウントする
text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
text = text.replace('.', '').replace(',', '')
ans = [len(word) for word in text.split()]
print(ans)