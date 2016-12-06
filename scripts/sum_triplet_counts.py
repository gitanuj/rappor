
count = 0
lineno = 0

with open("train_triplets.txt") as file:
	for line in file:
		count+=int(line.split("\t")[2])
		if (count % 1000000 == 0):
			print count, lineno
		lineno+=1

print count

