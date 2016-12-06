
# Generate true values
./gen-true-values.py ../data/case_params.csv ../data/train_triplets/segmentaa > ../data/case_true_values.csv

# Generate case_counts.csv
cat ../data/case_true_values.csv | ./encode.py ../data/case_params.csv | ./sum_bits.py ../data/case_params.csv > ../data/case_counts.csv

# Generate case_map.csv
cat ../data/case_unique_values.txt | ./gen-map.py ../data/case_params.csv > ../data/case_map.csv

# Run analysis
./compare_dist.R ../data/case ../data/case .