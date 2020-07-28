import numpy as np

def generate_x(max_x=1000,mode='log'):
    x = [i+1 for i in range(9)]
    exp = 1.2
    while x[-1] < max_x:
        x.append(int(x[-1]*exp))
    return x

def loglog_fitting(x,y):
    const,slope = np.polyfit(x,y,1)
    return slope
