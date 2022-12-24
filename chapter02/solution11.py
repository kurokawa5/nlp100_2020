import pandas as pd

df = pd.read_csv('chapter02/popular-names.txt', sep='\t', header=None)
df.to_csv('chapter02/solution11.txt', sep=' ', index=False, header=None)