# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

import pandas as pd

df_j = pd.read_json('chapter03/jawiki-country.json.gz', lines=True, compression='infer')
uk_text = df_j.query('title=="イギリス"')['text'].values
#uk_text = df_j.query('title=="イギリス"')['text'].values[0]
print(uk_text)