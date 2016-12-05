#!/usr/bin/python

import sys
import csv

sys.path.insert(0, '/home/vagrant/rappor/client/python')

import rappor

def HashCandidates(params, stdin, stdout):
  num_bloombits = params.num_bloombits
  csv_out = csv.writer(stdout)

  for line in stdin:
    word = line.strip()
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


HashCandidates(rappor.Params(), open(sys.argv[1]), sys.stdout)
