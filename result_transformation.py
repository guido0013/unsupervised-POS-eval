def result_transformation(languages):
    for language in languages:
        print(language)
        #brown_to_eval(language)
        #clark_to_eval(language, "d")
        #clark_to_eval(language, "dm")
        clark_to_eval(language, "dfm")
        #typetagger_to_eval(language, 1)
        #typetagger_to_eval(language, 2)
        #typetagger_to_eval(language, 3)

def brown_to_eval(language):
    results_file = open("results/brown/res_" + language, encoding="utf-8")
    
    words_clusters = {}
    cluster_int_mapping = {}
    i = 0
    
    for line in results_file:
        line = line.split()
          
        if line[0] in cluster_int_mapping:
            words_clusters[line[1]] = cluster_int_mapping[line[0]]
        else:
            cluster_int_mapping[line[0]] = i
            words_clusters[line[1]] = cluster_int_mapping[line[0]]    
            i += 1
        
    results_file.close()
    
    mod_file = open("results/brown/mod_res_" + language, 'w+', encoding="utf-8")
    brown_file = open("data/brown/" + language, encoding="utf-8")
    
    for sentence in brown_file:
        sentence = sentence.split()
        snt_tag = []
        for word in sentence:
            snt_tag.append(word + '/' + str(words_clusters[word]))
            
        mod_file.write(" ".join(snt_tag) + '\n')
        
    mod_file.close()
    brown_file.close()
  

def clark_to_eval(language, model):
    results_file = open("results/clark/"+model+"/res_" + language, encoding="utf-8")
    
    words_clusters = {}
    
    for line in results_file:
        line = line.split()
          
        words_clusters[line[0].lower()] = line[1]
        
    results_file.close()
    
    mod_file = open("results/clark/"+model+"/mod_res_" + language, 'w+', encoding="utf-8")
    brown_file = open("data/brown/" + language, encoding="utf-8")
    
    for sentence in brown_file:
        sentence = sentence.split()
        snt_tag = []
        for word in sentence:
            if "ß" in word:
                word2 = word.replace("ß", "ss")
                snt_tag.append(word + '/' + str(words_clusters[word2]))
            elif "ı" in word:
                word2 = word.replace("ı", "i")
                snt_tag.append(word + '/' + str(words_clusters[word2]))
            else:
                snt_tag.append(word + '/' + str(words_clusters[word]))
            
        mod_file.write(" ".join(snt_tag) + '\n')
        
    mod_file.close()
    brown_file.close()  
    

def typetagger_to_eval(language, model):
    results_file = open("results/type_tagger/model_"+str(model)+"/res_" + language, encoding="utf-8") 
    
    words_clusters = {}
    
    for line in results_file:
        line = line.split()
          
        words_clusters[line[1]] = line[0]
        
    results_file.close()
    
    mod_file = open("results/type_tagger/model_"+str(model)+"/mod_res_" + language, 'w+', encoding="utf-8") 
    brown_file = open("data/brown/" + language, encoding="utf-8")
    
    for sentence in brown_file:
        sentence = sentence.split()
        snt_tag = []
        for word in sentence:
            snt_tag.append(word + '/' + str(words_clusters[word]))
        mod_file.write(" ".join(snt_tag) + '\n')
        
    mod_file.close()
    brown_file.close() 

#result_transformation(["arabic.200k", "catalan.200k", "czech.200k", "english.200k", "hindi.200k", "french.200k", "german.200k", "latin.200k", "norwegian.200k", "portuguese.200k", "portuguese_br.200k", "romanian.200k", "russian.200k", "spanish.200k"])
result_transformation(["hindi.200k"])

