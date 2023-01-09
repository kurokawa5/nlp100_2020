# Extract field names and their values in the Infobox “country”, and store them in a dictionary object.
import pandas as pd
import re

df_j = pd.read_json('chapter03/jawiki-country.json.gz', lines=True, compression='infer')
text_uk = df_j.query('title=="イギリス"')['text'].values[0]

template_text = re.findall(r'\{\{基礎情報 (.+?^}\})', text_uk, re.MULTILINE+re.DOTALL)[0]
template = dict(re.findall("\|(.+?) *= *(.+?)\n(?=\||})", template_text, re.MULTILINE+re.DOTALL))

for t in template:
    print(t, template[t])