import nltk


if __name__ == '__main__':
    with open('data/phonemeDB.txt') as source:
        with open('data/phonemeDB_clean.txt', 'a') as target:
            for line in source:
                tag = nltk.tag.pos_tag([line.split("\t")[0]])[0][1]
                if tag == 'NN':
                    target.write(line)

    source.close()
    target.close()
