
with open(r'data/collated_data.txt') as cdata:
    train_data = []
    test_data = []
    valid_data = []
    for line in cdata:
        line_num, chr_id, movie_id, chr_name, gender, line_txt, credit_order = line.split('+++$+++')
        mod_movie_id = movie_id.replace('m','')
        mod_movie_id = int(mod_movie_id)
        line = line.replace('<i>','')
        line = line.replace('</i>','')
        if mod_movie_id <= 492:
            train_data.append(line)
        elif mod_movie_id <= 554 and mod_movie_id >=493:
            test_data.append(line)
        elif mod_movie_id >= 555:
            valid_data.append(line)

with open(r'data/training_set.txt','w+') as train_set:
    for i in range(len(train_data)):
        train_set.write(str(train_data[i]))

with open(r'data/test_set.txt','w+') as test_set:
    for j in range(len(test_data)):
        test_set.write(str(test_data[j]))

with open(r'data/validation_set.txt','w+') as valid_set:
    for k in range(len(valid_data)):
        valid_set.write(str(valid_data[k]))