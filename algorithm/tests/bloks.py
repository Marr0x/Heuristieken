# blokken van 4, 3, 2 swappen

def BubbleSort(genes):
	
	n = len(genes)	

	count = 0
	mutatiepunten = 0
	
	for i in range (n):
		for j in range (n - 3):
			# blok van 4 
			if genes[j] > genes[j + 3]:
				genes[j], genes[j + 3] = genes[j + 3], genes[j]
				genes[j + 1], genes[j + 2] = genes[j + 2], genes[j + 1]
				count += 1
				mutatiepunten += 3
				# print(genes[j])
			# blok van 3
			elif genes[j] > genes[j + 2]:
				genes[j], genes[j + 2] = genes[j + 2], genes[j]
				count += 1
				mutatiepunten += 2
				# print(genes[j])
			# blok van 2
			elif genes[j] > genes[j + 1]:
				genes[j], genes[j + 1] = genes[j + 1], genes[j]
				count += 1
				mutatiepunten += 1
			# print(genes[j])
		# print("####################")
	print(j)
	print("count =", end ='')
	print(count)
	print("mutatiepunten =", end = '')
	print(mutatiepunten)

if __name__ == "__main__":
	genes_melanogaster = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13,
							14, 15, 16, 17, 21, 3, 4, 9]

BubbleSort(genes_melanogaster)