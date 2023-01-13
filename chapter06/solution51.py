# Extract a set of features from the training, validation and test data, respectively.
# Save the features into files as follows: train.feature.txt, valid.feature.txt and test.feature.txt.
# Design the features that are useful for the news classification.
# The minimum baseline for the features is the tokenized sequence of the news headline.
import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocessing(data):
    x = []
    y = []
    label = {"b":0, "e":1, "t":2, "m":3}

    for title, category in data:
        title = re.sub("[0-9]+", "0", title)
        x.append(title.lower())
        y.append(label[category])

    return x,y

np.random.seed(123)
df = pd.read_csv("chapter06/NewsAggregatorDataset/newsCorpora.csv", header=None, sep="\t", names=["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"])
df = df.loc[df["PUBLISHER"].isin(["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]), ["TITLE", "CATEGORY"]]

train, valid_test = train_test_split(df, test_size=0.2, shuffle=True)
valid, test = train_test_split(valid_test, test_size=0.5, shuffle=True)

train = np.array(train)
valid = np.array(valid)
test = np.array(test)

X_train, Y_train = preprocessing(train)
X_valid, Y_valid = preprocessing(valid)
X_test, Y_test = preprocessing(test)

tfidfvectorizer = TfidfVectorizer(min_df=0.001)

X_train = tfidfvectorizer.fit_transform(X_train).toarray()
X_valid = tfidfvectorizer.transform(X_valid).toarray()
X_test = tfidfvectorizer.transform(X_test).toarray()

X_train = pd.DataFrame(X_train, columns = tfidfvectorizer.get_feature_names_out())
X_valid = pd.DataFrame(X_valid, columns = tfidfvectorizer.get_feature_names_out())
X_test = pd.DataFrame(X_test, columns = tfidfvectorizer.get_feature_names_out())

X_train.to_csv("chapter06/solution51/train.feature.txt", sep="\t", index=False)
X_valid.to_csv("chapter06/solution51/valid.feature.txt", sep="\t", index=False)
X_test.to_csv("chapter06/solution51/test.feature.txt", sep="\t", index=False)