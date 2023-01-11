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

flat = list(itertools.chain.from_iterable(parse_blocks))
flat = [f["base"] for f in flat if f["pos"]!="記号"]

words = Counter(flat)
word_freq = words.most_common()
word_freq = dict(word_freq[:10])
plt.figure()
plt.bar(word_freq.keys(), word_freq.values())
plt.show()