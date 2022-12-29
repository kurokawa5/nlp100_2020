# 記事中でカテゴリ名を宣言している行を抽出せよ．
import re
import pandas as pd

df_j = pd.read_json('chapter03/jawiki-country.json.gz', lines=True, compression='infer')
uk_text = df_j.query('title=="イギリス"')['text'].values[0]
for section in re.findall(r'(=+)([^=]+)\1\n', uk_text):
    print(f'{section[1].strip()}\t{len(section[0]) - 1}')