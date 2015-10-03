import nltk
import enchant
import json

def clean_phoneme_dict():
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
                    # if nltk.tag.pos_tag([word])[0][1] == 'NN' or word in top_nouns:
                    target.write(line)

    source.close()
    target.close()

def generate_json_from_snitch(file="data/snitch.txt"):
    with open(file) as f:
        root = {}
        ind = 0
        for line in f:
            elements = line.lower().strip().split(">")
            root[ind] = {"TRUE" : elements[0]}
            for i in range(1, len(elements)):
                root[ind][i] = {"PIC": elements[i] + ".jpg"}
            ind += 1
    final = json.dumps(root, sort_keys=True,indent=4, separators=(',', ': '))
    # print(final)
    text_file = open("data/snitch.json", "w")
    text_file.write(final)
    text_file.close()

if __name__ == '__main__':
    generate_json_from_snitch()
