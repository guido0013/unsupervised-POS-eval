def to_brown(infile_train, infile_dev, infile_test, outfile, nr_lines=-1):

    snts_train = open(infile_train, encoding="utf-8")
    snts_dev = open(infile_dev, encoding="utf-8")
    snts_test = open(infile_test, encoding="utf-8")
    train = open("data/brown/train/"+outfile+".train", 'w+')
    dev = open("data/brown/dev/"+outfile+".dev", 'w+')
    test = open("data/brown/test/"+outfile+".test", 'w+')
    
    train_corpus = extract_snts_tags(snts_train, nr_lines)
    dev_corpus = extract_snts_tags(snts_dev, nr_lines)
    test_corpus = extract_snts_tags(snts_test, nr_lines)
    
    for sentence in train_corpus:
        snt = []
        for word_tag_list in sentence:
            snt.append(word_tag_list[0].lower())
        train.write(" ".join(snt)+'\n')


def to_clark(infile_train, infile_dev, infile_test, outfile, nr_lines=-1):

    snts_train = open(infile_train, encoding="utf-8")
    snts_dev = open(infile_dev, encoding="utf-8")
    snts_test = open(infile_test, encoding="utf-8")
    train = open("data/clark/train/"+outfile+".train", 'w+')
    dev = open("data/clark/dev/"+outfile+".dev", 'w+')
    test = open("data/clark/test/"+outfile+".test", 'w+')
    
    train_corpus = extract_snts_tags(snts_train, nr_lines)
    dev_corpus = extract_snts_tags(snts_dev, nr_lines)
    test_corpus = extract_snts_tags(snts_test, nr_lines)
    
    for sentence in train_corpus:
        snt = []
        for word_tag_list in sentence:
            train.write(word_tag_list[0].lower()+'\n')
        train.write('\n')
    
    
def extract_snts_tags(snts, nr_lines):
    if nr_lines == -1:
        corpus = []
        sentence = []
        for line in snts:
            if line != "\n":
                line = line.split('\t')
                if len(line) > 4:
                    sentence.append([line[i] for i in (1,3)])
            else: 
                corpus.append(sentence)
                sentence = []
            
    else: 
        corpus = []
        sentence = []
        for index in range(0, nr_lines):
            line = snts.readline()
            if line != "\n":
                line = line.split('\t')
                if line[0] != '#':
                    sentence.append([line[i] for i in (1,3)])
            else: 
                corpus.append(sentence)
                sentence = []
            index += 1
            
    return corpus
    
to_brown("ud-treebanks-v1.4/UD_Galician/gl-ud-train.conllu", "ud-treebanks-v1.4/UD_Galician/gl-ud-dev.conllu", "ud-treebanks-v1.4/UD_Galician/gl-ud-test.conllu","galician")   
to_brown("ud-treebanks-v1.4/UD_Dutch/nl-ud-train.conllu", "ud-treebanks-v1.4/UD_Dutch/nl-ud-dev.conllu", "ud-treebanks-v1.4/UD_Dutch/nl-ud-test.conllu","dutch")  
to_clark("ud-treebanks-v1.4/UD_Dutch/nl-ud-train.conllu", "ud-treebanks-v1.4/UD_Dutch/nl-ud-dev.conllu", "ud-treebanks-v1.4/UD_Dutch/nl-ud-test.conllu","dutch")   

