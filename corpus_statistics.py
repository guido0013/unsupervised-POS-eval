import math
import csv

def compute_corpus_statistics(languages, output_name):
    with open(output_name, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(["Language", "#tokens", "#types", "Token/Type", "#sentences", "Avg |snt|", "#Tags", "Entropy"])
        
        int_tag_conversion = {}
        index = 0 
        
        for language in languages:
            brown = open("data/brown/" + language, encoding="utf-8")
            gold = open("gold_tags2/" + language + ".gold", encoding="utf-8")
            
            
            types = set()
            nr_tokens = 0
            nr_types = 0
            nr_snts = 0
            
            for sentence in brown:
                nr_snts += 1
                sentence = sentence.split()
                nr_tokens += len(sentence)
                for word in sentence:
                    if word not in types:
                        types.add(word)
                        nr_types += 1
            
            type_token_ratio = nr_tokens / nr_types       
            snt_len = nr_tokens / nr_snts 
            
            tag_word_dict = {}
            
            for word_tag in gold:
                word_tag = word_tag.split()
                if word_tag[1] in tag_word_dict:
                    tag_word_dict[word_tag[1]].append(word_tag[0])
                else:
                    tag_word_dict[word_tag[1]] = [word_tag[0]]
            
            nr_tags = len(tag_word_dict)
            
            entropy = calculate_entropy(tag_word_dict, nr_tokens)
            
            tag_info = {}
            for tag in tag_word_dict:
            
                if tag not in int_tag_conversion.values():
                    int_tag_conversion[index] = tag
                    index += 1
                
                tag_info[tag] = len(tag_word_dict[tag])
                
            tag_info_list = []
            tag_i = 0
            for tag_i in range(0, len(int_tag_conversion)):
                if int_tag_conversion[tag_i] in tag_info:
                    tag_info_list.append(tag_info[int_tag_conversion[tag_i]])
                else:
                    tag_info_list.append("-")  
                tag_i += 1  
            writer.writerow([language, nr_tokens, nr_types, type_token_ratio, nr_snts, snt_len, nr_tags, entropy] + tag_info_list)
            
            brown.close()
            gold.close()
            
        tag_names = []
        tag_i = 0
        for tag_i in range(0, len(int_tag_conversion)):
            tag_names.append(int_tag_conversion[tag_i])
            tag_i += 1
                
        writer.writerow(['', '', '', '', '', '', '', ''] + tag_names)
    
def calculate_entropy(clusters, total_words):
    entropy = 0
    for cluster in clusters:
        nr_words = len(clusters[cluster])
        probability = nr_words / total_words
        entropy += probability * math.log2(probability)
    return -entropy


compute_corpus_statistics(["arabic.200k", "catalan.200k", "czech.200k", "english.200k", "french.200k", "german.200k", "hindi.200k", "latin.200k", "norwegian.200k", "portuguese.200k", "portuguese_br.200k", "romanian.200k", "russian.200k", "spanish.200k"], "statistics.csv")
