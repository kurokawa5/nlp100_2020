# Implement a program that reads the result of part-of-speech tagging.
# Here, represent a sentence as a list of mapping objects, each of which associates a surface form,
# lemma (base form), part-of-speech tag with the keys text, lemma, pos.
# Use this representation in the rest of the problems.
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
#print(blocks[:3])
print(parse_blocks[:3])