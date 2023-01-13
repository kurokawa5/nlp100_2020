# Download News Aggregator Data Set and create training data (train.txt), validation data (valid.txt) and test data (test.txt) as follows:
# 1. Unpack the downloaded zip file and read readme.txt.
# 2. Extract the articles such that the publisher is one of the followings: “Reuters”, “Huffington Post”, “Businessweek”, “Contactmusic.com” and “Daily Mail”.
# 3. Randomly shuffle the extracted articles.
# 4. Split the extracted articles in the following ratio: the training data (80%), the validation data (10%) and the test data (10%). 
# Then save them into files train.txt, valid.txt and test.txt, respectively. In each file, each line should contain a single instance. Each instance should contain both the name of the category and the article headline. 
# Use Tab to separate each field.
# After creating the dataset, check the number of instances contained in each category.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(123)
df = pd.read_csv("chapter06/NewsAggregatorDataset/newsCorpora.csv", header=None, sep="\t", names=["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"])
df = df.loc[df["PUBLISHER"].isin(["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]), ["TITLE", "CATEGORY"]]

train, valid_test = train_test_split(df, test_size=0.2, shuffle=True)
valid, test = train_test_split(valid_test, test_size=0.5, shuffle=True)

train.to_csv("chapter06/solution50/train.txt", sep="\t", index=False)
valid.to_csv("chapter06/solution50/valid.txt", sep="\t", index=False)
test.to_csv("chapter06/solution50/test.txt", sep="\t", index=False)