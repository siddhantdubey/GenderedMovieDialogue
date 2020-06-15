# Open collated_data.txt
with open(r'data/collated_data.txt') as cdata:
    big_list2 = [] # New big_list to store sublists containing values
    chr_list = [] # List to contain all of the character ids
    chr_gender = {} # Dictionary where the keys are the character ids and the values are the corresponding gender
    for line in cdata: # Iterate through every line in the file
        line = line.strip() # Remove newline character from each line
        line_num, chr_id, movie_id, chr_name, gender, line_txt = line.split('+++$+++') # Split each line at the delimiter and store values in corresponding variables
        line_list = [line_num, chr_id, movie_id, chr_name, gender, line_txt] # Store values in a list
        chr_id, gender = chr_id.replace(' ',''), gender.replace(' ','') # Remove spaces from values
        chr_gender[chr_id] = gender # Add character id and corresponding gender to dictionary
        chr_list.append(chr_id) # Add user id to list
        big_list2.append(line_list) # Add sublist of values to big list
mc1, fc1, uc1 = 0, 0, 0 # Intialize counts for the number of characters of each gender
mc2, fc2, uc2 = 0, 0, 0 # Intialize counts for the number of lines from each gender
chr_list = list(set(chr_list)) # Remove duplicate character ids from the list

for j in range(len(chr_list)): # Iterate through every character id
    gender = chr_gender[chr_list[j]] # Retrieve the gender corresponding to a character id
    # Check if the gender is Male, Female, or Unknown and add to corresponding counts
    if gender == 'm' or gender == 'M':
        mc1 += 1
    elif gender == 'f' or gender == 'F':
        fc1 += 1
    elif gender == '?':
        uc1 += 1
for i in range(len(big_list2)): # Iterate thorugh every sublist
    gender  = (big_list2[i][4]).replace(' ','') # Retrieve the gender from the sublist and remove spaces
    # Check if the gender is Male, Female, or Unknown and add to corresponding counts
    if gender == 'm' or gender == 'M':
        mc2 += 1
    elif gender == 'f' or gender == 'F':
        fc2 += 1
    elif gender == '?':
        uc2 += 1

# Outputs
print('The number of male characters is %d' % mc1)
print('The number of instances of male speech is %d' % mc2)
print('The number of female characters is %d' % fc1)
print('The number of instances of female speech is %d' % fc2)
print('The number of characters of unknown gender is %d' % uc1)
print('The number of instances of speech from a character of unknwn gender is %d' % uc2)