from matplotlib import pyplot as plt
import numpy as np

num_male_words = []
num_female_words = []
num_genderless_words = []

with open(r"data/male_text.txt") as male:
    male_i = 0
    male_total = 0
    for line in male:
        line.strip()
        words = line.split()
        length = len(words)
        num_male_words.append(length)
        male_total += length 
        male_i += 1
    male_avg = (male_total/male_i)

with open(r"data/female_text.txt") as female:
    fem_num = 0
    fem_total = 0
    for line in female:
        line.strip()
        words = line.split()
        length = len(words)
        num_female_words.append(length)
        fem_total += length
        fem_num += 1
    fem_avg = (fem_total/fem_num)
with open(r"data/genderless_text.txt") as fin:
    gender_num = 0
    gender_total = 0
    for line in fin:
        line.strip()
        words = line.split()
        length = len(words)
        num_genderless_words.append(length)
        gender_total += length
        gender_num += 1
    genderless_avg = (gender_num/gender_num)



num_male_words = np.array(num_male_words)
num_female_words = np.array(num_female_words)
num_genderless_words = np.array(num_genderless_words)

unique_num_male = np.unique(num_male_words)
unique_num_female = np.unique(num_female_words)
unique_num_genderless = np.unique(num_genderless_words)

plt.hist(num_male_words, bins=len(unique_num_male))
plt.savefig("figures/num_male_words.png")

plt.hist(num_female_words, bins=len(unique_num_female))
plt.savefig("figures/num_female_words.png")

plt.hist(num_genderless_words, bins=len(unique_num_genderless))
plt.savefig("figures/num_genderless_words.png")