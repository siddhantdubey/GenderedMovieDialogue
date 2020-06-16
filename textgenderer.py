with open("data/combined_text.txt") as text:
    with open("data/collated_data.txt") as data:
        for i in range(len(text.readlines())):
            print(text.readline())
