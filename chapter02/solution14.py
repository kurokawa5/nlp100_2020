# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

import sys
import fire
import pandas as pd


if len(sys.argv) == 1:
    print('Set arg n, like "python chapter02/solution14.py 5"')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('chapter02/popular-names.txt', sep='\t', header=None)
    print(df.head(n))