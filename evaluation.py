from collections import Counter

def many_to_1(clusters_file, gold_tags_file, cluster_format):
#clusters: list of tuples with [0]: word, [1]: induced cluster
# gold_tags: list of tuples with [0]: word, [1]: gold_tag 

    gold_tags = extract_gold_tags(gold_tags_file)

    if cluster_format == "brown":
        clusters = extract_brown(clusters_file)
    elif cluster_format == "clark":
        clusters = extract_clark(clusters_file)
    
    clusters_to_words = {}
    words_to_clusters = {}
    for word in clusters:
    
        if word[1] in clusters_to_words:
            clusters_to_words[word[1]].append(word[0])
        else:
            clusters_to_words[word[1]] = [word[0]]
            
        words_to_clusters[word[0]] = word[1]
        
    
    gold_dict = {}

    for word in gold_tags:
    
        if word[0] in gold_dict:
            gold_dict[word[0]].append(word[1])
        else:
            gold_dict[word[0]] = [word[1]]
    
    # choose tag with most occurrences
    for word in gold_dict.keys():
        if len(gold_dict[word]) == 1:
            gold_dict[word] = gold_dict[word][0]
        else:
            gold_dict[word] = Counter(gold_dict[word]).most_common(1)[0][0]

    # choose tag with most occurrences in gold tag set
    cluster_to_gold = {}
    for cluster in clusters_to_words.keys():
        count_dict = {}
        
        for word in clusters_to_words[cluster]:
            if gold_dict[word] in count_dict:
                count_dict[gold_dict[word]] += 1
            else:
                count_dict[gold_dict[word]] = 1
                
        cluster_to_gold[cluster] = max(count_dict, key=lambda key: count_dict[key])
        
    # calculate accuracy
    nr_words = len(words_to_clusters)
    correct_classifications = 0
    for word in words_to_clusters:
        #print(gold_dict[word])
        if cluster_to_gold[words_to_clusters[word]] == gold_dict[word]:
            correct_classifications += 1
    
    print("Many-to-one mapping: Accuracy: " + str(correct_classifications / nr_words))

def extract_gold_tags(infile):
    gold_tags = open(infile, encoding="utf-8")
    gold = []
    for line in gold_tags:
        line = line.split()
        gold.append((line[0], line[1]))
        
    gold_tags.close()
    
    return gold
    
    
def extract_brown(infile):
    clusters_file = open(infile, encoding="utf-8")
    clusters = []
    
    for line in clusters_file:
        line = line.split()
            
        clusters.append((line[1], line[0]))
        
    clusters_file.close()
    
    return clusters    
    
def extract_clark(infile):
    pass
    
#for key in clusters_dict.keys():
many_to_1("results/brown/res_dutch.brown", "gold_tags/dutch.gold", "brown")    
many_to_1("results/brown/res_galician.brown", "gold_tags/galician.gold", "brown")   
