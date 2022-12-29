# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import pandas as pd
import re

df_j = pd.read_json('chapter03/jawiki-country.json.gz', lines=True, compression='infer')
uk_text = df_j.query('title=="イギリス"')['text'].values[0]
uk_texts = uk_text.split('\n')

pattern = re.compile(r'\|(.+?)\s=\s*(.+)')
ans = {}
for line in uk_texts:
    r = re.search(pattern, line)
    if r:
        ans[r[1]] = r[2]
        #print(r[2])
        #print(ans[r[1]])
print(ans)
