import json
import requests
import urllib
import os
from PIL import Image

id = 'a8f1135d-2f2e-49cc-b75b-8350ebc932d2'
acc_key = 's/25c2KSc6Y0lLSPzmjdGm0ZgKA2caIkS7iEJEIf4m8'

def process_word(word, n_img=1):
    data = bing_request(word)
    # if n_img == 1:
    i_url = data['d']['results'][0]['Image'][2]['MediaUrl']
    # print json.dumps(i_url,indent=4, separators=(',', ': '))
    save_img_url(i_url, word)


def bing_request(word):
    json_fname = 'json/' + word + '.json'
    if os.path.exists(json_fname):
        print("File " + json_fname + " exists")
        with open(json_fname) as data_file:
            data = json.load(data_file)
            return data
    else:
        print "Sending request for " + word
        data = requests.get(
            'https://api.datamarket.azure.com/Bing/Search/v1/Composite?Sources=%27image%27&Query=%27' + word + '%27&ImageFilters=%27Size%3AMedium%27&$format=json',
            auth=(id, acc_key)).json()
        # print(data)
        save_json_query(word, data)
        return data


def save_json_query(word, data):
    with open('json/' + word + '.json', 'w') as f:
        json.dump(data, f)


def save_img_url(url, word):
    # url_split = url.split(".")
    # extension = url_split[len(url_split) - 1]
    img_fname = "img/" + word + ".jpg"
    if os.path.exists(img_fname):
        # return
        os.remove(img_fname)
    try:
        resource = urllib.urlopen(url)
    except:
        print("Failed to get image for " + word)
        return
    output = open(img_fname, "wb")
    output.write(resource.read())
    output.close()


def process_words(filename):
    with open(filename) as fp:
        for line in fp:
            process_word(line.strip().lower())


if __name__ == '__main__':
    process_words('../data/words_redo.txt')
