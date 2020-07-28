"""
The toolkit for the statistical laws of financial time-series
"""
import numpy as np
from bisect import bisect_left
def log_distribution(series,side='positive',ticks=None,sample_point=100):
    """
    
    Parameters
    _________
    series : array-like
       time-series to be evaluated
    side : str (positive,negative), optional
        the side to evaluate the tail
    ticks : array-like, optional
        hoge
    sample_point : int, optional
        If ticks is not specified, the number of ticks is set to this value
        Default 100

    Returns
    _______
    ticks : array-like
    dist_values : list
        the probability between ticks[i] and ticks[i+1]

    Examples
    ________

    References
    __________

    """

    assert side in ['positive','negative']
    if side == 'positive':
        series = series[series > 0]
        if ticks is None:
            ticks = np.linspace(0,np.max(series),num=sample_point)
    else:
        series = series[series < 0]
        if ticks is None:
            ticks = -np.linspace(0,-np.min(series),num=sample_point)[::-1]
    
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
        

    Examples
    ________

    References
    __________
    """

    ticks = np.linspace(np.min(series),np.max(series),num=100)
    series = np.sort(series)
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

    See also
    ________

    Examples
    ________

    References
    __________
    .. [Granger et al.] Granger, C.W. J., Ding, Z. Some Properties of Absolute Return: An Alternative Measure of Risk , Annales d'Économie et de Statistique, No. 40, pp. 67-91 1995
       [Cont] R. Cont, Empirical properties of asset returns: Stylized facts and statistical issues, Quantitative Finance, 1 (2001), pp. 1–14.

    """
    if lags is None:
        lags = [i+1 for i in range(max_lag)]
    acf_values = []
    mean = np.mean(series)
    var = np.var(series)
    for lag in lags:
        series_1 = series[:-lag]
        series_2 = series[lag:]
        value = np.mean((series_1-mean)*(series_2-mean))/var
        acf_values.append(value)
        
    return lags,acf_values

def leverage_effect(series,max_lag=50,lags=None):
    """
    The leverage effect, the lead-lag correlation between price return and volatility.
    
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
        

    Examples
    ________

    References
    __________
    .. [Bouchaud et al.] J.P. Bouchaud et al.,  Leverage Effect in Financial Markets: The Retarded Volatility Model.↲ Physical Review Letter 87, 228701 2001.
    .. [Qiu et al.] T. Qiu et al., Return-volatility correlation in finacial dynamics. Physical Review E 73 06513 2006.
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
            first_term = np.mean(series[:-lag]*(abs_series[lag:]**2))
        else:
            first_term = np.mean(series[-lag:]*(abs_series[:lag]**2))
        value = (first_term-second_term)/Z
        lev_values.append(value)
    return lags, lev_values

def gainloss_asymmetry(series,theta=0.1):
    """
    Gain loss asymmetry

    Parameters
    __________
    series : array-like
        time-series to be evaluated
    theta : int, optional
        The hyper-paramter theta

    Returns
    _______
    step_dist_p : numpy array
        The distribution of required time to reach positive theta price change
    step_dist_n : numpy array
        The distribution of required time to reach negative theta price change

    References
    __________
    .. [Mogens] Mogens H. Jensen et al., Inverse statistics in economics: The gain-loss asymmetry Physica A 324 (1) 338-343 2003.

    Examples
    ________

    """
    assert theta != 0

    def compute_required_time_dist(series,theta):
        step_record = []
        for sample_point in range(series.size):
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

def coarsefine_volatility(series,delta=5,lags=None,min_lag=-20,max_lag=20):
    """
    Coarse fine volatility

    Parameters
    __________
    series : array-like
        time-series of price return 
    delta : int, optional
        the length to calculate coarse price return 
    min_lag : int, optional
        minimum lag to evaluate
        Default is -20
    max_lag : int, optional
        maximum lag to evaluate
        Default is 20

    Returns
    _______
    lags : list
        list of lags
    values : list
        list of values corresponding to the lags

    References
    __________
    .. [Ulrich] Ulrich A. Müller et al., Volatilities of different time resolutions — Analyzing the dynamics of market components
    Journal of Empirical Finance Volume 4, Issues 2–3, June 1997, Pages 213-239

    Examples
    ________

    """

    def compute_coarse_volatility(series):
        coarse_volatility = []
        for i in range(series.size//delta):
            coarse_volatility.append(np.abs(np.sum(series[delta*i:delta*(i+1)])))
        return coarse_volatility
    def compute_fine_volatility(series):
        fine_volatility = []
        for i in range(series.size//delta):
            fine_volatility.append(np.sum(np.abs(series)[delta*i:delta*(i+1)])/delta)
        return fine_volatility
   
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
            values.append(compute_correlation(coarse_volatility[lag:],fine_volatility[:-lag]))
        else:
            values.append(compute_correlation(coarse_volatility[:lag],fine_volatility[-lag:]))

    return lags, values
