# When training a logistic regression model, one can control the degree of overfitting by manipulating the regularization parameters. 
# Use different regularization parameters to train the model. Then, compute the accuracy score on the training data, validation data and test data. 
# Summarize the results on the graph, where x-axis is the regularization parameter and y-axis is the accuracy score.
import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score

def preprocessing(data):
    x = []
    y = []
    label = {"b":0, "e":1, "t":2, "m":3}

    for title, category in data:
        title = re.sub("[0-9]+", "0", title)
        x.append(title.lower())
        y.append(label[category])

    return x,y

def score(model, X):
    pred = model.predict([X])
    pred_proba = model.predict_proba([X])[0, pred]
    return pred[0], pred_proba[0]

def calc(Y, pred):
    ppv = precision_score(Y, pred, average=None)
    ppv_micro = precision_score(Y, pred, average="micro").reshape(1)
    ppv_macro = precision_score(Y, pred, average="macro").reshape(1)
    ppv = np.concatenate([ppv, ppv_micro, ppv_macro])

    recall = recall_score(Y, pred, average=None)
    recall_micro = recall_score(Y, pred, average="micro").reshape(1)
    recall_macro = recall_score(Y, pred, average="macro").reshape(1)
    recall = np.concatenate([recall, recall_micro, recall_macro])

    f1 = f1_score(Y, pred, average=None)
    f1_micro = f1_score(Y, pred, average="micro").reshape(1)
    f1_macro = f1_score(Y, pred, average="macro").reshape(1)
    f1 = np.concatenate([f1, f1_micro, f1_macro])


    index = ["0", "1", "2", "3", "micro", "macro"]
    scores = pd.DataFrame({"ppv": ppv, "recall": recall, "f1":f1}, index=index)

    return scores

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

X_train_df = pd.DataFrame(X_train, columns = tfidfvectorizer.get_feature_names_out())
X_valid_df = pd.DataFrame(X_valid, columns = tfidfvectorizer.get_feature_names_out())
X_test_df = pd.DataFrame(X_test, columns = tfidfvectorizer.get_feature_names_out())

model = LogisticRegression()
model.fit(X_train, Y_train)

result = []

for C in np.logspace(-5, 2, 10, base=np.e):
    model = LogisticRegression(C=C, max_iter=200)
    model.fit(X_train, Y_train)

    train_pred = []
    valid_pred = []
    test_pred = []

    for X in X_train:
        train_pred.append(score(model, X)[0])
    for X in X_valid:
        valid_pred.append(score(model, X)[0])
    for X in X_test:
        test_pred.append(score(model, X)[0])

    train_acc = accuracy_score(Y_train, train_pred)
    valid_acc = accuracy_score(Y_valid, valid_pred)
    test_acc = accuracy_score(Y_test, test_pred)
    print(valid_acc)

    result.append([C, train_acc, valid_acc, test_acc])

result = np.array(result).T

plt.plot(-np.log(result[0]),result[1], label="train")
plt.plot(-np.log(result[0]),result[2], label="valid")
plt.plot(-np.log(result[0]),result[3], label="test")
plt.ylim(0.5, 1.0)

plt.xlabel("ln λ")
plt.ylabel("acc")
plt.legend()
plt.show()