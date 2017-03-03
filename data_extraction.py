def extract_from_treebank(corpus_name, abbrev, language, nr_words=-1):
    #to_brown("ud-treebanks-v1.4/UD_"+corpus_name+"/"+abbrev+"-ud-train.conllu", "ud-treebanks-v1.4/UD_"+corpus_name+"/"+abbrev+"-ud-dev.conllu", "ud-treebanks-v1.4/UD_"+corpus_name+"/"+abbrev+"-ud-test.conllu",language, nr_words)
    
    #to_clark("ud-treebanks-v1.4/UD_"+corpus_name+"/"+abbrev+"-ud-train.conllu", "ud-treebanks-v1.4/UD_"+corpus_name+"/"+abbrev+"-ud-dev.conllu", "ud-treebanks-v1.4/UD_"+corpus_name+"/"+abbrev+"-ud-test.conllu",language, nr_words)
    
    #extract_gold_tags("ud-treebanks-v1.4/UD_"+corpus_name+"/"+abbrev+"-ud-train.conllu", "ud-treebanks-v1.4/UD_"+corpus_name+"/"+abbrev+"-ud-dev.conllu", "ud-treebanks-v1.4/UD_"+corpus_name+"/"+abbrev+"-ud-test.conllu", language+".gold", nr_words) 
    
    extract_gold_tags2("ud-treebanks-v1.4/UD_"+corpus_name+"/"+abbrev+"-ud-train.conllu", "ud-treebanks-v1.4/UD_"+corpus_name+"/"+abbrev+"-ud-dev.conllu", "ud-treebanks-v1.4/UD_"+corpus_name+"/"+abbrev+"-ud-test.conllu", language+".gold", nr_words) 
    

def to_brown(infile_train, infile_dev, infile_test, language, nr_words):

    snts_train = open(infile_train, encoding="utf-8")
    snts_dev = open(infile_dev, encoding="utf-8")
    snts_test = open(infile_test, encoding="utf-8")
    train = open("data/brown/"+language, 'w+')
    
    train_corpus = extract_snts_tags(snts_train)
    dev_corpus = extract_snts_tags(snts_dev)
    test_corpus = extract_snts_tags(snts_test)
    
    corpus = train_corpus + dev_corpus + test_corpus
    
    if nr_words == -1:
        for sentence in corpus:
            snt = []
            for word_tag_list in sentence:
                snt.append(word_tag_list[0].lower())
            train.write(" ".join(snt)+'\n')
    else:
        i = 0
        snt_index = 0
        while i < nr_words and snt_index < len(corpus):
            sentence = corpus[snt_index]
            i += len(sentence)
            snt = []
            for word_tag_list in sentence:
                snt.append(word_tag_list[0].lower())
            train.write(" ".join(snt)+'\n')
            
            snt_index += 1
        
    snts_train.close()
    snts_dev.close()
    snts_test.close()
    train.close()


def to_clark(infile_train, infile_dev, infile_test, language, nr_words=-1):

    snts_train = open(infile_train, encoding="utf-8")
    snts_dev = open(infile_dev, encoding="utf-8")
    snts_test = open(infile_test, encoding="utf-8")
    train = open("data/clark/"+language, 'w+')
    
    train_corpus = extract_snts_tags(snts_train)
    dev_corpus = extract_snts_tags(snts_dev)
    test_corpus = extract_snts_tags(snts_test)
    
    corpus = train_corpus + dev_corpus + test_corpus
    
    if nr_words == -1:
        for sentence in corpus:
            for word_tag_list in sentence:
                train.write(word_tag_list[0].upper()+'\n')
            train.write('\n')
    else:
    
        i = 0
        snt_index = 0
        
        while i < nr_words and snt_index < len(corpus):
        
            sentence = corpus[snt_index]
            
            i += len(sentence)
            
            for word_tag_list in sentence:
                train.write(word_tag_list[0].upper()+'\n')
            train.write('\n')
            
            snt_index += 1
    
    snts_train.close()
    snts_dev.close()
    snts_test.close()
    train.close()
    
    
def to_bmmm(infile_train, infile_dev, infile_test, outfile, nr_snts=-1):
    pass
    
    
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
    
    
def extract_gold_tags(infile_train, infile_dev, infile_test, language, nr_words):
    snts_train = open(infile_train, encoding="utf-8")
    snts_dev = open(infile_dev, encoding="utf-8")
    snts_test = open(infile_test, encoding="utf-8")
    gold = open("gold_tags/"+language, 'w+')
    
    train_corpus = extract_snts_tags(snts_train)
    dev_corpus = extract_snts_tags(snts_dev)
    test_corpus = extract_snts_tags(snts_test)
    
    corpus = train_corpus + dev_corpus + test_corpus
    
    if nr_words == -1:
        for sentence in corpus:
            for word_tag_list in sentence:
                gold.write(word_tag_list[0].lower()+'/'+word_tag_list[1] + ' ')
            gold.write('\n')
    else:
    
        i = 0
        snt_index = 0
        
        while i < nr_words and snt_index < len(corpus):
        
            sentence = corpus[snt_index]
            
            i += len(sentence)
            for word_tag_list in sentence:
                gold.write(word_tag_list[0].lower()+'/'+word_tag_list[1] + ' ')
            gold.write('\n')
            
                
            snt_index += 1
    
    snts_train.close()
    snts_dev.close()
    snts_test.close()
    gold.close()
    
def extract_gold_tags2(infile_train, infile_dev, infile_test, language, nr_words):
    snts_train = open(infile_train, encoding="utf-8")
    snts_dev = open(infile_dev, encoding="utf-8")
    snts_test = open(infile_test, encoding="utf-8")
    gold = open("gold_tags2/"+language, 'w+')
    
    train_corpus = extract_snts_tags(snts_train)
    dev_corpus = extract_snts_tags(snts_dev)
    test_corpus = extract_snts_tags(snts_test)
    
    corpus = train_corpus + dev_corpus + test_corpus
    
    if nr_words == -1:
        for sentence in corpus:
            for word_tag_list in sentence:
                gold.write(word_tag_list[0].lower()+ '\t' +word_tag_list[1] + '\n')
    else:
    
        i = 0
        snt_index = 0
        
        while i < nr_words and snt_index < len(corpus):
        
            sentence = corpus[snt_index]
            
            i += len(sentence)
            for word_tag_list in sentence:
                gold.write(word_tag_list[0].lower()+ '\t' +word_tag_list[1] + '\n')
            
                
            snt_index += 1
    
    snts_train.close()
    snts_dev.close()
    snts_test.close()
    gold.close()
    

    
extract_from_treebank("Czech", "cs", "czech.200k", 200000)
extract_from_treebank("Arabic", "ar", "arabic.200k", 200000)
extract_from_treebank("English", "en", "english.200k", 200000)
extract_from_treebank("French", "fr", "french.200k", 200000)
extract_from_treebank("Catalan", "ca", "catalan.200k", 200000)
extract_from_treebank("Hindi", "hi", "hindi.200k", 200000)
extract_from_treebank("German", "de", "german.200k", 200000)
extract_from_treebank("Latin-ITTB", "la_ittb", "latin.200k", 200000)
extract_from_treebank("Norwegian", "no", "norwegian.200k", 200000)
extract_from_treebank("Portuguese", "pt", "portuguese.200k", 200000)
extract_from_treebank("Portuguese-BR", "pt_br", "portuguese_br.200k", 200000)
extract_from_treebank("Romanian", "ro", "romanian.200k", 200000)
extract_from_treebank("Spanish", "es", "spanish.200k", 200000)
extract_from_treebank("Russian-SynTagRus", "ru_syntagrus", "russian.200k", 200000)



