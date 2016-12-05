#!/usr/bin/python
#
#	./sum_bits.py <encoded.txt> <output.txt>
#

import sys
import csv

sys.path.insert(0, '/home/vagrant/rappor/client/python')

import rappor

params = rappor.Params()

num_cohorts = params.num_cohorts
num_bloombits = params.num_bloombits

sums = [[0] * num_bloombits for _ in xrange(num_cohorts)]
num_reports = [0] * num_cohorts

csv_out = csv.writer(open(sys.argv[2], 'w'))

with open(sys.argv[1]) as f:
	for line in f:
		vals = line.strip().split(',')
		user_id = vals[0]
		cohort = int(vals[1])
		irr = vals[2]

		num_reports[cohort] += 1

		if not len(irr) == params.num_bloombits:
			raise RuntimeError("Expected %d bits, got %r" % (params.num_bloombits, len(irr)))

		for i, c in enumerate(irr):
			bit_num = num_bloombits - i - 1  # e.g. char 0 = bit 15, char 15 = bit 0
			if c == '1':
				sums[cohort][bit_num] += 1
			else:
				if c != '0':
					raise RuntimeError('Invalid IRR -- digits should be 0 or 1')

	for cohort in xrange(num_cohorts):
		# First column is the total number of reports in the cohort.
		row = [num_reports[cohort]] + sums[cohort]
		csv_out.writerow(row)
