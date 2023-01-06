# Split the sentence “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can”.
# into words, and extract the first letter from the 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words and the first two letters from the other words.
# Create an associative array (dictionary object or mapping object) that maps from the extracted string to the position (offset in the sentence) of the corresponding word.

# (1) コンマ(,)、ピリオド(.)を置換する
# (2) 文を単語に分割する
# (3) 単語の順番情報を取得し、順番にあわせて処理をする

def extract_chars(index, word):
    # 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字を取り出す
    if index in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        return (index, word[0])
    # それ以外の単語は先頭の2文字を取り出す
    else:
        return (index, word[:2])

original_text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
replaced_text = original_text.replace('.', '').replace(',', '')
ans = [extract_chars(index, word) for index, word in enumerate(replaced_text.split(), start = 1)]
print(dict(ans))