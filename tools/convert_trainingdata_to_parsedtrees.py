import spacy
import parse_data_to_dependencytrees


if __name__=='__main__':
    nlp = spacy.load('en_core_web_md')

    text = open('/home/tanvi/envs/thesis/quora/train/train.txt').read()
    lines = text.split('\n')
    new_lines = ""
    for line in lines:
        line_split = line.split('\t')
        if(len(line_split) == 3):
            sent1 = nlp(line_split[0])
            sent2 = nlp(line_split[1])
            label = line_split[2]
            parsed_sent1 = parse_data_to_dependencytrees.parse(sent1)
            parsed_sent2 = parse_data_to_dependencytrees.parse(sent2)
            new_line = str(parsed_sent1) + '\t' + str(parsed_sent2) + '\t' + str(label) + '\n'
            new_lines  = new_lines + new_line

    print(len(lines))
    print("New lines length")
    print(len(new_lines))

    with open('/home/tanvi/envs/thesis/quora/train/dep_train.txt', 'w') as parsed_file:
        parsed_file.write(new_lines)

