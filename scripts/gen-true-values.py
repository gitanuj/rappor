#!/usr/bin/python

import sys

sys.path.insert(0, '/home/vagrant/rappor/client/python')

import rappor

params = rappor.Params()

with open(sys.argv[1]) as f:
	for line in f:
		vals = line.split()
		user_id, song_id, play_count = vals
		cohort = str(hash(user_id) % params.num_cohorts)
		for i in range(int(play_count)):
			row = [user_id, cohort, song_id]
			print(','.join(row))