# Find the frequency of a string in the first column, and sort the strings by descending order of their frequencies.
# Confirm the result by using cut, uniq, and sort commands.
import pandas as pd

df = pd.read_csv('chapter02/popular-names.txt', sep='\t', header=None)
print(df.iloc[:,0].value_counts())
#print(df[0].value_counts())

