#!/usr/bin/env python
def greedy(genoom):
    """
    This program searched for the optimal trades to make: by looking at 
    existing breakpoints.
    """
    #
    # for i, j in enumerate(genoom[:-1]):
        # if j  == genoom[i+1]:
        #     genoom[i] = "foo"
        #     genoom[i+1] = "foo"

    print(genoom)

def distance(n1, n2):
    """
    Calculates the difference between two integersself.
    Returns boolean.
    """

    distance = abs(n1 - n2)

    if distance == 1:
        print(1)

        return True
    print(2)
    return False

if __name__ == "__main__":
    genoom = [1, 3, 2, 5, 4]
    # greedy(genoom)
    distance(3, 2)
    distance(1, 3)
