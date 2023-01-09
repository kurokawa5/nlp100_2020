# Extract section names in the article with their levels.
# For example, the level of the section is 1 for the MediaWiki markup "== Section name ==".
import re
import pandas as pd

df = pd.read_json('chapter03/jawiki-country.json.gz', lines=True, compression='infer')
text_uk = df.query('title=="イギリス"')['text'].values[0]

section_pattern = r'(={2,})(.+?)={2,}'
sections = re.findall(section_pattern, text_uk)

for section in sections:
    level = len(section[0])-1
    name = section[1].strip()
    print(f'セクション名: {name}, レベル: {level}')