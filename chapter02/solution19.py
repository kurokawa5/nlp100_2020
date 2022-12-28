# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

import pandas as pd

df = pd.read_csv('chapter02/popular-names.txt', sep='\t', header=None)
print(df.iloc[:,0].value_counts())
#print(df[0].value_counts())

