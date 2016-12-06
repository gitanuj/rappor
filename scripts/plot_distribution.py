# Plot the data in a csv file
# as a histogram
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def plot(bins):
    #plt.hist(bins, 100)
    plt.plot(np.arange(0, len(bins.values()), 1), bins.values())
    plt.savefig('true_dist.png')

def log(message):
    logfile = 'plot_dist.log'
    f = open(logfile, 'a')
    f.write(message + '\n')
    f.close()

def plot_csv(filename):
    bins = {}
    with open(filename) as f:
        for line in f:
            sid, count = line.split(',')
            count = count.rstrip()
            bins[sid] = int(count)

    plot(bins)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: ' + sys.argv[0] + ' input file'
        sys.exit(1)
    log('Running plot_csv on ' + sys.argv[1])
    plot_csv(sys.argv[1])
    

