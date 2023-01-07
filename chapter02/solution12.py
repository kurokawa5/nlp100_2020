# Extract the value of the first column of each line, and store the output into col1.txt.
# Extract the value of the second column of each line, and store the output into col2.txt.
# Confirm the result by using cut command.
import pandas as pd

df = pd.read_csv('chapter02/popular-names.txt', sep='\t', header=None)
df.iloc[:,0].to_csv('chapter02/col1.txt', index=False, header=False)
df.iloc[:,1].to_csv('chapter02/col2.txt', index=False, header=False)