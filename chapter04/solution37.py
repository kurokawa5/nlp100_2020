# Visualize the top-ten frequent words and their frequencies with a chart (e.g., bar chart).
import itertools
from collections import Counter
from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib

def parse_mecab(block):
    res = []
    for line in block.split('\n'):
        if line == '':
            return res
        (surface, attr) = line.split('\t')
        attr = attr.split(',')
        lineDict = {
            'surface': surface,
            'base': attr[6],
            'pos': attr[0],
            'pos1': attr[1]
        }
        res.append(lineDict)

filename = 'chapter04/neko.txt.mecab'
with open(filename, mode='rt', encoding='utf-8') as f:
    blocks = f.read().split('EOS\n')

filtered_blocks = list(filter(lambda x: x != '', blocks))
parse_blocks = [parse_mecab(block) for block in filtered_blocks]

neko_cooc = Counter([])

for sentence in parse_blocks:
    words = [word["base"] for word in sentence]

    if "猫" in words:
        neko_cooc += Counter(words)

neko_cooc = dict(neko_cooc.most_common()[:11])
neko_cooc.pop("猫")
print(neko_cooc)

plt.figure()
plt.bar(neko_cooc.keys(), neko_cooc.values())
plt.show()