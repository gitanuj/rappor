#!/usr/bin/python
#
#	./mapper.py <song_ids.txt> <rappor.csv> <actual.csv>
#

import sys
import csv
import pylab
import numpy as np

def plot_graph(actual, rappor, filename):
	pylab.close()
	pylab.plot(actual, color="b", linewidth=2.5, label="Actual")
	pylab.plot(rappor, color="r", linewidth=2.5, label="Rappor")
	pylab.legend(loc="upper right")
	pylab.xlim(-2000, len(actual))	# Just adding padding at origin
	pylab.ylim(-0.0001, max(rappor))	# Just adding padding at origin
	pylab.savefig(filename)
	# pylab.show()

song_ids = dict()
with open(sys.argv[1]) as f:
	for i, line in enumerate(f):
		song_ids[line.strip()] = i

rappor = dict()
csv_in = csv.reader(open(sys.argv[2]))
for (_, _, song_id, proportion, _) in csv_in:
	rappor[song_id] = float(proportion)

actual = dict()
csv_in = csv.reader(open(sys.argv[3]))
for (_, _, song_id, proportion, _) in csv_in:
	actual[song_id] = float(proportion)

rappor_proportions = [0] * len(song_ids)
actual_proportions = [0] * len(song_ids)
for str_id in song_ids.keys():
	p = 0.0
	try:
		p = rappor[str_id]
	except:
		pass
	rappor_proportions[song_ids[str_id]] = p
	q = 0.0
	try:
		q = actual[str_id]
	except:
		pass
	actual_proportions[song_ids[str_id]] = q

plot_graph(actual_proportions, rappor_proportions, "combined.png")

# Sorting the two lists
actual_sorted, rappor_sorted = (list(t) for t in zip(*sorted(zip(actual_proportions, rappor_proportions), reverse=True)))
plot_graph(actual_sorted, rappor_sorted, "combined_sorted.png")