# code >> https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Gnome_sort
# info >> https://en.wikipedia.org/wiki/Gnome_sort


def gnomeSort(genes):

	i = 0
	
	n = len(genes)

	count = 0

	while i < n:
		if i and genes[i] < genes[i - 1]:
			genes[i], genes[i - 1] = genes[i - 1], genes[1]
			i -=1
		else:
			i += 1
		count += 1
	print("count = ", end='')
	print(count)


def teleportingGnomeSort(genes):
	count = 0
	i = j = 0
	n = len(genes)
	while i < n:
		if i and genes[i] < genes[i - 1]:
			genes[i], genes[i - 1] = genes[i - 1], genes[i]
			i -= 1
		else:
			# teleport
			if i < j:
				i = j
			j = i = i + 1
		count += 1
	# print(count)
		# print(i)
		# print('j = ', j)

if __name__ == "__main__":
	genes_melanogaster = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13,
							14, 15, 16, 17, 21, 3, 4, 9]

gnomeSort(genes_melanogaster)
teleportingGnomeSort(genes_melanogaster)
