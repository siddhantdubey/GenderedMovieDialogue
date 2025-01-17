from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.model_selection import cross_val_score, validation_curve
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='utf-8', ngram_range=(1, 3), stop_words='english')


X_train = []
X_test = []
Y_train = []
Y_test = []
X_valid = []
Y_valid = []


male = []
female = []


with open(r'data/training_set.txt') as training:
    for line in training:
        line = line.strip()
        lnum, chr_id, movie_id, chr_name, chr_gender, line_text, credit_list = line.split("+++$+++")
        chr_gender = chr_gender.strip()
        if(chr_gender.lower() == "m"):
            X_train.append(line_text)
            male.append(line_text)
            Y_train.append(0)
        elif(chr_gender.lower() == "f"):
            X_train.append(line_text)
            female.append(line_text)
            Y_train.append(1)


with open(r'data/test_set.txt') as test:
    for line in test:
        line = line.strip()
        lnum, chr_id, movie_id, chr_name, chr_gender, line_text, credit_list = line.split("+++$+++")
        chr_gender = chr_gender.strip()
        if(chr_gender.lower() == "m"):
            X_test.append(line_text)
            male.append(line_text)
            Y_test.append(0)
        elif(chr_gender.lower() == "f"):
            X_test.append(line_text)
            female.append(line_text)
            Y_test.append(1)




with open(r'data/validation_set.txt') as valid:
    for line in valid:
        line = line.strip()
        lnum, chr_id, movie_id, chr_name, chr_gender, line_text, credit_list = line.split("+++$+++")
        chr_gender = chr_gender.strip()
        if(chr_gender.lower() == "m"):
            X_valid.append(line_text)
            male.append(line_text)
            Y_valid.append(0)
        elif(chr_gender.lower() == "f"):
            X_valid.append(line_text)
            female.append(line_text)
            Y_valid.append(1)
print(len(female))


# male_train = male[:48000]
# female_train = female[:48000]
# male_test = male[48001:49001]
# female_test = female[48001:49001]


# print(len(male_test))
X = X_train + X_test + X_valid
Y = Y_train + Y_test + Y_valid

print('Data Compiled')

indices = []
for i in range(len(X)):
  if(len(X[i]) > 0):
    answer = True 
  else:
    indices.append(i)

for index in sorted(indices, reverse=True):
    del X[index]
    del Y[index]


df = pd.DataFrame()

df['text'] = X
df['target'] = Y
def get_top_data(top_n = 30000):
  top_data_df_male = df[df['target'] == 0].head(top_n)
  top_data_df_female = df[df['target'] == 1].head(top_n)
  data_df_small = pd.concat([top_data_df_male, top_data_df_female])
  return data_df_small

top_data_df_small = get_top_data(top_n=Y.count(1))

from sklearn.model_selection import train_test_split
def split_train_test(top_data_df_small, test_size=0.1, shuffle_state=True):
    X_train, X_test, Y_train, Y_test = train_test_split(top_data_df_small[['text']], 
                                                        top_data_df_small['target'], 
                                                        shuffle=shuffle_state,
                                                        test_size=test_size, 
                                                        random_state=15)
    print("Value counts for Train genders")
    print(Y_train.value_counts())
    print("Value counts for Test genders")
    print(Y_test.value_counts())
    print(type(X_train))
    print(type(Y_train))
    X_train = X_train.reset_index()
    X_test = X_test.reset_index()
    Y_train = Y_train.to_frame()
    Y_train = Y_train.reset_index()
    Y_test = Y_test.to_frame()
    Y_test = Y_test.reset_index()
    # print(X_train.head())
    return X_train, X_test, Y_train, Y_test


# Call the train_test_split
X_train, X_test, Y_train, Y_test = split_train_test(df)

X_train = X_train['text']
Y_train = Y_train['target']
X_test = X_test['text']
Y_test = Y_test['target']
# features = tfidf.fit_transform(X_train + Y_train).toarray()

# labels = [0, 1]


print("Data Split")
count_vect = CountVectorizer(ngram_range=(1,3))

X_train_counts = count_vect.fit_transform(X)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(np.asarray(X_train_tfidf))
print("Count Vectorized")
# kbest = SelectKBest(score_func = chi2, k = 1)
# X_train_kbest = kbest.fit_transform(X_train_counts, Y_train)
# print(X_train_kbest)

# clf = MultinomialNB().fit(X_train_tfidf, Y_train)

# print(clf.predict(count_vect.transform(["My name is Sara. I am a female. Girly girl"])))

models = [
    RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),
    LinearSVC(),
    MultinomialNB(alpha=1.1),
    LogisticRegression(C=1e2, random_state=0, fit_intercept=False),
    MLPClassifier(alpha=1, max_iter=1000),
    AdaBoostClassifier(n_estimators=200),
    SVC(gamma=2, C=1e2),
    DecisionTreeClassifier(max_depth=3)

    
]


CV = 5
cv_df = pd.DataFrame(index=range(CV * len(models)))
entries = []

for model in models:
    model_name = model.__class__.__name__
    accuracies = cross_val_score(model, X_train_tfidf, Y, scoring='accuracy', cv=5)
    
    # name = "n_estimators"
    # if(model_name.strip() == "RandomForestClassifier"):
    #     name = "max_depth"
    #     param_range = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    #     train_scores, test_scores = validation_curve(model, X_train_tfidf, Y_train, param_name=name, param_range=param_range, scoring="accuracy", n_jobs=1)
    #     train_scores_mean = np.mean(train_scores, axis=1)
    #     train_scores_std = np.std(train_scores, axis=1)
    #     test_scores_mean = np.mean(test_scores, axis=1)
    #     test_scores_std = np.std(test_scores, axis=1)

    #     plt.title("Validation Curve with " + model_name)
    #     plt.xlabel(name)
    #     plt.ylabel("Score")
    #     plt.ylim(0.0, 1.1)
    #     lw = 2
    #     plt.semilogx(param_range, train_scores_mean, label="Training score", color="darkorange", lw=lw)
    #     plt.fill_between(param_range, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.2, color="darkorange", lw=lw)
    #     plt.semilogx(param_range, test_scores_mean, label="Cross-validation score", color="navy", lw=lw)
    #     plt.fill_between(param_range, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.2, color="navy", lw=lw)
    #     plt.legend(loc="best")
    #     plt.savefig('figures/models/' + model_name + 'large.png')
    #     plt.close()
    # elif(model_name.strip() == "LinearSVC"):
    #     name = "loss"
    #     # param_range = np.logspace(-6, -1, 5)
    #     param_range = ['hinge', 'squared_hinge']
    #     train_scores, test_scores = validation_curve(model, X_train_tfidf, Y_train, param_name=name, param_range=param_range, scoring="accuracy", n_jobs=1)
    #     train_scores_mean = np.mean(train_scores, axis=1)
    #     train_scores_std = np.std(train_scores, axis=1)
    #     test_scores_mean = np.mean(test_scores, axis=1)
    #     test_scores_std = np.std(test_scores, axis=1)

    #     plt.title("Validation Curve with " + model_name)
    #     plt.xlabel(name)
    #     plt.ylabel("Score")
    #     plt.ylim(0.0, 1.1)
    #     lw = 2
    #     plt.semilogx(param_range, train_scores_mean, label="Training score", color="darkorange", lw=lw)
    #     plt.fill_between(param_range, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.2, color="darkorange", lw=lw)
    #     plt.semilogx(param_range, test_scores_mean, label="Cross-validation score", color="navy", lw=lw)
    #     plt.fill_between(param_range, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.2, color="navy", lw=lw)
    #     plt.legend(loc="best")
    #     plt.savefig('figures/models/' + model_name + 'large.png')
    #     plt.close()
    # elif(model_name.strip() == "MultinomialNB"):
    #     name = "alpha"
    #     param_range = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
    #     train_scores, test_scores = validation_curve(model, X_train_tfidf, Y_train, param_name=name, param_range=param_range, scoring="accuracy", n_jobs=1)
    #     train_scores_mean = np.mean(train_scores, axis=1)
    #     train_scores_std = np.std(train_scores, axis=1)
    #     test_scores_mean = np.mean(test_scores, axis=1)
    #     test_scores_std = np.std(test_scores, axis=1)

    #     plt.title("Validation Curve with " + model_name)
    #     plt.xlabel(name)
    #     plt.ylabel("Score")
    #     plt.ylim(0.0, 1.1)
    #     lw = 2
    #     plt.semilogx(param_range, train_scores_mean, label="Training score", color="darkorange", lw=lw)
    #     plt.fill_between(param_range, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.2, color="darkorange", lw=lw)
    #     plt.semilogx(param_range, test_scores_mean, label="Cross-validation score", color="navy", lw=lw)
    #     plt.fill_between(param_range, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.2, color="navy", lw=lw)
    #     plt.legend(loc="best")
    #     plt.savefig('figures/models/' + model_name + 'large.png')
    #     plt.close()
    # elif(model_name.strip() == "LogisticRegression"):
    #     name = "C"
    #     param_range = np.logspace(-6, -1, 5)
    #     train_scores, test_scores = validation_curve(model, X_train_tfidf, Y_train, param_name=name, param_range=param_range, scoring="accuracy", n_jobs=1)
    #     train_scores_mean = np.mean(train_scores, axis=1)
    #     train_scores_std = np.std(train_scores, axis=1)
    #     test_scores_mean = np.mean(test_scores, axis=1)
    #     test_scores_std = np.std(test_scores, axis=1)

    #     plt.title("Validation Curve with " + model_name)
    #     plt.xlabel(name)
    #     plt.ylabel("Score")
    #     plt.ylim(0.0, 1.1)
    #     lw = 2
    #     plt.semilogx(param_range, train_scores_mean, label="Training score", color="darkorange", lw=lw)
    #     plt.fill_between(param_range, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.2, color="darkorange", lw=lw)
    #     plt.semilogx(param_range, test_scores_mean, label="Cross-validation score", color="navy", lw=lw)
    #     plt.fill_between(param_range, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.2, color="navy", lw=lw)
    #     plt.legend(loc="best")
    #     plt.savefig('figures/models/' + model_name + '_' +  name +  'large.png')
    #     plt.close()
    for fold_idx, accuracy in enumerate(accuracies):
        entries.append((model_name, fold_idx, accuracy))
    cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])
    
    print(model_name + " done testing")
cv_df.to_csv('data/lotsofmodelstfidf.csv')
import seaborn as sns
sns.boxplot(x='model_name', y='accuracy', data=cv_df)
sns.stripplot(x='model_name', y='accuracy', data=cv_df, 
              size=8, jitter=True, edgecolor="gray", linewidth=2)
plt.savefig('figures/models/lotsofmodelstfidf.png')
plt.show()
plt.close()
