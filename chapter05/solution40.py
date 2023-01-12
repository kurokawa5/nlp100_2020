# Design a class Word that represents a word. This class has three member variables,
# text (word surface), lemma (lemma), and pos (part-of-speech). Represent a sentence as
# an array of instances of Word class. Implement a program to load the parse result,
# and store the text as an array of sentences. Show the object of the first sentence of
# the body of the article.
class Morph:
    def __init__(self, dc):
        self.surface = dc['surface']
        self.base = dc['base']
        self.pos = dc['pos']
        self.pos1 = dc['pos1']

def parse_cabocha(block):
    res = []
    for line in block.split('\n'):
        if line == '':
            return res
        elif line[0] == '*':
            continue
        (surface, attr) = line.split('\t')
        attr = attr.split(',')
        lineDict = {
            'surface': surface,
            'base': attr[6],
            'pos': attr[0],
            'pos1': attr[1]
        }
        res.append(Morph(lineDict))

filename = 'chapter05/ai.ja.txt.parsed'
with open(filename, mode='rt', encoding='utf-8') as f:
    blocks = f.read().split('EOS\n')
blocks = list(filter(lambda x: x != '', blocks))
blocks = [parse_cabocha(block) for block in blocks]
for m in blocks[1]:
    print(vars(m))