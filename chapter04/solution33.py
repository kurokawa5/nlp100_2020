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
    res = []
    for i, word in enumerate(block):
        if word["surface"] == "の":

            if (i==0) or (i==len(block)-1):
                continue

            if (block[i-1]['pos'] == '名詞') & (block[i+1]['pos'] == '名詞'):
                phrase = block[i-1]['surface'] + "の" + block[i+1]['surface']
                res.append(phrase)
    return res

filename = 'chapter04/neko.txt.mecab'
with open(filename, mode='rt', encoding='utf-8') as f:
    blocks = f.read().split('EOS\n')

filtered_blocks = list(filter(lambda x: x != '', blocks))
parse_blocks = [parse_mecab(block) for block in filtered_blocks]
parse_blocks = [extract_base(block) for block in parse_blocks]
print(parse_blocks[11:13])