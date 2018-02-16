from gensim.models import Word2Vec
import nltk

sentence_list = []

def create_sentencelist():

    text = open("/home/tanvi/dataset/quora/train/train.txt").read()
    lines = text.split('\n')
    new_lines = ""
    for line in lines:
        line_split = line.split('\t')
        if (len(line_split) == 3):
            sent1 = line_split[0]
            sent2 = line_split[1]
            tokenize(sent1)
            tokenize(sent2)


def tokenize(sentence):
    words = nltk.word_tokenize(sentence)
    sentence_list.append(words)



def train_Word2Vec():
    create_sentencelist()
    print(len(sentence_list))
    print(sentence_list)
    model = Word2Vec(sentence_list, min_count=10, size=300)
    model.save('model10-300.bin')
    # summarize the loaded model
    print(model)
    # summarize vocabulary
    words = list(model.wv.vocab)
    print(words)
    # access vector for one word
    print(model['is'])
    print(len(model['swallow']))



if __name__ == '__main__':
    train_Word2Vec()
