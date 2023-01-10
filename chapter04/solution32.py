# Extract lemmas of all verbs appearing in the text.
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

def extract_base(block):
    res = list(filter(lambda x: x['pos'] == '動詞', block))
    res = [r['base'] for r in res]
    return res

filename = 'chapter04/neko.txt.mecab'
with open(filename, mode='rt', encoding='utf-8') as f:
    blocks = f.read().split('EOS\n')

filtered_blocks = list(filter(lambda x: x != '', blocks))
parse_blocks = [parse_mecab(block) for block in filtered_blocks]
parse_blocks = [extract_base(block) for block in parse_blocks]
print(parse_blocks[5])