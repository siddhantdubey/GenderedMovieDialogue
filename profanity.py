
profanity_list = []
with open(r'data/profane_words.txt') as prof:
    for line in prof:
        line = line.strip()
        line = line.lower()
        profanity_list.append(line)

mbad_words = []
mbad_lines = 0
with open(r'data/male_text.txt') as m_text:
    total_male_lines = 0
    total_male_words = 0
    for line in m_text:
        total_male_lines += 1
        line_count = 0
        line = line.strip()
        line = line.lower()
        words = line.split()
        total_male_words += len(words)
        for i in range(len(words)):
            if words[i] in profanity_list:
                line_count += 1
        mbad_words.append(line_count)

    for j in range(len(mbad_words)):
        if mbad_words[j] > 0:
            mbad_lines += 1
    total_mbad_words = sum(mbad_words)

fbad_words = []
fbad_lines = 0
with open(r'data/female_text.txt') as f_text:
    total_female_lines = 0
    total_female_words = 0
    for line in f_text:
        total_female_lines += 1
        line_count = 0
        line = line.strip()
        line = line.lower()
        words = line.split()
        total_female_words += len(words)
        for i in range(len(words)):
            if words[i] in profanity_list:
                line_count += 1
        fbad_words.append(line_count)

    for j in range(len(fbad_words)):
        if fbad_words[j] > 0:
            fbad_lines += 1
    total_fbad_words = sum(fbad_words)
        
gbad_words = []
gbad_lines = 0
with open(r'data/genderless_text.txt') as g_text:
    total_genderless_lines = 0
    total_genderless_words = 0
    for line in g_text:
        total_genderless_lines += 1
        line_count = 0
        line = line.strip()
        line = line.lower()
        words = line.split()
        total_genderless_words += len(words)
        for i in range(len(words)):
            if words[i] in profanity_list:
                line_count += 1
        gbad_words.append(line_count)

    for j in range(len(gbad_words)):
        if gbad_words[j] > 0:
            gbad_lines += 1
    total_gbad_words = sum(gbad_words)

mbad_word_prop = total_mbad_words / total_male_words
mbad_line_prop = mbad_lines / total_male_lines
fbad_word_prop = total_fbad_words / total_female_words
fbad_line_prop = fbad_lines / total_female_lines
gbad_word_prop = total_gbad_words / total_genderless_words
gbad_line_prop = gbad_lines / total_genderless_lines

print('The total number of bad words in male utterances is %d' % total_mbad_words)
print('The total number of male utterances with bad words is %d' % mbad_lines)
print('The proportion of all words spoken by male characters which are profanity is %.5f' % mbad_word_prop)
print('The proportion of all male utterances which contain profanity is %.5f' % mbad_line_prop)
print('The total number of bad words in female utterances is %d' % total_fbad_words)
print('The total number of female utterances with bad words is %d' % fbad_lines)
print('The proportion of all words spoken by female characters which are profanity is %.5f' % fbad_word_prop)
print('The proportion of all female utterances which contain profanity is %.5f' % fbad_line_prop)
print('The total number of bad words in genderless utterances is %d'% total_gbad_words)
print('The total number of genderless utterances with bad words is %d' % gbad_lines)
print('The proportion of all words spoken by genderless characters which are profanity is %.5f' % gbad_word_prop)
print('The proportion of all genderless utterances which contain profanity is %.5f' % gbad_line_prop)