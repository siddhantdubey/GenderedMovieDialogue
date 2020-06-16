from nltk import pos_tag, RegexpParser, ne_chunk
from tokenize_words import word_sentence_tokenize

text = ""
i = 0
with open(r"data/collated_data.txt") as data:
    for line in data:
        line = line.strip()
        line_num, chr_id, movie_id, chr_name, chr_gender, line_text, credit_id = line.split("+++$+++")
        text += line_text.strip() + '\n'
        i += 1
        print(str(i) + " iterations of combining text done" + '\n')

with open(r"data/combined_text.txt", "w+") as combinedtext:
    combinedtext.write(text) 
# with open(r"data/combined_text.txt") as combinedtext:
#     for line in combinedtext:
#         text += line + '\n'

word_tokenized_text = word_sentence_tokenize(text) #this function is from tokenize_words.py, used to tokenize words.
print("Word Tokenization Done" + '\n')
pos_tagged_text = []
i = 0
with open(r"data/pos_tagged.txt", "w+") as postxt:
    for sentence in word_tokenized_text:
        pos_tagged_text.append(pos_tag(sentence))
        postxt.write(str(pos_tag(sentence)))
        postxt.write("\n")
        i += 1
        print(str(i) + " iterations of pos tagging done" + "\n")


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
ner_text = []
i = 0
with open(r"data/processed.txt", "w+") as processed:
    for sentence in pos_tagged_text:
        chunked_sentence = ne_chunk(sentence)
        ner_text.append(str(chunked_sentence))
        processed.write(str(chunked_sentence))
        processed.write("\n")
        i += 1
        print(str(i) + " iterations of ner are done" + "\n")