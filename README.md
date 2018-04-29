# Heuristics - Case: Fruit fly #

The goal of this project is to find the evolutionary path between two fruit fly species. The genes of the fruit flies Drosophila Melanogaster and Drosophila Miranda are identical. The only difference between the genomes of the two species is that the genes are sorted in a different order due to mutations (Picture 1). Mutations occur when segments of the gene reverse. In the current project we are going to find which series of mutations led to the genome of one of the species from the other one. More series are possible, but our goal is to find the most plausible one: the series with the smallest and the least mutations.

Picture 1.
![genomes fruit flies](http://heuristieken.nl/wiki/images/0/03/Tweegenomen.gif)


For more information about the case:
[Heuristieken Fruitvlieg](http://heuristieken.nl/wiki/index.php?title=Fruitvliegen)

## Getting Started ##

### Requirements ###
- Python 3.x

### Code ###
This folder holds all the scripts, including algorithms and for loading the data.
- Depth First Branch and bound

### Data ###
This folder holds all the data used for this case, including textfiles with the genomes of the fruitfly species.

## Usage ##
main.py is the main script that is responsible for calculating the evolutionary path between two fruitfly species. It expects an array of numbers that represents the genes of a fruitfly as input. An algorithm can be chosen to calculate a series of mutations that led to the genome of one fruitfly to the other.

## Authors ##
- Marwa Ahmed
- Shan Shan Huang
- Mercylyn Wiemer

## Acknowledgements ##
UvA - Minor Progammeren
