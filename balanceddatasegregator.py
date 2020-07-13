
male_pos_list = []
with open(r'data/male_tagged.txt') as mtagged:
    for line in mtagged:
        line = line.strip()
        male_pos_list.append(line)

male_pos_list = male_pos_list[:114253]

with open(r'data/male_tagged_balanced.txt','w+') as mtaggedb:
    for i in range(len(male_pos_list)):
        mtaggedb.write(male_pos_list[i])
        mtaggedb.write('\n')

with open(r'data/male_tagged_balanced.txt') as mtaggeds:
    mtrain_set = []
    mtest_set = []
    c = 0 
    for line in mtaggeds:
        c += 1
        if c <= 91402:
            mtrain_set.append(line)
        else:
            mtest_set.append(line)

with open(r'data/female_tagged.txt') as ftaggeds:
    ftrain_set = []
    ftest_set = []
    c = 0
    for line in ftaggeds:
        c += 1
        if c <= 91402:
            ftrain_set.append(line)
        else:
            ftest_set.append(line)

with open(r'data/male_tagged_train.txt','w+') as mtaggedtrain:
    for i in range(len(mtrain_set)):
        mtaggedtrain.write(mtrain_set[i])

with open(r'data/male_tagged_test.txt','w+') as mtaggedtest:
    for i in range(len(mtest_set)):
        mtaggedtest.write(mtest_set[i])

with open(r'data/female_tagged_train.txt','w+') as ftaggedtrain:
    for i in range(len(ftrain_set)):
        ftaggedtrain.write(ftrain_set[i])

with open(r'data/female_tagged_test.txt','w+') as ftaggedtest:
    for i in range(len(ftest_set)):
        ftaggedtest.write(ftest_set[i])