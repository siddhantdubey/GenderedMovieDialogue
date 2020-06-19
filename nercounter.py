import matplotlib.pyplot as plt
import numpy as np

num_male_ner = 0
total_male = 0

num_female_ner = 0
total_female = 0

total_male_text = " "
total_female_text = " "

with open(r"data/male_ner.txt") as male:
    for line in male:
        line = line.strip()
        total_male_text += line 

with open(r"data/male_text.txt") as maletext:
    for line in maletext:
        line = line.strip()
        total_male += len(line)

with open(r"data/female_ner.txt") as fem:
    for line in fem:
        line = line.strip()
        total_female_text += line 

with open(r"data/female_text.txt") as female:
    for line in female:
        line = line.strip()
        total_female += len(line)

num_male_org = total_male_text.count("ORGANIZATION")
num_male_person = total_male_text.count("PERSON")
num_male_location = total_male_text.count("LOCATION")
num_male_facility = total_male_text.count("FACILITY")
num_male_gpe = total_male_text.count("GPE") 

num_male_ner = num_male_org + num_male_gpe + num_male_location + num_male_person + num_male_facility

num_female_org = total_female_text.count("ORGANIZATION")
num_female_person = total_female_text.count("PERSON")
num_female_location = total_female_text.count("LOCATION")
num_female_facility = total_female_text.count("FACILITY")
num_female_gpe = total_female_text.count("GPE") 

num_female_ner = num_female_org + num_female_gpe + num_female_location + num_female_person + num_female_facility


print(num_male_ner)
print(total_male)
print((num_male_ner/total_male) * 100)

print(num_female_ner)
print(total_female)
print((num_female_ner/total_female) * 100)


femners = [num_female_org, num_female_gpe, num_female_location, num_female_person, num_female_facility]

female_ners = [(num/total_female) * 100 for num in femners]

maleners = [num_male_org, num_male_gpe, num_male_location, num_male_person, num_male_facility]

male_ners = [(num/total_male) * 100 for num in maleners]

xlabels = ["ORGANIZATION", "GPE", "LOCATION", "PERSON", "FACILITY"]

x = np.arange(len(xlabels))

width = 0.35

fig, ax = plt.subplots()

rects1 = ax.bar(x - width/2, male_ners, width, label="Males")
rects2 = ax.bar(x + width/2, female_ners, width, label="Females")

ax.set_ylabel("Percentage of total number of words")
ax.set_title("Ratio of NER tags to total number of words by gender")
ax.set_xticks(x)
ax.set_xticklabels(xlabels)
ax.legend()

plt.savefig("figures/ner_tagged.png")

