# Find distinct strings (a set of strings) of the first column of the file.
# Confirm the result by using cut, sort, and uniq commands.
import pandas as pd

df = pd.read_csv('chapter02/popular-names.txt', sep='\t', header=None)
ans = list(set(df.iloc[:,0]))
print(sorted(ans))