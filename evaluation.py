from collections import Counter
import math

########################################################################################################################
######### Many-to-one mapping
########################################################################################################################

def many_to_1(clusters_file, gold_tags_file, cluster_format):
#clusters: list of tuples with [0]: word, [1]: induced cluster
# gold_tags: list of tuples with [0]: word, [1]: gold_tag 

    if cluster_format == "brown":
        clusters = extract_brown(clusters_file)
    elif cluster_format == "clark":
        clusters = extract_clark(clusters_file)
    
    gold_tags = extract_gold_brown(gold_tags_file)
    
    clusters_to_words, words_to_clusters = cluster_dictionaries(clusters)
    
    gold_dict = gold_dictionary(gold_tags)
    
    # choose tag with most occurrences
    gold_dict = most_occuring_tags(gold_dict)

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
    
########################################################################################################################
######### Variation of Information
########################################################################################################################
def variation_information(clusters_file, gold_tags_file, cluster_format):

    if cluster_format == "brown":
        clusters = extract_brown(clusters_file)
    elif cluster_format == "clark":
        clusters = extract_clark(clusters_file)
    
    gold_tags = extract_gold_brown(gold_tags_file)
    
    clusters_to_words, words_to_clusters = cluster_dictionaries(clusters)
    
    gold_dict = gold_dictionary(gold_tags)
    
    # choose tag with most occurrences
    gold_dict = most_occuring_tags(gold_dict)
    
    # reverse clusters and words (which we can do now as we have obtained a 1-to-1 mapping in the previous step)
    gold_to_words = {}
    for word in gold_dict:
        if gold_dict[word] in gold_to_words:
            gold_to_words[gold_dict[word]].append(word)
        else:
            gold_to_words[gold_dict[word]] = [word]
    
    
    total_words = len(gold_dict)
    
    ent_tags = calculate_entropy(clusters_to_words, total_words)
    ent_gold = calculate_entropy(gold_to_words, total_words)

    mutual_info = calculate_mutual_info(clusters_to_words, gold_to_words, total_words)
    
    print("Variation of Information: Score (in bits): " + str(ent_tags + ent_gold - 2 * mutual_info))
    




########################################################################################################################
def extract_gold_brown(infile):
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
    clusters_file = open(infile, encoding="utf-8")
    clusters = []
    
    for line in clusters_file:
        line = line.split()
            
        clusters.append((line[0].lower(), line[1]))
        
    clusters_file.close()
    
    return clusters    


########################################################################################################################

def cluster_dictionaries(clusters):
    clusters_to_words = {}
    words_to_clusters = {}
    for word in clusters:
    
        if word[1] in clusters_to_words:
            clusters_to_words[word[1]].append(word[0])
        else:
            clusters_to_words[word[1]] = [word[0]]
            
        words_to_clusters[word[0]] = word[1]
        
    return clusters_to_words, words_to_clusters
   
   
def gold_dictionary(gold_tags):
    gold_dict = {}

    for word in gold_tags:
    
        if word[0] in gold_dict:
            gold_dict[word[0]].append(word[1])
        else:
            gold_dict[word[0]] = [word[1]]
            
    return gold_dict

def most_occuring_tags(gold_dict):
    for word in gold_dict.keys():
        if len(gold_dict[word]) == 1:
            gold_dict[word] = gold_dict[word][0]
        else:
            gold_dict[word] = Counter(gold_dict[word]).most_common(1)[0][0]
    
    return gold_dict
    
def calculate_entropy(clusters_to_words, total_words):
    entropy = 0
    for cluster in clusters_to_words:
        nr_words = len(clusters_to_words[cluster])
        probability = nr_words / total_words
        entropy += probability * math.log2(probability)
    return -entropy
    
def calculate_mutual_info(clusters_to_words, gold_to_words, total_words):
    mutual_info = 0
    for cluster in clusters_to_words:
    
        nr_cluster_words = len(clusters_to_words[cluster]) 
        
        for gold_tag in gold_to_words:
        
            nr_gold_tag_words = len(gold_to_words[gold_tag])
            nr_joint_words = 0
            for word in clusters_to_words[cluster]:
                if word in gold_to_words[gold_tag]:
                    nr_joint_words += 1
            joint_prob = nr_joint_words / total_words
            
            prob_cluster = nr_cluster_words / total_words
            prob_gold_tag = nr_gold_tag_words / total_words
            if joint_prob != 0:
                mutual_info += joint_prob * math.log2(joint_prob / (prob_cluster * prob_gold_tag))

    return mutual_info

########################################################################################################################

#for key in clusters_dict.keys():
#many_to_1("results/brown/res_dutch.brown", "gold_tags/dutch.gold", "brown")    
#many_to_1("results/brown/res_galician.brown", "gold_tags/galician.gold", "brown")   
#many_to_1("results/clark/res_galician.clark", "gold_tags/galician.gold", "clark")   
#many_to_1("results/clark/res_english.clark", "gold_tags/english.gold", "clark") 
#many_to_1("results/clark/res_slovenian.clark", "gold_tags/slovenian.gold", "clark") 
#many_to_1("results/clark/res_dutch2.clark", "gold_tags/dutch.gold", "clark")
variation_information("results/clark/res_dutch2.clark", "gold_tags/dutch.gold", "clark")
variation_information("results/brown/res_dutch.brown", "gold_tags/dutch.gold", "brown")
variation_information("results/brown/res_galician.brown", "gold_tags/galician.gold", "brown")
