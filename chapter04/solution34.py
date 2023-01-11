# Extract the longest noun phrase consisting of consecutive nouns.
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

def extract_noun(block):
    res = []
    for i, word in enumerate(block):

        if (word["pos"] == "名詞") & ((i==0)|(block[i-1]["pos"] != "名詞")):
            nouns = ''
            j = 0
            while (i+j < len(block)-1) & (block[i+j]["pos"] == "名詞"):
                nouns += block[i+j]["surface"]
                j += 1
            if j >= 2:
                res.append(nouns)
    return res

filename = 'chapter04/neko.txt.mecab'
with open(filename, mode='rt', encoding='utf-8') as f:
    blocks = f.read().split('EOS\n')

filtered_blocks = list(filter(lambda x: x != '', blocks))
parse_blocks = [parse_mecab(block) for block in filtered_blocks]
parse_blocks = [extract_noun(block) for block in parse_blocks]
print(parse_blocks[8])