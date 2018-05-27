def sort(genes):

    highest_number = len(genes)
    high_position = highest_number - 1

    position = genes.index(highest_number)
    # print(position)

    # print(highest_number)

    for i in range(highest_number):
        highest_number += i
        
        if position is not highest_number - 1:
            genes[position], genes[highest_number - 1] = genes[highest_number - 1], genes[position]
            count =+ 1
        print(i)

    print(count)
    print(genes)




if __name__ == "__main__":
	# genes_melanogaster = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13,
	# 						14, 15, 16, 17, 21, 3, 4, 9]

    genen = [2, 4, 5, 3, 1]

sort(genen)
