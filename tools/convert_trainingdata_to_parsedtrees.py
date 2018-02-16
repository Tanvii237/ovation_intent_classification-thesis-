import os
import spacy
import parse_data_to_dependencytrees
from random import randint



def create_parsed_data():
    nlp = spacy.load('en_core_web_md')

    text = open("/home/tanvi/dataset/quora/test/test.txt").read()
    lines = text.split('\n')
    new_lines = ""
    for line in lines:
        line_split = line.split('\t')
        if (len(line_split) == 3):
            sent1 = nlp(line_split[0])
            sent2 = nlp(line_split[1])
            label = line_split[2]
            parsed_sent1 = parse_data_to_dependencytrees.parse(sent1)
            parsed_sent2 = parse_data_to_dependencytrees.parse(sent2)
            #new_line = str(parsed_sent1) + '\t' + str(parsed_sent2) + '\t' + str(label) + '\n'
            new_line = ' '.join(parsed_sent1) + '\t' + ' '.join(parsed_sent2) + '\t' + str(label) + '\n'
            new_lines = new_lines + new_line

    print(len(lines))
    print("New lines length")
    print(len(new_lines.split('\n')))

    with open('/home/tanvi/dataset/quora/test/dep_test.txt', 'w') as parsed_file:
        parsed_file.write(new_lines)


def update_vocab():
    with open('/home/tanvi/dataset/quora/dependency_labels.txt', 'r') as deplabels_file:
        dep_labels_list = deplabels_file.read().split('\n')
        print(dep_labels_list)
        print(len(dep_labels_list))
    # adding [ ] in label list
    dep_labels_list.append('[')
    dep_labels_list.append(']')
    print(len(dep_labels_list))
    with open('/home/tanvi/dataset/quora/vocab.txt', 'r') as vocablist:
        vocab_list = vocablist.read().split('\n')
        print(vocab_list[:50])
    # making dictionary of vocab list
    vocab_dict = dict(x.split('\t') for x in vocab_list)
    print(len(vocab_dict.keys()))
    print("vocablist")
    print(len(vocab_list))

    # add new vocab in vocab dictionary
    count = 0
    for label in dep_labels_list:
        print(label)
        if (label not in vocab_dict.keys()):
            vocab_dict.update({label: randint(10, 50)})
        else:
            print('E    ' + label + '\t' + vocab_dict.get(label))
            count = count + 1
    print(count)
    print("updated vocab")
    print(len(vocab_dict.keys()))
    # print(randint(0, 9))


    # updatevocab
    # vacab_str = ''
    # for k, v in vocab_dict.items(): vacab_str = vacab_str + k + '\t' + str(v) + '\n'
    # print(vacab_str)
    with open('/home/tanvi/dataset/quora/vocab.txt', "a") as myfile:
        for k, v in vocab_dict.items():
            line = k + '\t' + str(v) + '\n'
            myfile.write(line)


if __name__=='__main__':
    create_parsed_data()


