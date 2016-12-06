# Read the triplets and write
# a csv containing song id, count pairs
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def log(message):
    logfile = 'count_frequencies.log'
    f = open(logfile, 'a')
    f.write(message + '\n')
    f.close()

def count_frequencies(filename):
    bins = {}
    with open(filename) as f:
        for line in f:
            #l = line.rstrip()
            elems = line.split('\t')
            if len(elems) < 3:
                log('error, line does not contain enough values:')
                log(line)
                continue
            
            sid = elems[1]
            count = elems[2].rstrip()

            try:
                count_int = int(count)
            except ValueError:
                log('error, ' + count + ' could not be converted to an integer')
                continue

            if sid in bins:
                bins[sid] += count_int
            else:
                bins[sid] = count_int
    for sid in bins:
        print sid + ', ' + str(bins[sid])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: ' + sys.argv[0] + ' input file'
        sys.exit(1)
    log('Running count_frequencies on ' + sys.argv[1])
    count_frequencies(sys.argv[1])
    

