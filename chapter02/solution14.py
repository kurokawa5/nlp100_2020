# Receive a natural number $N$ from a command-line argument, and output the first $N$ lines of the file. 
# Confirm the result by using head command.

import sys
import pandas as pd
#import fire

if len(sys.argv) == 1:
    print('Set arg n, like "python chapter02/solution14.py 5"')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('chapter02/popular-names.txt', sep='\t', header=None)
    print(df.head(n))