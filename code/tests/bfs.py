from classes.Fruitfly import Fruitfly

def bfs(root):
    """ Breadth-First Search (bfs): in progress. """

    # solution = Fruitfly([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
    solution = Fruitfly([1, 2, 3, 4, 5])
    queue = [root]
    solved = False
    generation = 0

    while not solved and generation < 8:
        genome = queue.pop(0)
        next_generation = genome.create_children()

        generation = next_generation[0].get_generation()

        for child in next_generation:
            if child == solution:
                solved = True
                solution_child = child
                print('solution: {}'.format(child))
                print('solution found in generation: {}'.format(child.get_generation()))
            else:
                queue.append(child)

    # print(queue)
    print('path: {}'.format(solution_child.path_solution()))
    # print("length of path: {}".format(len(solution_child.path_solution()) - 1))
