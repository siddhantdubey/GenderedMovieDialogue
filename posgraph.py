import numpy as np
import matplotlib.pyplot as plt
import ast

def adj_adv_prop(my_dict):
    total = sum(list(my_dict.values()))
    adj_count = my_dict['JJ'] + my_dict['JJR'] + my_dict['JJS']
    adv_count = my_dict['RB'] + my_dict['RBR'] + my_dict['RBS']
    adj_prop = adj_count / total
    adv_prop = adv_count / total

    return [adj_prop, adv_prop]

with open(r'data/male_tagged.txt') as male_t:
    male_pos = {}
    for line in male_t:
        line = line.strip()
        line = ast.literal_eval(line)
        for i in range(len(line)):
            pos = line[i][1]
            if pos in male_pos.keys():
                male_pos[pos] += 1
            else:
                male_pos[pos] = 1

with open(r'data/female_tagged.txt') as fem_t:
    fem_pos = {}
    for line in fem_t:
        line = line.strip()
        line = ast.literal_eval(line)
        for i in range(len(line)):
            pos = line[i][1]
            if pos in fem_pos.keys():
                fem_pos[pos] += 1
            else:
                fem_pos[pos] = 1

with open(r'data/genderless_tagged.txt') as gl_t:
    gl_pos = {}
    for line in gl_t:
        line = line.strip()
        line = ast.literal_eval(line)
        for i in range(len(line)):
            pos = line[i][1]
            if pos in gl_pos.keys():
                gl_pos[pos] += 1
            else:
                gl_pos[pos] = 1

width = 2.0
plt.title('Frequency of POS Tags in Utterances Spoken by Male Characters')
plt.xlabel('POS Tags')
plt.ylabel('Frequency')
plt.bar(male_pos.keys(), male_pos.values(), width, color = 'g')
plt.savefig('figures/male_pos.png')
plt.close()

plt.title('Frequency of POS Tags in Utterances Spoken by Female Characters')
plt.xlabel('POS Tags')
plt.ylabel('Frequency')
plt.bar(fem_pos.keys(), fem_pos.values(), width, color = 'r')
plt.savefig('figures/female_pos.png')
plt.close()

plt.title('Frequency of POS Tags in Utterances Spoken by Genderless Characters')
plt.xlabel('POS Tags')
plt.ylabel('Frequency')
plt.bar(gl_pos.keys(), gl_pos.values(), width, color = 'b')
plt.savefig('figures/genderless_pos.png')
plt.close()

width = 1.0
fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False)
plt.suptitle('Frequency of POS Tags in Utterances Spoken by Characters')
axs[0].set_xlabel('POS Tags')
axs[1].set_xlabel('POS Tags')
axs[2].set_xlabel('POS Tags')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Male')
axs[1].set_title('Female')
axs[2].set_title('Genderless')
axs[0].bar(male_pos.keys(), male_pos.values(), width, color = 'g')
axs[1].bar(fem_pos.keys(), fem_pos.values(), width, color = 'r')
axs[2].bar(gl_pos.keys(), gl_pos.values(), width, color = 'b')
plt.savefig("figures/combined_pos_plots.png")
plt.close()

m = adj_adv_prop(male_pos)
f = adj_adv_prop(fem_pos)
g = adj_adv_prop(gl_pos)

male_adj_prop = m[0]
male_adv_prop = m[1]
female_adj_prop = f[0]
female_adv_prop = f[1]
genderless_adj_prop = g[0]
genderless_adv_prop = g[1]

print('The proportion of words spoken by male characters that are adjectives is %.5f' % male_adj_prop)
print('The proportion of words spoken by male characters that are adverbs is %.5f' % male_adv_prop)
print('The proportion of words spoken by female characters that are adjectives is %.5f' % female_adj_prop)
print('The proportion of words spoken by female characters that are adverbs is %.5f' % female_adv_prop)
print('The proportion of words spoken by genderless characters that are adjectives is %.5f' % genderless_adj_prop)
print('The proportion of words spoken by genderless characters that are adverbs is %.5f' % genderless_adv_prop)
