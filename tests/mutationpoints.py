# def distance(n1, n2):
#     """
#     Calculates the difference between two integersself.
#     Returns boolean.
#     """

#     distance = abs(n1 - n2)

#     return distance

def mutationpoints(genome):

    mutationpoints = 0

    for gene in genome:
        solution_index = gene - 1
        gene_index = genome.index(gene)

        if gene_index != solution_index:
            mutationpoints += abs(solution_index - gene_index)

    return mutationpoints
 
