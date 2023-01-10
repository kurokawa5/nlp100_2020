# In addition to the process of the problem 26, remove internal links from the values.
# See Help:Cheatsheet. https://en.wikipedia.org/wiki/Help:Cheatsheet
import pandas as pd
import re

df_j = pd.read_json('chapter03/jawiki-country.json.gz', lines=True, compression='infer')
text_uk = df_j.query('title=="イギリス"')['text'].values[0]

template_text = re.findall(r'\{\{基礎情報 (.+?^}\})', text_uk, re.MULTILINE+re.DOTALL)[0]

template_text = re.sub("'{2,5}","", template_text)
template_text = re.sub("\[\[(?:.[^|]+?\|)??(([^|]+?)|(\{\{.+?\}\}))\]\]", r"\1", template_text)

template = dict(re.findall("\|(.+?) *= *(.+?)\n(?=\||})", template_text, re.MULTILINE+re.DOTALL))

for t in template:
    print(t, template[t])