# 記事中でカテゴリ名を宣言している行を抽出せよ．

import pandas as pd

df_j = pd.read_json('chapter03/jawiki-country.json.gz', lines=True, compression='infer')
uk_text = df_j.query('title=="イギリス"')['text'].values[0]
uk_texts = uk_text.split('\n')
ans = list(filter(lambda x: '[Category:' in x, uk_texts))
ans = [a.replace('[[Category:', '').replace('|*', '').replace(']]', '').replace('|元','') for a in ans]
print(ans)