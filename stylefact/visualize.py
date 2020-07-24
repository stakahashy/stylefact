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
    plt.figure(dpi=150)
    plt.plot(x,y,'.',markersize=8)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Normalized Scale in $\sigma$',fontsize=20)
    plt.ylabel('Probability Density Function $P(r)$',fontsize=40)
    plt.savefig(filename,transparent=True)
    plt.close()


def log_distribution(x,y,filename):
    #split into positive and negative sides
    dist_x_pos = x[x > 0]
    dist_y_pos = y[-dist_x_pos.size:]
    dist_x_neg = -x[x < 0]
    dist_y_neg = y[:dist_x_neg.size]
    #for positive
    plt.figure(dpi=150)
    plt.plot(dist_x_pos,dist_y_pos,'.')
    plt.xlabel('Normalized Scale in $\sigma$',fontsize=20)
    plt.ylabel('Probability Density Function $P(r)$',fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig(filename, transparent=True)
    plt.close()
    #for negative
    plt.figure(dpi=150)
    plt.plot(dist_x_neg,dist_y_neg,'.')
    plt.xlabel('Normalized Scale in $\sigma$',fontsize=20)
    plt.ylabel('Probability Density Function $P(r)$',fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig(filename+'_neg_log.png', transparent=True)
    plt.close()

def autocorrelation(x,y,file_name,scale='log'):
    plt.figure(dpi=150)
    plt.plot(x,y,'.')
    if scale is 'log':
        plt.ylim(1e-5,1.)
    else:
        plt.ylim(-1.,1.)
    plt.xscale(scale)
    plt.yscale(scale)
    plt.xlabel('lag $k$',fontsize=20)
    plt.ylabel('autocorrelation',fontsize=20)
    plt.savefig(filename,transparent=True)
    plt.close()

def Zipf(x,y,filename):
    plt.figure(dpi=150)
    plt.plot(x,y)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('rank',fontsize=20)
    plt.ylabel('frequency',fontsize=20)
    plt.savefig(filename,transparent=True)
    plt.close()

def Heap(x,y,filename):
    plt.figure(dpi=150)
    plt.plot(x,y,'.')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig(filename,transparent=True)
    plt.close()

def Ebeling_Neiman(x,y,filename):
    plt.figure(dpi=150)
    plt.plot(x,y)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('window size')
    plt.ylabel('variance')
    plt.savefig(filename,transparent=True)
