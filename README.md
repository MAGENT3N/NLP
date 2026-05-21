# NLP
Originally started with trying to learn basic File i/o
Ended up counting distinct words which then led to writing
a program for calculating the similarity between 2 documents.

---

## Implementations

| File | Topic | Description |
|------|-------|-------------|
| `document_similarity.py` | Document Similarity | Cosine similarity using word frequency vectors |
| `tf_idf.py` | Document Similarity | Cosine similarity using tf_idf Metric|
---

## Document Similarity

**File:** `document_similarity.py`  
**Concepts:** Linear Algebra, NLP, Cosine Similarity ,Text frequency and Inverse Document frequency 
**What it does:** Measures how similar two documents are using the geometric 
notion of cosine similarity.(implementation is bad limited by python knoweldge as
I have a bunch of for loops so that can't be good)

**Approach:**
1. Convert each document into a word frequency vector
(This is the bulk of the task the math is very basic, getting the
text in the suitable form , removing punctuations ,setting the case etc was 
the hard part for me).
PROBLEMS:- In the first attempt I tried to convert the words into
a frequency vector by individually parsing the strings but the I realised
2 bodies of texts rarely(well almost never) have the same number of words in
them.So I had to create a common dictionary of all the words and then index
the frequency counts based on that common dictionary of all words.

3. Compute the cosine similarity between the two vectors:

```math
\text{similarity} = \frac{A \cdot B}{||A|| \cdot ||B||}
```

**Key insight:** The problem of comparing documents reduces to finding the 
angle between two vectors — documents with similar word distributions 
will have a smaller angle between them.

---

## To do next?
- Comparing multiple documents at once
