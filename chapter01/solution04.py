# “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. 
# Arthur King Can.”という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

def extract_chars(i, word):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        return (i, word[0])
    else:
        return (i, word[:2])

ans = {}
text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
text = text.replace('.', '').replace(',', '')
ans = [extract_chars(i, w) for i, w in enumerate(text.split(), 1)]
print(ans)
