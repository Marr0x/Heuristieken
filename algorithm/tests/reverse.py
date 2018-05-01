# reverse.py
#
# Heuristieken
#
# Names: Marwa Ahmed, Mercylyn Wiemers, Shan Shan Huang
# 
# This program makes every possible reversion of a list of integers

def rev(genes, x, y):
	""" reverses a list of genes
		genes = the list of integers
		x  = index of list where reversion should start
		y = index of list where reversion should end"""
	
	# dit werkt nog niet. Hij schrijft genes over
	genes[x:y+1] = genes[y:x-1:-1]

	new_genes = list(genes)

	return new_genes


def main():

	# er wordt nog geen reversed lijst teruggegeven
	# maar de for loops en het indexeren werken!

	genes = [4,5,3,2,1]
	n = len(genes)

	print("genes: {}".format(genes))

	# iterates over genes, decreasing every time
	for i in range(n - 1 , 0, -1):
		print("aantal: {}".format(i))

		# x is the index of where the reversion starts
		# y is the index of where the reversion ends
		for j in range(0, i):

			x = n - 1 - i
			y = j + 1
			print("[{}, {}]".format(x, y))

		print("\n")

if __name__ == "__main__":
	main()

