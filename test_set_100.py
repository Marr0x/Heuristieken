#   test_set_100.py
#
#   Heuristics - Case: Fruit fly
#   Authors: Mercylyn Wiemer (10749306), Shan Shan Huang (10768793) & Marwa Ahmed (10747141)
#
#   Test set

from data import load_data
import random

def random_genome_list(length):
    genome_list = []
    genome25 = load_data.load_genome("genome_length25.txt")
    #
    while len(genome_list) < length:
        genome_random = genome25[:25]
        random.shuffle(genome_random)

        if genome_random not in genome_list:
            genome_list.append(genome_random)

    return genome_list
