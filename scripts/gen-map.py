#!/usr/bin/python
#
# ./gen-map.py <params.csv>
#

import sys
import csv

sys.path.insert(0, '/home/vagrant/rappor/client/python')

import rappor

def HashCandidates(params, csv_in, csv_out):
  num_bloombits = params.num_bloombits

  for line in csv_in:
    word = line[0]
    row = [word]
    for cohort in xrange(params.num_cohorts):
      bloom_bits = rappor.get_bloom_bits(word, cohort, params.num_hashes,
                                         num_bloombits)
      for bit_to_set in bloom_bits:
        # bits are indexed from 1.  Add a fixed offset for each cohort.
        # NOTE: This detail could be omitted from the map file format, and done
        # in R.
        row.append(cohort * num_bloombits + (bit_to_set + 1))

    csv_out.writerow(row)

params = None
with open(sys.argv[1]) as f:
  params = rappor.Params.from_csv(f)
csv_in = csv.reader(sys.stdin)
csv_out = csv.writer(sys.stdout)
HashCandidates(rappor.Params(), csv_in, csv_out)
