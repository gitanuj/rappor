#!/usr/bin/python
#
#	./encode.py <params.csv>
#

import sys
import csv
import time

sys.path.insert(0, '/home/vagrant/rappor/client/python')
sys.path.insert(0, '/home/vagrant/rappor/tests')

import rappor
import fastrand

def log(msg, *args):
  if args:
    msg = msg % args
  print >>sys.stderr, msg

def RapporClientSim(params, irr_rand, csv_in, csv_out):
  """Read true values from csv_in and output encoded values on csv_out."""
  header = ('client', 'cohort', 'irr')
  csv_out.writerow(header)

  # TODO: It would be more instructive/efficient to construct an encoder
  # instance up front per client, rather than one per row below.
  start_time = time.time()

  for i, (client_str, cohort_str, true_value) in enumerate(csv_in):
    if i == 0:
      if client_str != 'client':
        raise RuntimeError('Expected client header, got %s' % client_str)
      if cohort_str != 'cohort':
        raise RuntimeError('Expected cohort header, got %s' % cohort_str)
      if true_value != 'value':
        raise RuntimeError('Expected value header, got %s' % value)
      continue  # skip header row

    #if i == 30:  # EARLY STOP
    #  break

    if i % 10000 == 0:
      elapsed = time.time() - start_time
      log('Processed %d inputs in %.2f seconds', i, elapsed)

    cohort = int(cohort_str)
    secret = client_str
    e = rappor.Encoder(params, cohort, secret, irr_rand)

    # Real users should call e.encode().  For testing purposes, we also want
    # the PRR.
    irr = e.encode(true_value)
    irr_str = rappor.bit_string(irr, params.num_bloombits)

    out_row = (client_str, cohort_str, irr_str)
    csv_out.writerow(out_row)

params = None
with open(sys.argv[1]) as f:
  params = rappor.Params.from_csv(f)
csv_out = csv.writer(sys.stdout)
csv_in = csv.reader(sys.stdin)
irr_rand = fastrand.FastIrrRand(params)
RapporClientSim(params, irr_rand, csv_in, csv_out)