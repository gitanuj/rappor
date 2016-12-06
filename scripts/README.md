
# Generate case_counts.csv
./gen-true-values.py ../data/case_params.csv ../data/train_triplets/segmentaa | ./encode.py ../data/case_params.csv | ./sum_bits.py ../data/case_params.csv > ../data/case_counts.csv

# Generate case_map.csv
cat ../data/case_unique_values.txt | ./gen-map.py ../data/case_params.csv > ../data/case_map.csv