#source: https://jeremykun.com/2013/01/22/depth-and-breadth-first-search/
from collections import deque

def breadth_first(start, last_value):
   visited_nodes = set()
   queue = deque([start])

   while len(queue) > 0:
      node = queue.pop()
      if node in visited_nodes:
         continue

      visited_nodes.add(node)
      if node.value == last_Value:
         return True

      for n in node.adjacent_nodes:
         if n not in visited_nodes:
            queue.appendleft(n)
   return False
