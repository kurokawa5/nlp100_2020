# 記事から参照されているメディアファイルをすべて抜き出せ．

import pandas as pd
import re

df_j = pd.read_json('chapter03/jawiki-country.json.gz', lines=True, compression='infer')
uk_text = df_j.query('title=="イギリス"')['text'].values[0]

for file in re.findall(r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]', uk_text):
    print(file[1])

#for m in re.finditer(r'\[\[(?:File|ファイル):([^\[\]|]+)(?:\|[^\[\]]+)?(.*)\]\]', uk_text):
