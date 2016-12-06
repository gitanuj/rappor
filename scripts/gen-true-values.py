#!/usr/bin/python
#
#	./gen-true-values.py <params.csv> <segment>
#

import sys
import csv

sys.path.insert(0, '/home/vagrant/rappor/client/python')

import rappor

params = None
with open(sys.argv[1]) as f:
  params = rappor.Params.from_csv(f)

csv_out = csv.writer(sys.stdout)
header = ('client', 'cohort', 'value')
csv_out.writerow(header)

with open(sys.argv[2]) as f:
	for line in f:
		vals = line.split()
		user_id, song_id, play_count = vals
		cohort = str(hash(user_id) % params.num_cohorts)
		for i in range(int(play_count)):
			row = (user_id, cohort, song_id)
			csv_out.writerow(row)