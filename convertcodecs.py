import codecs

BLOCKSIZE = 1048576 

with codecs.open('data/training_set.txt', "r", "charmap") as train: 
    with codecs.open('data/good_training_set.txt', "w+", "charmap") as newtrain:
        while True:
            contents = train.read(BLOCKSIZE)
            if not contents:
                break
            newtrain.write(contents)

with codecs.open('data/test_set.txt', "r", "charmap") as test: 
    with codecs.open('data/good_test_set.txt', "w+", "charmap") as newtest:
        while True:
            contents = test.read(BLOCKSIZE)
            if not contents:
                break
            newtest.write(contents)