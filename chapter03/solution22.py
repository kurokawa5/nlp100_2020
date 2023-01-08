# Extract the category names of the article.
import pandas as pd

df = pd.read_json('chapter03/jawiki-country.json.gz', lines=True, compression='infer')
text_uk = df.query('title=="イギリス"')['text'].values[0]
splited_text_uk = text_uk.split('\n')
ans = list(filter(lambda x: '[Category:' in x, splited_text_uk))

ans = [a.replace('[[Category:', '').replace('|*', '').replace(']]', '').replace('|元','') for a in ans]
print(ans)