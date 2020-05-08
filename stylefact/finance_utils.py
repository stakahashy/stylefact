"""
utility functions for finance.py
"""
import numpy as np

def normalize(x):
    x = np.array(x)
    mean = np.mean(x)
    std = np.std(x)
    return (x-mean)/std
    
