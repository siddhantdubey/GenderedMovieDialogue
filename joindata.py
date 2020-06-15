# Open movie_lines.txt

with open(r'data/movie_lines.txt') as movie_lines:
    big_list = [] # List to store sublists containing data from each line
    for line in movie_lines: #iterate through the lines in the text file
        line = line.strip() #remove newline character
        line_num, chr_id, movie_id, chr_name, line_txt = line.split('+++$+++')
        line_list = [line_num, chr_id, movie_id, chr_name,0, line_txt]
        for i in range(1):
            e = str(line_list[i])
            e = e.replace(' ','')        
        big_list.append(line_list) #add the sublist of values to the big_list, which is to be added to the new combined data text file

#The following loop creates a dictionary named user_gender, where the keys are the character ids and the values are the genders. 
with open(r'data/movie_characters_metadata.txt') as chr_data:
    user_gender = {}
    for line in chr_data:
        line = line.strip()
        chr_id, name, movie_id, movie_name, gender, credit_order = line.split('+++$+++')
        chr_id = chr_id.replace(' ','')
        gender = gender.replace(' ','')
        gender = ' ' + gender
        user_gender[chr_id] = gender

#Loop through the the sublists in big_list
for i in range(len(big_list)): 
    big_list[i][4] = user_gender[big_list[i][1].replace(' ','')] #Replace the zero in the sublist with the correct gender 

#Create a new file collated_data.txt if it doesn't exist.Else open it to write to.
with open(r'data/collated_data.txt','w+') as fout:
    #Loop through each sublist in big list
    for i in range(len(big_list)):
        line = '' #Empty string stores the values in each line.
        for j in range(len(big_list[i])):
            line += big_list[i][j] + ' +++$+++' #Add values seperated by a delimiter
        line = line.strip('+++$+++') #Gets rid of the extra delimiter that is added to the end of the line
        fout.write(line)
        fout.write('\n') #write a new line after you write the line to the file to allow for readability and usability of data.
