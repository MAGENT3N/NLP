
import numpy as np

PUNCTUATION = '.!?,-:;'

"""
   The main approach :-
   1)Take a text file and process it which involves,
     Removing all the punctuations which we have defined
     in the Global scope and setting all ther words to lower
     case
     
     2) Then we take the words in a list and count how many time
     Each words appears and store it in a dictionary where the 
     key is the specific word and the value is its frequency
     
     3) We then collect the frequencies from the dictionary and 
     Make a frequency collector of sorts
     Point three has a huge mistake mainly that we presume the
     documents will be of the same word count but that is never
     (almost) the case so we need to make a dictionary of the 
     combined words of  both documents and get frequency vectors
     by comparing from that common dictionary which will solve our
     dimension problem(Explained clearly in the def frequency_vector())
     
     4)We then can find the cosine similarity as the frequency enc
     oded are just numbers
"""
def main():
    # first txt file
    para_1 = get_word_counts('mov_para_1.txt')
    # Second txt file
    para_2 = get_word_counts('mov_para_2.txt')
    # Creating the word counts to freq vectors of each text
    vector_para_1 , vector_para_2 = frequency_vector(para_1, para_2)
    print(vector_para_1)
    # To find similarity we use cos(theta) = a.b/|a|.|b|
    similarity = ((np.dot(vector_para_1 , vector_para_2))/(np.linalg.norm(vector_para_1) *
                  np.linalg.norm(vector_para_2)))
    print(f"Similarity Score: {similarity:.4f}")





"""
   Function for deleting PUNCTUATION from the
   text string
"""

def delete_punctuation(string):
    result = ''
    for char in string:
        if char not in PUNCTUATION:
            result += char
    return result
"""
   Function for opening file and getting individual
   word counts
"""
def get_word_counts(file_name):
    #Initializing an empty dictionary
    counts = {}
    with open(file_name) as file:
        for line in file:
            words = delete_punctuation(line).split()
            #Converting to lower case
            for word in words:
                word = word.lower()
                #Building our dictionary
                if word not in counts:
                    counts[word] = 1
                else :
                    counts[word] += 1
    return counts
"""
   Function for creating a frequency vector 
   of all the words in the text{THIS APPROACH WAS WRONG
    BECAUSE THE DIMENSIONS WILL NEVER MATCH }
   
   BETTER APPROACH:-
   Creat a common dictionary with all the combines words of the
   2 texts , then compare those indinvidual dictionaries with
   the common dictionary , if the key is present 1 will be added
   to the vector else 0
   Exampples- txt 1-"My name is A",txt-2-"My name is B"
   common_dictionary set is {My , name ,is , A , B}
   vector_1 = [1,1,1,1,0] and vector_2 = [1,1,1,0,1]
   Now the dimensions are matched
"""
def frequency_vector(counts_1 , counts_2):
    all_words = {}
    vector_1 = []
    vector_2 = []
    for key in counts_1:
        all_words[key] = counts_1[key]
    for key in counts_2:
        all_words[key] = counts_2[key]
    for key in all_words:
        if key in counts_1:
            vector_1.append(counts_1[key])
        else :
            vector_1.append(0)
        if key in counts_2:
            vector_2.append(counts_2[key])
        else:
            vector_2.append(0)
    return vector_1 , vector_2
            
    

# def dot_product(vector1 , vector2):
#     if len(vector1)
#     for i in range(len(vector))

if __name__=="__main__":
    main()