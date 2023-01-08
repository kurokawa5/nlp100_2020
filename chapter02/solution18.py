# Sort the lines in descending numeric order of the third column (sort lines without changing the content of each line). 
# Confirm the result by using sort command.
import pandas as pd

df = pd.read_csv('chapter02/popular-names.txt', sep='\t', header=None)
print(df.sort_values(2 ,ascending=False))
