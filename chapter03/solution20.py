# Read the JSON documents and output the body of the article about the United Kingdom.
# Reuse the output in problems 21-29.

import pandas as pd

df = pd.read_json('chapter03/jawiki-country.json.gz', lines=True, compression='infer')
text_uk = df.query('title=="イギリス"')['text'].values[0]
print(text_uk)