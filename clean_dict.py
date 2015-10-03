import nltk
import enchant

if __name__ == '__main__':
    top_nouns = []
    with open('data/top_nouns.txt') as t_n:
        for line in t_n:
            top_nouns.append(line.split("\t")[0].lower().strip())
    print(top_nouns)
    d = enchant.Dict("en_US")
    with open('data/phonemeDB.txt') as source:
        with open('data/phonemeDB_clean.txt', 'a') as target:
            for line in source:
                word = line.split("\t")[0].strip().lower()
                tag = nltk.tag.pos_tag([word])[0][1]
                if d.check(word):
                    if nltk.tag.pos_tag([word])[0][1] == 'NN' or word in top_nouns:
                        target.write(line)

    source.close()
    target.close()
