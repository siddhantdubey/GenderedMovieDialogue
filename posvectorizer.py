import random
import ast

random.seed(42)

train = {}
test = {}
X_train = []
X_train_vect = []
Y_train = []
X_test = []
X_test_vect = []
Y_test = []
all_pos_tags = ['#', '$', "''", '(', ')', ',', '.', ':', 'CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB', '``']


with open(r'data/male_tagged_train.txt') as mtagged_train:
    for line in mtagged_train:
        line = str(line.strip())
        line = ast.literal_eval(line)
        train[tuple(line)] = 0

with open(r'data/male_tagged_test.txt', encoding = 'charmap') as mtagged_test:
    for line in mtagged_test:
        line = str(line.strip())
        line = ast.literal_eval(line)
        test[tuple(line)] = 0

with open(r'data/female_tagged_train.txt', encoding = 'charmap') as ftagged_train:
    for line in ftagged_train:
        line = str(line.strip())
        line = ast.literal_eval(line)
        train[tuple(line)] = 1
        
with open(r'data/female_tagged_test.txt', encoding = 'charmap') as ftagged_test:
    for line in ftagged_test:
        line = str(line.strip())
        line = ast.literal_eval(line)
        test[tuple(line)] = 1


train_keys = list(train.keys())
for i in range(len(train_keys)):
    if type(train_keys[i]) == type(5):
        print(i)
        print(train_keys[i])
random.shuffle(train_keys)
train_set =  [(key, train[key]) for key in train_keys]


test_keys = list(test.keys())
random.shuffle(test_keys)
test_set= [(key, test[key]) for key in test_keys]

def str_to_vect(x):
    pos_dict = {key : 0 for key in all_pos_tags}
    tag_list = []
    for i in range(len(x)):
        tag_list.append(x[i][1])
    for j in range(len(tag_list)):
        pos_dict[tag_list[j]] += 1
    
    pos_vector = list(pos_dict.values())
    total = sum(pos_vector)
    pos_prop_vector = []

    for k in range(len(pos_vector)):
        pos_prop_vector.append(pos_vector[k] / total)

    return pos_prop_vector


for i in range(len(train_set)):
    X_train.append(train_set[i][0])
    Y_train.append(train_set[i][1])

for j in range(len(test_set)):
    X_test.append(test_set[j][0])
    Y_test.append(test_set[j][1])


for i in range(len(X_train)):
    X_train_vect.append(str_to_vect(X_train[i]))

for j in range(len(X_test)):
    X_test_vect.append(str_to_vect(X_test[j]))
