"""
pass
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import powerlaw

def tail_distribution(x):
    """
    
    Parameters
    _________
    x : array-like
       list of symbols to be analyzed

    Returns
    _______
    x : list
        list of ranks
    y : list
        frequency of i-th most frequent words
        

    Raises
    ______

    See also
    ________

    Examples
    ________
    """
    pass
    pass
    
def distribution(x):
    """
    
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
        

    Raises
    ______

    See also
    ________

    Examples
    ________
    """
    pass

def autocorrelation(x,min_lag=1,max_lag=1000,lags=None):
    """
    Autocorrelation function f(k)  measures the pearson correlation of two variables with lag k.
    
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
        

    Raises
    ______

    See also
    ________

    Examples
    ________
    """
    if lags is None:
        lags = [i for i in range(min_lag,max_lag+1)]
    values = []
    for lag in lags:
        pass

def leverage_effect(x,min_lag=1,max_lag=1000,lags=None):
    """
    Compute leverage effect, the lead-lag correlation between price return and volatility.


    Bibliography:
    Leverage Effect in Financial Markets: The Retarded Volatility Model
    Jean-Philippe Bouchaud, Andrew Matacz, and Marc Potters
    Phys. Rev. Lett. 87, 228701 2001
    Return-volatility correlation in finacial dynamics. T. Qiu, B. Zheng, F.Ren and S.Trimper. 2006. Physical Review E 73 06513

    
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
        

    Raises
    ______

    See also
    ________

    Examples
    ________
    """
    if lags is None:
        lags = [i for i in range(min_lag,max_lag+1)]
    values = []
    x_abs = np.abs(x)
    second_term = np.mean(x)*np.mean(x_abs**2)
    denominator = (np.mean(x_abs**2))**2
    for lag in lags:
        if lag == 0:
            first_term = np.mean(x*(x_abs)**2)
        elif lag > 0:
            first_term = np.mean(x[:-t]*(x_abs[t:]**2)) 
        else:
            first_term = np.mean(x[-t:]*(x_abs[:t]**2))
        values.append(first_term-second_term)/
    return lags,values

def gainloss_asymmetry(x):
    """
    Bibliography:
    Inverse statitics in economics: The gain-loss asymmetry
    Physica A324 338-343 2006.
    """
    pass

def coarsefine_volatility(x,delta=5,min_lag=-20,max_lag=20):
    """
    Bibliography:
    Volatilities of different time resolutions — Analyzing the dynamics of market components
    Journal of Empirical Finance Volume 4, Issues 2–3, June 1997, Pages 213-239
    https://www.sciencedirect.com/science/article/abs/pii/S0927539897000078
    
    Parameters
    _________
    words : array-like
        time-series of price return 
    delta : int, optional
    min_lag : int, optional
    max_lag : int, optional

    Returns
    _______
    x : list
        list of ranks
    y : list
        frequency of i-th most frequent words

    Raises
    ______

    See also
    ________

    Examples
    ________
    """

    def compute_coarse_volatility(x):
        coarse_volatility = []
        for i in range(x.size//delta):
            coarse_volatility.append(np.abs(np.sum(x[delta*i:delta*(i+1)])))
    def compute_fine_volatility(x):
        fine_volatility = []
        for i in range(x.size//delta):
            fine_volatility.append(np.sum(np.abs(x)[delta*i:delta*(i+1)])/delta)
   
   def compute_correlation(x1,x2):
       x1_mean = np.mean(x1)
       x2_mean = np.mean(x2)
       x1_std = np.std(x1)
       x2_std = np.std(x2)
       return np.mean((x1-x1_mean)*(x2-x2_mean))/(x1_std*x2_std)


