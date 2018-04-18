# fruitfly.py
# 
# Heuristieken - Case: fruitflies
# Authors: Marwa Ahmed, Shan Shan Huang & Mercylyn wiemer
# 
# Datastrictire of the fruitfly case


class Fruitfly:

	def __init__(self, genes = [12, 34, 45, 34]):
		self.genes = genes

	def print_genes(self):
		print(self.genes)

	# def bubbesort(self, genes):

def main ():

	set1 = Fruitfly()
	set1.print_genes()

if __name__ == "__main__":
	main()