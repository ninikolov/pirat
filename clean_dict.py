import nltk
import enchant

if __name__ == '__main__':
    d = enchant.Dict("en_US")
    with open('data/phonemeDB.txt') as source:
        with open('data/phonemeDB_clean.txt', 'a') as target:
            for line in source:
                word = line.split("\t")[0].strip().lower()
                # tag = nltk.tag.pos_tag([word])[0][1]
                if d.check(word):
                    target.write(line)

    source.close()
    target.close()
