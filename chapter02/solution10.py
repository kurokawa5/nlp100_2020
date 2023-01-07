# Count the number of lines of the file. Confirm the result by using wc command.

import pandas as pd

df = pd.read_csv('chapter02/popular-names.txt', sep='\t', header=None)
print(len(df))