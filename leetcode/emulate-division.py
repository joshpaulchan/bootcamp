'''

Topics: BFS LC Questions

LC Medium Questions
https://leetcode.com/problems/evaluate-division/
https://leetcode.com/problems/word-ladder/




Example:

equations = [["a","b"],["b","c"]] -> a/b, b/c
values = [2.0,3.0] -> a/b = 2.0, b/c = 3.0
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
a/c= 6.0  , b/a = 0.5, a/e = -1, a/a = 1, x/x = -1,
[6.00000,0.50000,-1.00000,1.00000,-1.00000]


a   b   a
- x - = -
b   c   c

  2.0  3.0
a -> b -> c =  a/c = 6.0

  2.0
a -> b

 0.5
b -> a

a-> c = 6.0
c -> a = 1/6




Algorithm:
1. Build a graph based on the equations and values. Store edge weights from node to node
 in a map. Also add the inverse if it doesn't already exist.
2. Go through each of the queries one by one, and calculate the value of the query using
BFS. (Go into detail later)
3. Retrieve output of BFS while also saving it into our graph.


BFS Algorithm:
2.1 Intialize a queue and a seen set to prevent revisits.
2.2 Add the initial starting point into the queue. Ex: ["a","c"] -> start: 'a', dest: 'c'
  Want to find the shortest path from start to dest.
2.3 Also store the cumulative product into the queue where the starting point = 1.0
  ex: queue = [('a', 1.0)]
2.4 While queue is not empty or have not reached destination, pop out front of the queue
Check out unvisited neighbors and multiply current product with the current node edge to neighbor. Add the neighbor node into the queue with the new cumulative product.
2.5 Also, you have to make sure you check if you have reached destination, if so store/modify value into the graph to save. Of course, return value in the end.
2.6 If you have no path to destination, return -1


Edge cases: 
1. If start or destination doesn't exist in graph, return -1
2. if start == destination: return 1


Time Complexity: O(N * Q) - where N is the number of unique variables, where Q is the number of queries

1. Build a graph -> O(N)
2. BFS -> O(N)
3. Going through each query, O(N) * Q -> O(N + Q)

Space Complexity: O(N^2) - if everything is connected and you store that relationship into the graph
'''

import collections
def evaluateDivision(equations, values, queries):

  # Build graph
  graph = collections.defaultdict(collections.defaultdict)
  for i in range(len(equations)):
    u, v = equations[i]
    value = values[i]
    graph[u][v] = value
    graph[v][u] = 1 / value


  # Create BFS Function
  def bfs(start, destination):

    if start not in graph or destination not in graph:
      return -1.0
    if start == destination:
      return 1.0
    if start in graph and destination in graph[start]:
      return graph[start][destination]
    
    queue = collections.deque([(start, 1.0)])
    seen = set([start])

    while queue:
      node, product = queue.popleft()

      if node == destination:
        graph[start][destination] = product
        graph[destination][start] = 1 / product
        return product

      for nei in graph[node]:
        if nei not in seen:
          edge = graph[node][nei] # graph[a][b] = 2.0
          queue.append((nei, product * edge)) # (b, 1.0 * 2.0)
          seen.add(nei)
    return -1.0

  # Go through each query and save result
  result = []
  for start, dest in queries:
    result.append(bfs(start, dest))

  return result


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
output = [6.00000,0.50000,-1.00000,1.00000,-1.00000]

print(evaluateDivision(equations, values, queries))