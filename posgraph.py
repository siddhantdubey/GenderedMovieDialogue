import numpy as np
import matplotlib.pyplot as plt
import ast
import numpy as np
from tabulate import tabulate
from collections import OrderedDict

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
male_pos_prop = {}
mkey_list = list(male_pos.keys())
total_mtokens = sum(list(male_pos.values()))
for i in range(len(mkey_list)):
    male_pos_prop[mkey_list[i]] = male_pos[mkey_list[i]] / total_mtokens

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
fem_pos_prop = {}
fkey_list = list(fem_pos.keys())
total_ftokens = sum(list(fem_pos.values()))
for j in range(len(fkey_list)):
    fem_pos_prop[fkey_list[j]] = fem_pos[fkey_list[j]] / total_ftokens

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

gl_pos_prop = {}
gkey_list = list(gl_pos.keys())
total_gtokens = sum(list(gl_pos.values()))
for k in range(len(gkey_list)):
    gl_pos_prop[gkey_list[k]] = male_pos[mkey_list[k]] / total_gtokens

male_pos = dict(OrderedDict(sorted(male_pos.items())))
fem_pos = dict(OrderedDict(sorted(fem_pos.items())))
gl_pos = dict(OrderedDict(sorted(gl_pos.items())))
male_pos_prop = dict(OrderedDict(sorted(male_pos_prop.items())))
fem_pos_prop = dict(OrderedDict(sorted(fem_pos_prop.items())))
gl_pos_prop = dict(OrderedDict(sorted(gl_pos_prop.items())))


width = 0.3
plt.figure(figsize=(20,4))
plt.title('Frequency of POS Tags in Utterances Spoken by Male Characters')
plt.xlabel('POS Tags')
plt.ylabel('Frequency')
plt.bar(male_pos.keys(), male_pos.values(), width, align='edge', color = 'g')
plt.xticks(rotation=90)
plt.savefig('figures/male_pos.png')
plt.close()

plt.figure(figsize=(20,4))
plt.title('Frequency of POS Tags in Utterances Spoken by Female Characters')
plt.xlabel('POS Tags')
plt.ylabel('Frequency')
plt.bar(fem_pos.keys(), fem_pos.values(), width, align='edge', color = 'r')
plt.xticks(rotation=90)
plt.savefig('figures/female_pos.png')
plt.close()

plt.figure(figsize=(20,4))
plt.title('Frequency of POS Tags in Utterances Spoken by Genderless Characters')
plt.xlabel('POS Tags')
plt.ylabel('Frequency')
plt.bar(gl_pos.keys(), gl_pos.values(), width, align='edge', color = 'b')
plt.xticks(rotation=90)
plt.savefig('figures/genderless_pos.png')
plt.close()


N = len(list(male_pos.keys()))
fig, ax = plt.subplots()
fig.set_figheight(4)
fig.set_figwidth(20)
ind = np.arange(N)
width = 0.3
p1 = ax.bar(ind, list(male_pos.values()), width)
p2 = ax.bar(ind + width, list(fem_pos.values()), width)
ax.set_title('Frequency of POS Tags in Utterances Spoken by Characters')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(tuple(male_pos.keys()))
ax.legend((p1[0], p2[0]), ('Male', 'Female'))
ax.autoscale_view()
plt.savefig('figures/combined_pos_plots.png')
plt.close()

N = len(list(male_pos_prop.keys()))
fig, ax = plt.subplots()
fig.set_figheight(4)
fig.set_figwidth(20)
ind = np.arange(N)
width = 0.3
p1 = ax.bar(ind, list(male_pos_prop.values()),width)
p2 = ax.bar(ind+ width, list(fem_pos_prop.values()),width)
ax.set_title('Proportion of Utterances with POS Tags')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(tuple(male_pos_prop.keys()))
ax.legend((p1[0], p2[0]), ('Male', 'Female'))
ax.autoscale_view()
plt.savefig('figures/combined_pos_prop_plots.png')

male_female_ratio = {}
for i in range(len(list(male_pos.keys()))):
    curr_ind = (list(male_pos.keys()))[i]
    male_female_ratio[curr_ind] = male_pos[curr_ind] / fem_pos[curr_ind]

plt.figure(figsize=(20,4))
plt.title('Ratio of Male to Female Frequency of POS Tags')
plt.xlabel('POS Tags')
plt.ylabel('Male-to-Female Ratio')
plt.bar(male_female_ratio.keys(), male_female_ratio.values(), width, align='edge', color = 'b')
plt.xticks(rotation=90)
plt.savefig('figures/POS_ratio.png')
plt.close()

male_female_prop_ratio = {}
for j in range(len(list(male_pos_prop.keys()))):
    curr_ind = (list(male_pos_prop.keys()))[j]
    male_female_prop_ratio[curr_ind] = male_pos_prop[curr_ind] / fem_pos_prop[curr_ind]

plt.figure(figsize=(20,4))
plt.title('Ratio of Male to Female Proportion of POS Tags')
plt.xlabel('POS Tags')
plt.ylabel('Male-to-Female Ratio')
plt.bar(male_female_prop_ratio.keys(), male_female_prop_ratio.values(), width, align='edge', color = 'g')
plt.xticks(rotation=90)
plt.savefig('figures/POS_prop_ratio.png')
plt.close()

'''
width = 0.1
fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False)
plt.figure(figsize=(20,3))
plt.suptitle('Frequency of POS Tags in Utterances Spoken by Characters')
axs[0].set_xlabel('POS Tags')
axs[1].set_xlabel('POS Tags')
axs[2].set_xlabel('POS Tags')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Male')
axs[1].set_title('Female')
axs[2].set_title('Genderless')
axs[0].bar(male_pos.keys(), male_pos.values(), width, color = 'g')
axs[1].bar(fem_pos.keys(), fem_pos.values(), width, color = 'm')
axs[2].bar(gl_pos.keys(), gl_pos.values(), width, color = 'b')

plt.savefig("figures/combined_pos_plots.png")
plt.close()


fig, axs = plt.subplots(1,3, sharey = True, tight_layout = False)
plt.suptitle('Proportion of POS Tags in Utterances Spoken by Characters')
axs[0].set_xlabel('POS Tags')
axs[1].set_xlabel('POS Tags')
axs[2].set_xlabel('POS Tags')
axs[0].set_ylabel('Proportion of Total Tokens')
axs[0].set_title('Male')
axs[1].set_title('Female')
axs[2].set_title('Genderless')
axs[0].bar(male_pos_prop.keys(), male_pos_prop.values(), width, color = 'g')
axs[1].bar(fem_pos_prop.keys(), fem_pos_prop.values(), width, color = 'm')
axs[2].bar(gl_pos_prop.keys(), gl_pos_prop.values(), width, color = 'b')

plt.savefig('figures/combined_pos_prop_plots.png')
plt.close()
'''
print('Table of Number of Male Tokens of Each POS Tag')
mtable1 = []
for i in range(len(list(male_pos.keys()))):
    a = (list(male_pos_prop.keys()))[i]
    a = str(a)
    b = (list(male_pos.values()))[i]
    b = float(b)
    mtable1.append([a,b])
print(tabulate(mtable1, headers = ['POS Tags', 'Quantity']))

print('Table of Number of Female Tokens of Each POS Tag')
ftable1 = []
for i in range(len(list(fem_pos.keys()))):
    a = (list(fem_pos_prop.keys()))[i]
    a = str(a)
    b = (list(fem_pos.values()))[i]
    b = float(b)
    ftable1.append([a,b])
print(tabulate(ftable1, headers = ['POS Tags', 'Quantity']))

print('Table of Number of Genderless Tokens of Each POS Tag')
gtable1 = []
for i in range(len(list(gl_pos.keys()))):
    a = (list(gl_pos_prop.keys()))[i]
    a = str(a)
    b = (list(gl_pos.values()))[i]
    b = float(b)
    gtable1.append([a,b])
print(tabulate(gtable1, headers = ['POS Tags', 'Quantity']))

print('Table of Proportion of Male Tokens of each POS Tag')
mtable2 = []
for i in range(len(list(male_pos_prop.keys()))):
    a = (list(male_pos_prop.keys()))[i]
    a = str(a)
    b = (list(male_pos_prop.values()))[i]
    b = float(b)
    mtable2.append([a,b])
print(tabulate(mtable2, headers = ['POS Tags', 'Proportion']))

print('Table of Proportion of Female Tokens of each POS Tag')
ftable2 = []
for i in range(len(list(fem_pos_prop.keys()))):
    a = (list(fem_pos_prop.keys()))[i]
    a = str(a)
    b = (list(fem_pos_prop.values()))[i]
    b = float(b)
    ftable2.append([a,b])
print(tabulate(ftable2, headers = ['POS Tags', 'Proportion']))    

print('Table of Proportion of Genderless Tokens of each POS Tag')
gtable2 = []
for i in range(len(list(gl_pos_prop.keys()))):
    a = (list(gl_pos_prop.keys()))[i]
    a = str(a)
    b = (list(gl_pos_prop.values()))[i]
    b = float(b)
    gtable2.append([a,b])
print(tabulate(gtable2, headers = ['POS Tags', 'Proportion']))  

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