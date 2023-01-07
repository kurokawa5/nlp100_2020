# Join the contents of col1.txt and col2.txt, and create a text file whose each line contains
# the values of the first and second columns (separated by tab character) of the original file.
# Confirm the result by using paste command.import pandas as pd
import pandas as pd

df_col1 = pd.read_csv('chapter02/col1.txt', header=None)
df_col2 = pd.read_csv('chapter02/col2.txt', header=None)
df_merged = pd.concat([df_col1, df_col2], axis=1)
df_merged.to_csv('chapter02/solution13.txt', sep='\t', index=False, header=False)
