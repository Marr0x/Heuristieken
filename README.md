# Heuristics - Case: Fruit fly #

The goal of this project is to find the evolutionary path between two fruit fly species. The genes of the fruit flies Drosophila Melanogaster and Drosophila Miranda are identical. The only difference between the genomes of the two species is that the genes are sorted in a different order due to mutations (Picture 1). Mutations occur when segments of the gene reverse. In the current project our aim is to find which series of mutations led to the genome of one of the species from the other one. More series are possible, but our goal is to find the most plausible one: the series with the smallest and the least mutations.

Picture 1.
![genomes fruit flies](http://heuristieken.nl/wiki/images/0/03/Tweegenomen.gif)


For more information about the case:
[Heuristieken Fruitvlieg](http://heuristieken.nl/wiki/index.php?title=Fruitvliegen)

## Getting Started ##

### Requirements ###
- Python 3.6.5
- Numpy 1.14.3

### Code ###
This folder holds all the scripts: algorithms, classes, and helper functions.

- Classes:
    - Fruitfly Class: This class consists of attributes of a fruitfly, such as
                      the genes, the geneartion, the parent of a fruitfly, and
                      how many breakpoints, distancepoints, mutationpoints a
                      fruitfly has. In addition it contains methods that can make
                      fruitfly children.
 
- Best-first Search: Finds a path between fruitflies by constantly
  selecting "best" fruitfly child based on the following:
    - Breakpoints: When there are two non-consecutive numbers.
    - Distancepoints: How far an gene is from solution genome.
    - Combinationpoints: Combines breakpoints and distancepoints.
    - Mutationpoints: How large an inversion is. In the evolution small inversions
        are more likely than large inversions.

- Branch and Bound (depth-first) with breakpoints: searches for a path between fruitflies
  by selecting the "best" two children based on breakpoints.

- Helpers.py is an helper script that for example loads a data genome.

### Data ###
This folder holds all the data used for this case.
    - genome_length25.txt: contains the genome of drosophila melanogaster with a length of 25 genes.

## Usage ##
main.py is the main script that is responsible for finding the evolutionary path between two fruitfly species. 

Asks user to choose a genomeset:
1. Drosophila melanogaster genome of length 25.
2. Random genome of a chosen length between 5-25.

Asks user to choose an algorithm:
1. Branch and Bound: breakpoints.
2. Best-first search: breakpoints.
3. Best-first search: distancepoints.
4. Best-first search: mutationpoints.
5. Best-first search: combinationpoints.

Notes:
- It is not recommended to use the Branch and Bound to find a solution with a large random
genome, because of the long runtime.
- It is not recommended to use Best-first search: mutationpoints to find a solution with
a large genome, because of the long runtime.

## Authors ##
- Marwa Ahmed
- Shan Shan Huang
- Mercylyn Wiemer

## Acknowledgements ##
UvA - Minor Progammeren
