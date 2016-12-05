#!/usr/bin/python
#
#	./encode.py <train-triplets.txt> <output.txt>
#

import sys

sys.path.insert(0, '/home/vagrant/rappor/client/python')
sys.path.insert(0, '/home/vagrant/rappor/tests')

import rappor
import fastrand

params = rappor.Params()
irr_rand = fastrand.FastIrrRand(params)

output = open(sys.argv[2], 'w')

with open(sys.argv[1]) as f:
	for line in f:
		vals = line.split()

		client_str = vals[0]
		song_str = vals[1]
		song_count = vals[2]

		secret = client_str
		cohort = hash(client_str) % params.num_cohorts
		cohort_str = str(cohort)

		e = rappor.Encoder(params, cohort, secret, irr_rand)

		for i in range(int(song_count)):
			irr = e.encode(song_str)
			irr_str = rappor.bit_string(irr, params.num_bloombits)
			row = [client_str, cohort_str, irr_str]
    		output.write(','.join(row) + '\n')

output.close()
