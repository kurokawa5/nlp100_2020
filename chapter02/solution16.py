# Receive a natural number $N$ from a command-line argument, and split the input file into $N$ pieces at line boundaries.
# Confirm the result by using split command.
import sys
import pandas as pd

if len(sys.argv) == 1:
    print('Set arg n, like "python chapter02/solution16.py 5"')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('chapter02/popular-names.txt', sep='\t', header=None)
    nrow = -(-len(df) // n)

    for i in range(n):
        df.iloc[nrow * i:nrow * (i + 1)].to_csv(f'chapter02/solution16/solution16_{i}', sep='\t', index=False, header=None)