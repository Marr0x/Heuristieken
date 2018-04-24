genes = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

count = 0

for i in range(len(genes) - 1):

	minimum = min(genes[i:])
	minimum_index = genes[i:].index(minimum)

	j = i + minimum_index

	genes[i:j + 1] = reversed(genes[i: j + 1])
	count += 1
	print(genes)

print (count)


