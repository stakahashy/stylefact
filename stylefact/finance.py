"""
The toolkit for the statistical laws of financial time-series
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import powerlaw
from bisect import bisect_left
def log_distribution(series,side='positive',sample_point=100,ticks=None):

    """
    
    Parameters
    _________
    series : array-like
       time-series to be evaluated
    side : str (positive,negative)

    Returns
    _______
    ticks : list
        list of ranks
    dist_values : list
        frequency of i-th most frequent words
        

    Raises
    ______

    See also
    ________

    Examples
    ________
    """

    assert side in ['positive','negative']
    if side == 'positive':
        series = series[series > 0]
        if ticks is None:
            ticks = np.logspace(0,np.log(np.max(series)),num=sample_point)
    else:
        series = series[series < 0]
        if ticks is None:
        ticks = np.logspace(np.log(np.min(series),0),num=sample_point)
    
    series = np.sort(series)
    dist_values = []
    
    for tick1,tick2 in zip(ticks[:-1],ticks[1:]):
        count = bisect_left(series,tick2)-bisect_left(series,tick1)
        value = count / series.size
        dist_values.append(value)
    return ticks,dist_values
    
def linear_distribution(series):
    """
    
    Parameters
    _________
    series : array-like
        list of symbols to be analyzed

    Returns
    _______
    ticks : list
        list of ranks
    dist_values : list
        frequency of i-th most frequent words
        

    Raises
    ______

    See also
    ________

    Examples
    ________
    """

    ticks = np.linspace(np.min(series),np.max(series),num=100)
    series = np.sort(seies)
    dist_values = []

    for tick1,tick2 in zip(ticks[:-1],ticks[1:]):
        count = bisect_left(series,tick2)-bisect_left(series,tick1)
        dist_values.append(count/series.size)
    return ticks,dist_values

def autocorrelation(series,max_lag=1000,lags=None):
    """
    Autocorrelation function f(k)  measures the pearson correlation of two variables with lag k.
    
    Parameters
    _________
    series : array-like
        time-series to be evaluated
    max_lag : int, optional
        maximum lag evaluated

    Returns
    _______
    lags : list
        list of lags evaluated
    acf_values : list
        list of correlation values

    Raises
    ______

    See also
    ________

    Examples
    ________
    """
    if lags is None:
        lags = [i+1 for i in range(max_lag)]
    acf_values = []
    var = np.var(series)
    for lag in lags:
        series_1 = series[:-lag]
        series_2 = series[lag:]
        value = np.mean(series_1*series_2)/var
        acf_values.append(value)
        
    return lags,acf_values

def leverage_effect(series,max_lag=50,lags=None):
    """
    Compute leverage effect, the lead-lag correlation between price return and volatility.

    Bibliography:
    Leverage Effect in Financial Markets: The Retarded Volatility Model
    Jean-Philippe Bouchaud, Andrew Matacz, and Marc Potters
    Phys. Rev. Lett. 87, 228701 2001
    Return-volatility correlation in finacial dynamics. T. Qiu, B. Zheng, F.Ren and S.Trimper. 2006. Physical Review E 73 06513

    
    Parameters
    _________
    series : list
        list of symbols to be analyzed
    max_lag : int, optional
        maximum lag evaluated
    lags : list, optional
        lags to evaluate leverage effect

    Returns
    _______
    lags : list
        list of ranks
    lev_values : list
        values of leverage effect
        

    Raises
    ______

    See also
    ________

    Examples
    ________
    """
    if lags is None:
        lags = [i+1 for i in range(max_lag)]
    abs_series = np.abs(series)
    Z = np.mean(abs_series**2)**2
    second_term = np.mean(series)*np.mean(series**2)
    
    lev_values = []
    for lag in lags:
        if lag == 0:
            first_term = np.mean(series*(series)**2)
        elif lag > 0:
            first_term = np.mean(series[:-lag]*(series_abs[lag:]**2))
        else:
            first_term = np.mean(series[-lag:]*(series_abs[:lag]**2))
        value = (first_term-second_term)/Z
        lev_values.append(value)
    return lags, lev_values

def gainloss_asymmetry(series,sample_points=100000,theta=0.1):
    """
    Bibliography:
    Inverse statitics in economics: The gain-loss asymmetry
    Physica A324 338-343 2006.
    """
    assert theta != 0

    def compute_required_time_dist(series,theta):
        step_record = []
        for sample_point in range(sample_points):
            diff = 0.
            for step in range(1,series.size-sample_point-1):
                diff += series[sample_point+step-1]
                if theta > 0. and diff >= theta:
                    step_record.append(step)
                    break
                if theta < 0. and diff <= theta:
                    step_record.append(step)
                    break
        step_dist = np.zeros(series.size)
        for i in range(1,step_dist.size+1):
            step_dist[i-1] = step_record.count(i)
        return step_dist/step_dist.sum()
    step_dist_p = compute_required_time_dist(series,theta)
    step_dist_n = compute_required_time_dist(series,-theta)

    return step_dist_p,step_dist_n

def coarsefine_volatility(x,delta=5,min_lag=-20,max_lag=20):
    """
    Bibliography:
    Volatilities of different time resolutions — Analyzing the dynamics of market components
    Journal of Empirical Finance Volume 4, Issues 2–3, June 1997, Pages 213-239
    https://www.sciencedirect.com/science/article/abs/pii/S0927539897000078
    
    Parameters
    _________
    series : array-like
        time-series of price return 
    delta : int, optional
    min_lag : int, optional
    max_lag : int, optional

    Returns
    _______
    lags : list
        list of lags
    values : list
        list of.values corresponding to the lags.

    Raises
    ______

    See also
    ________

    Examples
    ________
    """

    def compute_coarse_volatility(series):
        coarse_volatility = []
        for i in range(series.size//delta):
            coarse_volatility.append(np.abs(np.sum(series[delta*i:delta*(i+1)])))
    def compute_fine_volatility(series):
        fine_volatility = []
        for i in range(series.size//delta):
            fine_volatility.append(np.sum(np.abs(series)[delta*i:delta*(i+1)])/delta)
   
    def compute_correlation(x1,x2):
        x1_mean = np.mean(x1)
        x2_mean = np.mean(x2)
        x1_std = np.std(x1)
        x2_std = np.std(x2)
        return np.mean((x1-x1_mean)*(x2-x2_mean))/(x1_std*x2_std)

    if lags is None:
        lags = [i for i in range(min_lag,max_lag+1)]
    coarse_volatility = compute_coarse_volatility(series)
    fine_volatility = compute_fine_volatility(series)
    values = []
    for lag in lags:
        if lag == 0:
            values.append(compute_correlation(coarse_volatility,fine_volatility))
        elif lag > 0:
            values.append(compute_correlation(coarse_volatility[lag:]),fine_volatility[:-lag])
        else:
            values.append(compute_correlation(coarse_volatility[:lag]),fine_volatility[-lag:])
    return lags, values
