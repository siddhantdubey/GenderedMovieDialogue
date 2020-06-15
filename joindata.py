
with open(r'data/movie_lines.txt') as movie_lines:
    big_list = []
    for line in movie_lines:
        line = line.strip()
        line_num, chr_id, movie_id, chr_name, line_txt = line.split('+++$+++')
        line_list = [line_num, chr_id, movie_id, chr_name,0, line_txt]
        for i in range(1):
            e = str(line_list[i])
            e = e.replace(' ','')        
        big_list.append(line_list)

with open(r'data/movie_characters_metadata.txt') as chr_data:
    user_gender = {}
    for line in chr_data:
        line = line.strip()
        chr_id, name, movie_id, movie_name, gender, credit_order = line.split('+++$+++')
        chr_id = chr_id.replace(' ','')
        gender = gender.replace(' ','')
        gender = ' ' + gender
        user_gender[chr_id] = gender

for i in range(len(big_list)):
    big_list[i][4] = user_gender[big_list[i][1].replace(' ','')]

with open(r'data/collated_data.txt','w+') as fout:
    for i in range(len(big_list)):
        line = ''
        for j in range(len(big_list[i])):
            line += big_list[i][j] + ' +++$+++'
        line = line.strip('+++$+++')
        fout.write(line)
        fout.write('\n')
