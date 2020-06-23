from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_selection import chi2
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='utf-8', ngram_range=(1, 3), stop_words='english')

male_train = []
female_train = []

with open(r'data/training_set.txt') as training:
    for line in training:
        line = line.strip()
        lnum, chr_id, movie_id, chr_name, chr_gender, line_text, credit_list = line.split("+++$+++")
        chr_gender = chr_gender.strip()
        if(chr_gender.lower() == "m"):
            male_train.append(line_text)
        elif(chr_gender.lower() == "f"):
            female_train.append(line_text)


male_test = []
female_test = []

with open(r'data/test_set.txt') as test:
    for line in test:
        line = line.strip()
        lnum, chr_id, movie_id, chr_name, chr_gender, line_text, credit_list = line.split("+++$+++")
        chr_gender = chr_gender.strip()
        if(chr_gender.lower() == "m"):
            male_test.append(line_text)
        elif(chr_gender.lower() == "f"):
            female_test.append(line_text)

male_valid = []
female_valid = []

with open(r'data/validation_set.txt') as valid:
    for line in valid:
        line = line.strip()
        lnum, chr_id, movie_id, chr_name, chr_gender, line_text, credit_list = line.split("+++$+++")
        chr_gender = chr_gender.strip()
        if(chr_gender.lower() == "m"):
            male_valid.append(line_text)
        elif(chr_gender.lower() == "f"):
            female_valid.append(line_text)

features = tfidf.fit_transform(male_train + female_train).toarray()

labels = ["male", "female"]


X_train = male_train + female_train 
X_test = male_test + female_test 

Y_train = []
Y_test = []

for i in range(len(male_train)):
    Y_train.append("m")

for j in range(len(female_train)):
    Y_train.append("f")

for g in range(len(male_test)):
    Y_test.append("m")          

for h in range(len(female_test)):
    Y_test.append("f")

count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, Y_train)

print(clf.predict(count_vect.transform(["My name is Sara. I am a female. Girly girl"])))

models = [
    RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),
    LinearSVC(),
    MultinomialNB(),
    LogisticRegression(C=1e2, random_state=0, fit_intercept=False),
]


CV = 5
cv_df = pd.DataFrame(index=range(CV * len(models)))
entries = []

for model in models:
    model_name = model.__class__.__name__
    accuracies = cross_val_score(model, X_train_counts, Y_train, scoring='accuracy', cv=5)
    for fold_idx, accuracy in enumerate(accuracies):
        entries.append((model_name, fold_idx, accuracy))
    cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])

import seaborn as sns
sns.boxplot(x='model_name', y='accuracy', data=cv_df)
sns.stripplot(x='model_name', y='accuracy', data=cv_df, 
              size=8, jitter=True, edgecolor="gray", linewidth=2)
plt.show()

# model = RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0)

# model.fit(X_train_counts, Y_train)

# y_pred = model.predict(count_vect.fit_transform(X_test))


# from sklearn.metrics import confusion_matrix

# conf_mat = confusion_matrix(Y_test, y_pred)
# fig, ax = plt.subplots(figsize=(10,10))
# sns.heatmap(conf_mat, annot=True, fmt='d',
#             xticklabels=['m', 'f'], yticklabels=['m', 'f'])
# plt.ylabel('Actual')
# plt.xlabel('Predicted')
# plt.show()