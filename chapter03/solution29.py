# Obtain the URL of the country flag by using the analysis result of Infobox.
# (Hint: convert a file reference to a URL by calling imageinfo in MediaWiki API)
import pandas as pd
import re
import requests

df_j = pd.read_json('chapter03/jawiki-country.json.gz', lines=True, compression='infer')
text_uk = df_j.query('title=="イギリス"')['text'].values[0]

template_text = re.findall(r'\{\{基礎情報 (.+?^}\})', text_uk, re.MULTILINE+re.DOTALL)[0]

template_text = re.sub("'{2,5}","", template_text)
template_text = re.sub("\[\[(?:.[^|]+?\|)??(([^|]+?)|(\{\{.+?\}\}))\]\]", r"\1", template_text)

template_text = re.sub("\[\[ファイル:(.+?)(?:\|.+)*\]\]", r"\1", template_text)
template_text = re.sub("\{\{lang\|.+?\|(.+?)\}\}", r"\1", template_text)
template_text = re.sub("\{\{仮リンク\|(.+?)\|.+?\}\}", r"\1", template_text)
template_text = re.sub("\{\{.+?}\}","", template_text)
template_text = re.sub("<.+?>","", template_text)
template_text = re.sub("\[.+?]","", template_text)

template = dict(re.findall("\|(.+?) *= *(.+?)\n(?=\||})", template_text, re.MULTILINE+re.DOTALL))

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"
path = template["国旗画像"].replace(" ","_")

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop": "url",
    "titles": "File:"+path
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v["imageinfo"][0]["url"])