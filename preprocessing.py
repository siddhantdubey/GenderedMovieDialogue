from nltk import pos_tag, RegexpParser, ne_chunk
from tokenize_words import word_sentence_tokenize

male_text = ""
female_text = ""
genderless_text = ""
i = 0
with open(r"data/collated_data.txt") as data:
    for line in data:
        line = line.strip()
        line_num, chr_id, movie_id, chr_name, chr_gender, line_text, credit_id = line.split("+++$+++")
        chr_gender = chr_gender[1:2]
        chr_gender.replace(' ', '')
        print(chr_gender)
        if(chr_gender.lower() == 'm'):
            male_text += line_text.strip() + '\n'
            print("Male categorized")
        elif(chr_gender.lower() == 'f'):
            female_text += line_text.strip() + "\n"
            print("Female Categorized")
        else:
            genderless_text += line_text.strip() + "\n"
            print("Genderless categorized")
        i += 1
        print(str(i) + " iterations of combining text done" + '\n')

with open(r"data/male_text.txt", "w+") as maletext:
    maletext.write(male_text)

with open(r"data/female_text.txt", "w+") as femaletext:
    femaletext.write(female_text)

with open(r"data/genderless_text.txt", "w+") as genderlesstext:
    genderlesstext.write(genderless_text)

# with open(r"data/combined_text.txt") as combinedtext:
#     for line in combinedtext:
#         text += line + '\n'

word_tokenized_male_text = word_sentence_tokenize(male_text) #this function is from tokenize_words.py, used to tokenize words.
word_tokenized_female_text = word_sentence_tokenize(female_text)
word_tokenized_genderless_text = word_sentence_tokenize(genderless_text)
print("Word Tokenization Done" + '\n')

pos_tagged_male_text = []
pos_tagged_female_text = []
pos_tagged_genderless_text = []

i = 0

with open(r"data/male_tagged.txt", "w+") as maletxt:
    for sentence in word_tokenized_male_text:
        tagged = pos_tag(sentence)
        pos_tagged_male_text.append(tagged)
        maletxt.write(str(tagged))
        maletxt.write("\n")
        i += 1
        print(str(i) + " iterations of pos tagging done" + "\n")

i = 0
with open(r"data/female_tagged.txt", "w+") as femaletxt:
    for sentence in word_tokenized_female_text:
        tagged = pos_tag(sentence)
        pos_tagged_female_text.append(tagged)
        femaletxt.write(str(tagged))
        femaletxt.write("\n")
        i += 1
        print(str(i) + " iterations of female pos tagging done" + "\n")

i = 0
with open(r"data/genderless_tagged.txt", "w+") as genderlesstxt:
    for sentence in word_tokenized_genderless_text:
        tagged = pos_tag(sentence)
        pos_tagged_genderless_text.append(tagged)
        genderlesstxt.write(str(tagged))
        genderlesstxt.write("\n")
        i += 1
        print(str(i) + " iterations of female pos tagging done" + "\n")

np_pattern = 'NP: {<DT>?<JJ>*<NN>}' #in case we want to use noun phrases in the future
cp = RegexpParser(np_pattern)

# final_text = [] #this section of code would find the noun phrases and append them, but we don't need that
# i = 0
# with open(r"data/np_tagged.txt", "w+") as nptxt:
#     for sentence in pos_tagged_text():
#         parsed_sentence = cp.parse(sentence)
#         final_text.append(parsed_sentence)
#         np.write(parsed_sentence + '\n')
#         i += 1
#         print(str(i) + " iterations of np parsing done" + "\n")


#The following code named entity recognition tags the text from the combined_text.txt file
ner_male = []
ner_female = []
ner_genderless = []

i = 0
with open(r"data/male_ner.txt", "w+") as maletxt:
    for sentence in pos_tagged_male_text:
        chunked_sentence = ne_chunk(sentence)
        ner_male.append(str(chunked_sentence))
        maletxt.write(str(chunked_sentence))
        maletxt.write("\n")
        i += 1
        print(str(i) + " iterations of male ner are done" + "\n")

i = 0
with open(r"data/female_ner.txt", "w+") as femtxt:
    for sentence in pos_tagged_female_text:
        chunked_sentence = ne_chunk(sentence)
        ner_female.append(str(chunked_sentence))
        femtxt.write(str(chunked_sentence))
        femtxt.write("\n")
        i += 1
        print(str(i) + " iterations of female ner are done" + "\n")

i = 0
with open(r"data/genderless_ner.txt", "w+") as unknown:
    for sentence in pos_tagged_genderless_text:
        chunked_sentence = ne_chunk(sentence)
        ner_genderless.append(str(chunked_sentence))
        unknown.write(str(chunked_sentence))
        unknown.write("\n")
        i += 1
        print(str(i) + " iterations of genderless ner are done" + "\n")