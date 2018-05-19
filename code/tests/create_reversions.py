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

	new_genes = genes[:]

	if x is 0:
		new_genes[:y+1] = new_genes[y::-1]
		return new_genes
	elif y < len(genes):
		new_genes[x:y+1] = new_genes[y:x-1:-1]
		return new_genes
	else:
		print("error1")


def main():

	genes = [5,4,3,2,1]
	n = len(genes)

	print("genes: {}".format(genes))

	count = 0

	# iterates over genes, decreasing every time
	for i in range(n - 1 , 0, -1):
		print("aantal: {}".format(i))

		# x is the index of where the reversion starts
		# y is the index of where the reversion ends
		for j in range(0, i):

			x = n - 1 - i
			y = j + (n - i)
			print("[{}, {}]".format(x, y))

			R = rev(genes, x, y)

			count += 1

			# prints out reversed list
			print(R)

		print("\n")

	print(count)

if __name__ == "__main__":
	main()
