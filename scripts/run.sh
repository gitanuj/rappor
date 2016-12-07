#!/bin/bash
#
#	Input:
#		Requires case_params.csv & case_unique_values.txt in $DATA_DIR
#		And segment file at $SEGMENT_PATH
#
#	Output:
#		Generates all_output.txt and metrics.csv in current directory (and other files in $DATA_DIR)
#

SEGMENT_PATH='../train_triplets/segmentaa'
DATA_DIR='../segmentaa-data'

# Generate true values
./gen-true-values.py $DATA_DIR/case_params.csv $SEGMENT_PATH > $DATA_DIR/case_true_values.csv

# Generate case_counts.csv
cat $DATA_DIR/case_true_values.csv | ./encode.py $DATA_DIR/case_params.csv | ./sum_bits.py $DATA_DIR/case_params.csv > $DATA_DIR/case_counts.csv

# Generate case_map.csv
cat $DATA_DIR/case_unique_values.txt | ./gen-map.py $DATA_DIR/case_params.csv > $DATA_DIR/case_map.csv

# Run analysis
./compare_dist.R $DATA_DIR/case $DATA_DIR/case .