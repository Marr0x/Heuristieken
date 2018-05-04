def rev(genes, x, y):
  """ reverses a list of genes
    genes = the list of integers
    x  = index of list where reversion should start
    y = index of list where reversion should end"""
  
  new_genes = genes[:]

  if x is 0:
    new_genes[:y+1] = new_genes[y::-1]
    return new_genes
  elif y < len(genes):
    new_genes[x:y+1] = new_genes[y:x-1:-1]
    return new_genes
  else:
    print("error1")


def main():

  genes = [5,4,3,2,1]
  n = len(genes)

  # iterates over genes, decreasing every time
  for i in range(n - 1 , 0, -1):

    # x is the index of where the reversion starts
    # y is the index of where the reversion ends
    for j in range(0, i):

      x = n - 1 - i
      y = j + (n - i)

      R = rev(genes, x, y)

      # prints out reversed list
      print(R) 

if __name__ == "__main__":
  main()

