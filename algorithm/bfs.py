from classes.Fruitfly import Fruitfly

def bfs(root):
    """ Breadth-First Search (bfs): in progress. """

    solution = Fruitfly([1, 2, 3, 4, 5])
    queue = [root]
    solved = False;

    print(queue)

    while not solved:
        genome = queue.pop(0)
        next_generation = genome.create_children()

        for child in next_generation:
            if child == solution:
                solved = True
                solution_child = child
                print('parent {}'.format(child.get_parent()))
                print('generation {}'.format(child.get_generation()))
                print('solution {}'.format(child))
            else:
                queue.append(child)

    # print(queue)
    print('parent solution {}'.format(solution_child.path_solution()))
