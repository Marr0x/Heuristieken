# main.py
#
# Heuristics - Case: fruit flies
# Authors: Marwa Ahmed, Shan Shan Huang & Mercylyn wiemer
#
# Implements algorithms to find the evolutionary path between fruit fly species.
from algorithm.classes.Fruitfly import Fruitfly

def main ():

	genome = input("Please enter the filename with a genome \n")

	genome1 = Fruitfly(genome)
	genome1.print_genes()

	genome1.smallest_first_sort()
	genome1.print_genes()

if __name__ == "__main__":
	main()
