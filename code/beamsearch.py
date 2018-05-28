from classes.Fruitfly import Fruitfly
import numpy as np
import heapq

def beamsearch(root_genome):

    print("root genome:", root_genome)

    solved = False
    solution = root_genome.solution()

    queue = []
    priority_queue = []
    queue.append(root_genome)

    while not solved:

        # get current node with least points
        genome = queue.pop(0)

        # show path to solution, when solution found
        if genome == solution:
            solved = True
            print("Solution found in generation: ",
                  genome.get_generation())

            path = genome.path_solution()
            print("Path to solution: ")

            for inversion in range(len(path)):
                print("Inversion: {:2d}".format(inversion), path[inversion])

        else:

            children = genome.create_children(Fruitfly.breakpoint_compare)

            for child in children:
                heapq.heappush(priority_queue, child)
                print(child.get_generation())

            for child in range(2):
                best = heapq.heappop(priority_queue)
                queue.append(best)


def main():
    root_genome = [1,2,3,4,5]
    np.random.shuffle(root_genome)
    # root_genome = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
    fly = Fruitfly(root_genome)
    beamsearch(fly)

if __name__ == '__main__':
    main()