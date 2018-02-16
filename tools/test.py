import spacy
import numpy as np
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize as nltk_tokenizer

nlp = spacy.load('en_core_web_md')

def plot_from_file_using_numpy():
    x, y = np.loadtxt('example.txt', delimiter=',', unpack=True) # unpack attribute
                                                                #  unpacks the returned list in variable x and y
    plt.plot(x, y, label='File Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Loading File Data using Numpy')
    plt.legend()
    plt.show()


def tokenize():
    spacy_nlp = spacy.load('en_core_web_md')
    spacy_tokenizer = spacy_nlp.tokenizer
    tokens = spacy_tokenizer('[aux I am nsubj]]')
    print(tokens)
    print(len(tokens))

def plot_cnnlstm():
    step, time, pco, mse = np.loadtxt('/scratch/experiments/QUORA_CNN_LSTM/val_results/val_history.txt', delimiter='\t', unpack=True)



if  __name__ == '__main__':
    tokenize()
