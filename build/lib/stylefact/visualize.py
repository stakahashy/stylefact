import matplotlib as mpl
mpl.use('Agg')
mpl.rcParams['figure.autolayout']=True
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

def leverage_effect(x,y,filename):          
    plt.figure(dpi=150)
    plt.plot(x,y)
    plt.xlabel(r'$t$',fontsize=20)
    plt.ylabel(r'$L(t)$',fontsize=20)
    plt.axhline()
    plt.savefig(filename,transparent=True)
    plt.close()


def linear_distribution(x,y,filename):
    if len(x) == len(y) + 1:
        x = [(x[i]+x[i+1])/2 for i in range(x.size-1)]
    plt.figure(dpi=150)
    plt.plot(x,y,'.')
    plt.xlabel(r'Price Return $r_{t}$',fontsize=16)
    plt.ylabel('Probability Density Function $P(r)$',fontsize=16)
    plt.savefig(filename,transparent=True)
    plt.close()


def log_distribution(x,y,filename):
    if len(x) == len(y) + 1:
        x = [(x[i]+x[i+1])/2 for i in range(x.size-1)]
    plt.figure(dpi=150)
    plt.plot(x,y,'.')
    plt.ylim(1e-4,1e0)
    plt.xlabel(r'Price Return $r_{t}$',fontsize=16)
    plt.ylabel(r'Probability Density Function $P(r)$',fontsize=16)
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig(filename, transparent=True)
    plt.close()
    plt.close()

def autocorrelation(x,y,filename,scale='log'):
    plt.figure(dpi=150)
    plt.plot(x,y,'.')
    if scale is 'log':
        plt.ylim(1e-5,1.)
    else:
        plt.ylim(-1.,1.)
    plt.xscale(scale)
    plt.yscale(scale)
    plt.xlabel('lag $k$',fontsize=16)
    plt.ylabel('correlation',fontsize=16)
    plt.savefig(filename,transparent=True)
    plt.close()

def coarsefine_volatility(x,y,filename):
    diffs = []
    for i in range(len(x)):
        if x[i] == 0:
            zero_position = i
    max_lag = min(max(x),-min(x))
    for i in range(max_lag):
        diffs.append(y[zero_position+i]-y[zero_position-i])
    plt.figure(dpi=150)
    plt.plot(x,y)
    plt.plot([i for i in range(max_lag)],diffs)
    plt.xlabel('lag $k$',fontsize=16)
    plt.ylabel(r'$\rho (k)$',fontsize=16)
    plt.axhline(color='black')
    plt.savefig(filename,transparent=True)
    plt.close()

def gainloss_asymmetry(y1,y2,filename,xscale='log'):
    plt.figure(dpi=150)
    plt.plot([i+1 for i in range(len(y1))],y1,'.',color='red')
    plt.plot([i+1 for i in range(len(y2))],y2,'.',color='blue')
    plt.xlabel('step',fontsize=16)
    plt.ylabel('distribution',fontsize=16)
    plt.xscale(xscale)
    plt.savefig(filename,transparent=True)
    plt.close()


