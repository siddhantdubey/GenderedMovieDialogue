from matplotlib import pyplot as plt
import numpy as np

num_male_words = []
num_female_words = []
num_genderless_words = []

with open(r"data/male_text.txt") as male:
    male_num = 0
    male_total = 0
    for line in male:
        line = line.strip()
        words = line.split()
        length = len(words)
        num_male_words.append(length)
        male_total += length
        male_num += 1
    male_avg = (male_total/male_num)

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
    genderless_avg = (gender_total/gender_num)



num_male_words = np.array(num_male_words)
num_female_words = np.array(num_female_words)
num_genderless_words = np.array(num_genderless_words)

unique_num_male = np.unique(num_male_words)
unique_num_female = np.unique(num_female_words)
unique_num_genderless = np.unique(num_genderless_words)

plt.xlim(0,100)
plt.title('Distribution of Words in Utterances Spoken by Male Characters')
plt.xlabel('Number of Words')
plt.ylabel('Frequency')
plt.axvline(num_male_words.mean(), color='k', linestyle='dashed', linewidth=1)
plt.hist(num_male_words, bins=200)
plt.savefig("figures/num_male_words.png")
plt.close()

plt.xlim(0,100)
plt.title('Distribution of Words in Utterances Spoken by Female Characters')
plt.xlabel('Number of Words')
plt.ylabel('Frequency')
plt.axvline(num_female_words.mean(), color='k', linestyle='dashed', linewidth=1)
plt.hist(num_female_words, bins=100)
plt.savefig("figures/num_female_words.png")
plt.close()

plt.xlim(0,100)
plt.title('Distribution of Words in Utterances Spoken by Genderless Characters')
plt.xlabel('Number of Words')
plt.ylabel('Frequency')
plt.axvline(num_genderless_words.mean(), color='k', linestyle='dashed', linewidth=1)
plt.hist(num_genderless_words, bins=100)
plt.savefig("figures/num_genderless_words.png")
plt.close()

n_bins = 50
fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False)
plt.suptitle('Distribution of Words in Utterances Spoken by Characters')
axs[0].set_xlim([0,100])
axs[1].set_xlim([0,100])
axs[2].set_xlim([0,100])
axs[0].set_xlabel('# of Words')
axs[1].set_xlabel('# of Words')
axs[2].set_xlabel('# of Words')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Male')
axs[1].set_title('Female')
axs[2].set_title('Genderless')
axs[0].axvline(num_male_words.mean(), color='k', linestyle='dashed', linewidth=1)
axs[1].axvline(num_female_words.mean(), color='k', linestyle='dashed', linewidth=1)
axs[2].axvline(num_genderless_words.mean(), color='k', linestyle='dashed', linewidth=1)
axs[0].hist(num_male_words, bins= n_bins)
axs[1].hist(num_female_words, bins = n_bins)
axs[2].hist(num_genderless_words, bins = n_bins)
plt.savefig("figures/combined_num_plots.png")
plt.close()

print('The average number of words in an utterance spoken by a male character is %.5f' % male_avg)
print('The average number of words in an utterance spoken by a female character is %.5f' % fem_avg)
print('The average number of words in an utterance spoken by a genderless character is %.5f' % genderless_avg)