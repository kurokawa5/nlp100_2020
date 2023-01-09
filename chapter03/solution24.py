# Extract references to media files linked from the article.
import pandas as pd
import re

df_j = pd.read_json('chapter03/jawiki-country.json.gz', lines=True, compression='infer')
text_uk = df_j.query('title=="イギリス"')['text'].values[0]

media = re.findall(r'\[\[ファイル:(.+?)(?:\|.+)*\]\]', text_uk)
for file in media:
    print(file)