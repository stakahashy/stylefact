"""
The toolkit for the statistical laws of natural language
"""
import numpy as np
from collections import Counter
from stylefact.utils import generate_x, loglog_fitting

def Zipf(words,relative_freq=False):
    """
    Zipf's law

    Compute the rank-frequency distribution.
    
    Parameters
    _________
    words : list
        list of symbols to be analyzed
    relative_freq : bool, optional
        If True, the frequency is scaled to the empirical probability.
        Default is False.

    Returns
    _______
    x : list
        list of ranks
    y : list
        frequency of i-th most frequent words
    exp : float
        The Zipf exponent

    Raises
    ______

    See also
    ________

    Reference
    _________
    .. [Zipf] George K. Zipf (1949) Human Behavior and the Principle of Least Effort. Addison-Wesley.


    Examples
    ________
    >>> from language import Zipf
    >>> import random
    >>> words = [str(random.randint(0,100)) for i in range(10000)]
    >>> x,y,exp = Zipf(words)

    """
    counts = Counter(words)
    y = list(counts.values())
    if relative_freq:
        y = [e/len(words) for e in y]
    x = [i+1 for i in range (len(y))]
    exp = loglog_fitting(x,y)
    return x,y,exp

def Heap(words,x=None):
    """
    Heaps' law

    Compute the growth of the number of unique words with respect to the text size.

    Parameters
    __________
    words : list
        list of symbols to be analyzed
    x: list, optional
        list of text sizes
        if x = None, x is specified by utils.generate_x, suitable for log-log plot.
        Default is None.

    Returns
    _______
    x: list
        list of text size
    y: list
        list of number of unique words up to  x[i]-th words
    exp: float
        Heap's exponent

    References
    __________
    [Heaps] Heaps, Harold Stanley (1978), Information Retrieval: Computational and Theoretical Aspects, Academic Press. Heaps' law is proposed in Section 7.5 (pp. 206–208).
    [Herdan] Herdan, Gustav (1960), Type-token mathematics, The Hague: Mouton.

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
    exp = loglog_fitting(x,y)
    return x,y

def MI(words,x=None,threshold = 1e-8):
    """
    Mutual Information: I(X;Y)


    Parameters
    _________
    words : list
        list of symbols to be analyzed
    x : list, optional
        list of distances to compute the mutual information.
        if x = None, x is specified by utils.generate_x, suitable for log-log plot.
        Default is None. 
    threshold : float, optional
        threshold value to avoid log(0) computation. 
        Default is 1e-8

    Returns
    _______
    x : list
        list of distances
    y : list
        list of mutual information values for distance of x[i]

    Raises
    ______

    See also
    ________

    References
    __________
    [Li] Mutual Information Functions of Natural Language Texts. Wentian Li. Santa Fe Research 1989.

    Examples
    ________
    >>> from language import MI
    >>> import random
    >>> words = [str(random.randint(0,100)) for i in range(10000)]
    >>> x,y = MI(words)
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

def Ebeling_Neiman(words,window_sizes=None,max_size=100000):
    """
    Ebeling Neiman method
    Bibliography:
    Mutual Information Functions of Natural Language Texts. Wentian Li. Santa Fe Research 1989.

    Parameters
    _________
    words : list
        list of symbols to be analyzed
    window_sizes : list, optional
        list of window sizes  to compute the mutual information.
        if x = None, x is specified by utils.generate_x, suitable for log-log plot.
        Default is None. 
    max_size : int, optional
        the maximum window size to be evaluated
        Default is 100000
    Returns
    _______
    x : list
        list of window sizes
    y : list
        list of variance corresponding to x[i]
    Raises
    ______

    See also
    ________

    References
    __________
    .. [Ebeling] Ebeling, W. and Neiman A. Long-range correlations between letters and sentences in texts, Physica A. 215 (3), pp. 233-241. 1995.


    Examples
    ________
    >>> from language import MI
    >>> import random
    >>> words = [str(random.randint(0,100)) for i in range(10000)]
    >>> x,y = MI(words)
    """
    vocabulary = set(words)
    if window_sizes is None:
        window_sizes = []
        window_size = 10
        words_size = len(words)
        while window_size < max_size:
            window_sizes.append(int(window_size))
            window_size *= 1.8

    positions = dict()
    for e in vocabulary:
        positions[e] = np.where(words==e)[0]

    window_vars = []
    for window_size in window_sizes:
        window_var = 0.
        for e in vocabulary:
            counts = np.zeros(words_size//window_size)
            x = positions[e]
            for value in x:
                if value//window_size < words_size//window_size:
                    counts[value//window_size] += 1
            window_var += np.var(counts)
        window_vars.append(window_var)
    return window_sizes, window_vars


