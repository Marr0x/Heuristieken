# https://www.geeksforgeeks.org/cocktail-sort/
# python program for implementation of Cocktail sort

def cocktailSort (genes):
	
	n = len(genes)
	swapped = True
	start = 0
	end = n - 1

	count = 0

	while (swapped == True):

		# reset the swapped flag on entering the loop, because it might 
		# be true from a previous iteration.
		swapped = False 

		# loop from left to right same as the bubble sort
		for i in range (start, end):
			if (genes[i]> genes[i + 1]):
				genes[i], genes[i + 1] = genes[i + 1], genes[i]
				swapped = True
				count += 1

		# if nothing moved, then the array is sorted
		if (swapped == False):
			break

		# otherwise, reset the swapped flag so that it can be used in the next stage
		swapped = False

		# move the end point back by one, because item at the 
		# end is in its rightful spot
		end = end - 1

		# from right to left, doing the same comparison as in the previous stage 
		for i in range(end - 1, start - 1, -1):
			if (genes[i] > genes[i + 1]):
				genes[i], genes[i + 1] = genes[i + 1], genes[i]
				swapped = True
				count += 1

		# increase the starting point, because the last stage would have moved the 
		# next smalles number to its rightful spot.
		start = start + 1

		print(count)

		# driver code to test above 
if __name__ == "__main__":
		genes_melanogaster = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13,
							14, 15, 16, 17, 21, 3, 4, 9]

		cocktailSort(genes_melanogaster)
		# print("Sorted array is:")
		# for i in range(len(genes_melanogaster)):
		# 	print("% d " % genes_melanogaster[i])

