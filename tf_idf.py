import document_similarity as ds
import math
import numpy as np
"""
   Instead of using the frequency vectors,we find the
   cosing similarity between two documents by using 
   the tf_idf(total frequency and inverse document frequency)
   of the words in the documents
"""

def main():
    count1 = ds.get_word_counts('mov_para_1.txt')
    count2 = ds.get_word_counts('mov_para_1.txt')
    
    tf_1 = calculate_tf(count1)
    tf_2 = calculate_tf(count2)
    
    idf_values = calculate_idf(count1, count2)
    
    tf_idf_vals_1 = tf_idf_score(tf_1, idf_values)
    tf_idf_vals_2 = tf_idf_score(tf_2, idf_values)
    
    similarity = cosine_similarity(tf_idf_vals_1, tf_idf_vals_2, idf_values)
    print(f"Cosine Similarity: {similarity:.4f}")
"""
   Function for calculating the the tf value of each word
   TF = number of times a word appears/total number of words
   Input- A dictionary mapping each unique word to it frequency
   Output- A dictionary mapping each unique word with its tf score
"""
    
def calculate_tf(count):
    tf = {}
    total_words = sum(count.values()) 
    for key, value in count.items():
        tf[key] = round(value / total_words, 4)
    return tf
"""
    Function for calculating the IDF value of each word
    IDF = log((number of documents)/(number of documents containing
                                     that word)) + 1(to avoid 0 error)
    IDF is useful for establishing the uniqueness of a word in the docu
    ment. Redundant words get a lower score as they have a higher prob-
    ability of appearing across the corupus of the documents
    Input- Dictionary contatining the word counts of each document
    Output- Dictionary mapping the words to their idf scores
"""
def calculate_idf(count1, count2):
    idf = {}
    common_words = set(count1.keys()) | set(count2.keys())
    no_of_documents = 2 # Hardcoded to 2 
    
    for words in common_words:
        doc_count = 0
        if words in count1:
            doc_count += 1
        if words in count2:
            doc_count += 1
        
        # Added "+ 1" smoothing to prevent log(1) = 0
        idf[words] = math.log(no_of_documents / doc_count) + 1
    return idf
"""
   Function for calculating the tf * idf value for each word
   Input- TF dictionary
   Output - Dictionary containing the tf-idf score of each word
"""
def tf_idf_score(tf, idf):
    tf_idf_score = {}
    for word in tf:
        tf_idf_score[word] = round(tf[word] * idf[word], 4)
    return tf_idf_score
"""
   Function for calculating the cosine_similarity using the 
   tf_idf score of each individual document
   Input- Tf_Idf dictionaries of the documents and idf_values
   Output- Cosine similarity of the two documents
"""
def cosine_similarity(tf_idf_1, tf_idf_2, idf_values):
    vector_1 = []
    vector_2 = []
    
    for word in idf_values:
        vector_1.append(tf_idf_1.get(word, 0))
        vector_2.append(tf_idf_2.get(word, 0))
        
    vector_1 = np.array(vector_1)
    vector_2 = np.array(vector_2)
    
    # Avoiding 0 / 0 division errors if vectors are empty or all zeros
    norm_1 = np.linalg.norm(vector_1)
    norm_2 = np.linalg.norm(vector_2)
    if norm_1 == 0 or norm_2 == 0:
        return 0.0
        
    return np.dot(vector_1, vector_2) / (norm_1 * norm_2)
    
if __name__ == "__main__":
    main()