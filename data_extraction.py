def to_brown(infile_train, infile_dev, infile_test, outfile, nr_snts=-1):

    snts_train = open(infile_train, encoding="utf-8")
    snts_dev = open(infile_dev, encoding="utf-8")
    snts_test = open(infile_test, encoding="utf-8")
    train = open("data/brown/"+outfile+".brown", 'w+')
    
    train_corpus = extract_snts_tags(snts_train)
    dev_corpus = extract_snts_tags(snts_dev)
    test_corpus = extract_snts_tags(snts_test)
    
    corpus = train_corpus + dev_corpus + test_corpus
    
    if nr_snts == -1 or nr_snts >= len(corpus):
        for sentence in corpus:
            snt = []
            for word_tag_list in sentence:
                snt.append(word_tag_list[0].lower())
            train.write(" ".join(snt)+'\n')
    else:
        for i in range(0, nr_snts):
            sentence = corpus[i]
            snt = []
            for word_tag_list in sentence:
                snt.append(word_tag_list[0].lower())
            train.write(" ".join(snt)+'\n')
            
    snts_train.close()
    snts_dev.close()
    snts_test.close()
    train.close()


def to_clark(infile_train, infile_dev, infile_test, outfile, nr_snts=-1):

    snts_train = open(infile_train, encoding="utf-8")
    snts_dev = open(infile_dev, encoding="utf-8")
    snts_test = open(infile_test, encoding="utf-8")
    train = open("data/clark/"+outfile+".clark", 'w+')
    
    train_corpus = extract_snts_tags(snts_train)
    dev_corpus = extract_snts_tags(snts_dev)
    test_corpus = extract_snts_tags(snts_test)
    
    corpus = train_corpus + dev_corpus + test_corpus
    
    if nr_snts == -1 or nr_snts >= len(corpus):
        for sentence in corpus:
            for word_tag_list in sentence:
                train.write(word_tag_list[0].lower()+'\n')
            train.write('\n')
    else:
    
        for i in range(0, nr_snts):
            sentence = corpus[i]
            for word_tag_list in sentence:
                train.write(word_tag_list[0].lower()+'\n')
            train.write('\n')
    
    snts_train.close()
    snts_dev.close()
    snts_test.close()
    train.close()
    
    
def extract_snts_tags(snts):
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
            
    return corpus
    
    
def extract_gold_tags(infile_train, infile_dev, infile_test, outfile, nr_snts=-1):
    snts_train = open(infile_train, encoding="utf-8")
    snts_dev = open(infile_dev, encoding="utf-8")
    snts_test = open(infile_test, encoding="utf-8")
    gold = open("gold_tags/"+outfile+".gold", 'w+')
    
    train_corpus = extract_snts_tags(snts_train)
    dev_corpus = extract_snts_tags(snts_dev)
    test_corpus = extract_snts_tags(snts_test)
    
    corpus = train_corpus + dev_corpus + test_corpus
    
    if nr_snts == -1 or nr_snts >= len(corpus):
        for sentence in corpus:
            for word_tag_list in sentence:
                gold.write(word_tag_list[0].lower()+'\t'+word_tag_list[1]+'\n')
    else:
    
        for i in range(0, nr_snts):
            sentence = corpus[i]
            for word_tag_list in sentence:
                gold.write(word_tag_list[0].lower()+'\t'+word_tag_list[1]+'\n')
    
    snts_train.close()
    snts_dev.close()
    snts_test.close()
    gold.close()

    
to_brown("ud-treebanks-v1.4/UD_Galician/gl-ud-train.conllu", "ud-treebanks-v1.4/UD_Galician/gl-ud-dev.conllu", "ud-treebanks-v1.4/UD_Galician/gl-ud-test.conllu","galician")   
to_brown("ud-treebanks-v1.4/UD_Dutch/nl-ud-train.conllu", "ud-treebanks-v1.4/UD_Dutch/nl-ud-dev.conllu", "ud-treebanks-v1.4/UD_Dutch/nl-ud-test.conllu","dutch")  
to_clark("ud-treebanks-v1.4/UD_Galician/gl-ud-train.conllu", "ud-treebanks-v1.4/UD_Galician/gl-ud-dev.conllu", "ud-treebanks-v1.4/UD_Galician/gl-ud-test.conllu","galician")  
to_clark("ud-treebanks-v1.4/UD_Dutch/nl-ud-train.conllu", "ud-treebanks-v1.4/UD_Dutch/nl-ud-dev.conllu", "ud-treebanks-v1.4/UD_Dutch/nl-ud-test.conllu","dutch")  
extract_gold_tags("ud-treebanks-v1.4/UD_Galician/gl-ud-train.conllu", "ud-treebanks-v1.4/UD_Galician/gl-ud-dev.conllu", "ud-treebanks-v1.4/UD_Galician/gl-ud-test.conllu","galician")
extract_gold_tags("ud-treebanks-v1.4/UD_Dutch/nl-ud-train.conllu", "ud-treebanks-v1.4/UD_Dutch/nl-ud-dev.conllu", "ud-treebanks-v1.4/UD_Dutch/nl-ud-test.conllu","dutch")  

