from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

num_male_neg = 0
num_male_neu = 0
num_male_pos = 0

num_female_neg = 0
num_female_neu = 0
num_female_pos = 0

num_gl_neg = 0
num_gl_neu = 0
num_gl_pos = 0

sid = SentimentIntensityAnalyzer()

with open(r'data/male_text.txt') as male:
    for line in male:
        ss = sid.polarity_scores(line)
        if(ss["compound"] > 0.45):
            num_male_pos += 1
        elif(ss["compound"] < -0.45):
            num_male_neg += 1
        else:
            num_male_neu += 1


with open(r'data/female_text.txt') as female:
    for line in female:
        ss = sid.polarity_scores(line)
        if(ss["compound"] > 0.45):
            num_female_pos += 1
        elif(ss["compound"] < -0.45):
            num_female_neg += 1
        else:
            num_female_neu += 1

with open(r'data/genderless_text.txt') as genderless:
    for line in genderless:
        ss = sid.polarity_scores(line)
        if(ss["compound"] > 0.3):
            num_gl_pos += 1
        elif(ss["compound"] < -0.3):
            num_gl_neg += 1
        else:
            num_gl_neu += 1

xlabels = ["pos", "neg", "neu"]

male_y = [num_male_pos, num_male_neg, num_male_neu]
female_y = [num_female_pos, num_female_neg, num_female_neu]
gl_y = [num_gl_pos, num_gl_neg, num_gl_neu]

width = 0.3
plt.figure(figsize=(20,4))
plt.title('Frequency of Sentiment in Utterances spoken by Male Characters')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.bar(xlabels, male_y, width, align='edge', color = 'g')
plt.xticks(rotation=90)
plt.savefig('figures/male_sentiment.png')
plt.close()

width = 0.3
plt.figure(figsize=(20,4))
plt.title('Frequency of Sentiment in Utterances spoken by Female Characters')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.bar(xlabels, female_y, width, align='edge', color = 'g')
plt.xticks(rotation=90)
plt.savefig('figures/female_sentiment.png')
plt.close()

width = 0.3
plt.figure(figsize=(20,4))
plt.title('Frequency of Sentiment in Utterances spoken by Characters with Unknown gender')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.bar(xlabels, male_y, width, align='edge', color = 'g')
plt.xticks(rotation=90)
plt.savefig('figures/gl_sentiment.png')
plt.close()