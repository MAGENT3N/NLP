# NLP
Started with how inner products can lead us quantify document similarity.

---

## Implementations

| File | Topic | Description |
|------|-------|-------------|
| `document_similarity.py` | Document Similarity | Cosine similarity using word frequency vectors |

---

## Document Similarity

**File:** `document_similarity.py`  
**Concepts:** Linear Algebra, NLP, Cosine Similarity  
**What it does:** Measures how similar two documents are using the geometric 
notion of cosine similarity.(implementation is bad limited by python knoweldge as
I have a bunch of for loops so that can't be good)

**Approach:**
1. Convert each document into a word frequency vector
(This is the bulk of the task the math is very basic, getting the
text in the suitable form , removing punctuations ,setting the case etc)
3. Compute the cosine similarity between the two vectors:

```math
\text{similarity} = \frac{A \cdot B}{||A|| \cdot ||B||}
```

**Key insight:** The problem of comparing documents reduces to finding the 
angle between two vectors — documents with similar word distributions 
will have a smaller angle between them.

---

## To do next?
- TF-IDF weighting
- Comparing multiple documents at once
