"""
The toolkit for the statistical laws of natural languages
"""
import numpy as np
from collections import Counter
from utils import generate_x
import language_utils

def zipf(words,relative_freq=False):
    """
    Zipf's law

    Compute the rank-frequency distribution.
    x: rank
    y: frequency of i-th most frequent words

    George K. Zipf (1949) Human Behavior and the Principle of Least Effort. Addison-Wesley.
    

    """
    counts = Counter(words)
    y = list(counts.values())
    if relative_freq:
        y = [e/len(words) for e in y]
    x = [i+1 for i in range (len(y))]
    return x,y

def Heap(words,x=None):
    """
    Heaps' law

    Compute the growth of the number of unique words with respect to the text size.

    Parameters
    __________
    words: list
    x: list, optional

    Returns
    _______
    x: text size
    y: the number of unique words

    Examples
    ________
    >>> from language import Heap
    >>> words = ['a','a','a','b','c','c','d','e','f','f']
    >>> Heap(words)
    >>> x,y
    [1,2,3,4,5,6,7,8,9,10] [1,1,1,2,3,3,4,5,6,6]
    """

    if x is None:
        x = generate_x(max_x=len(words))
    y = []
    for e in x:
        y.append(len(list(set(words[:e]))))
    return x,y

def MI(words,x=None,threshold = 1e-8):
    """
    Mutual Information: I(X;Y)
    Mutual Information Functions of Natural Language Texts. Wentian Li. Santa Fe Research 1989.
    """
    if x is None:
        pass
    vocabulary_list = list(set(words))
    vocabulary_size = len(vocabulary_list)
    vocabulary_dict = dict()
    for i,e in vocabulary_list:
        vocabulary_dict[e] = i
    y = []
    for d in x:
        matrix = np.zeros((vocabulary_size,vocabulary_size)) 
        for i in range(len(words)-d):
            x1 = vocabulary_dict[words[i]]
            x2 = vocabulary_dict[words[i+d]]
            matrix[x1][x2] += 1
        matrix = matrix / (len(words)-d)
        for i in range(vocabulary_size):
            for j in range(vocabulary_size):
                pxy = matrix[i,j]
                px = matrix[i,:].sum()
                py = matrix[:,j].sum()
                if px > threshold and py > threshold and pxy > threshold:
                    mi += pxy*np.log(pxy/(px*py))
        y.append(mi)
    return x,y
