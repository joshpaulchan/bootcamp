"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

import math
import queue

def distance_away(a, b):
  return sum(0 if a[i] == b[i] else 1 for i in range(len(a)))

def test_distance_away(distance_away):
  assert distance_away("hot", "hot") == 0
  assert distance_away("hot", "dot") == 1
  assert distance_away("hot", "dog") == 2

# test_distance_away(distance_away)

def is_word_one_distance_away(a, b):
  return len(a) == len(b) and distance_away(a, b) == 1

def test_is_word_one_distance_away(is_word_one_distance_away):
  assert not is_word_one_distance_away("hot", "hot")
  assert is_word_one_distance_away("hot", "dot")
  assert not is_word_one_distance_away("hot", "dog")

# test_is_word_one_distance_away(is_word_one_distance_away)

def build_word_graph(words):
  """
  O(nlogn)
  """
  graph = {}
  for i in range(len(words)):
    for j in range(len(words)):
      if i == j or words[i] == words[j]: 
        continue

      if not words[i] in graph:
        graph[words[i]] = set()

      if not words[j] in graph:
        graph[words[j]] = set()

      if words[j] in graph[words[i]]:
        continue
      
      if is_word_one_distance_away(words[i], words[j]):
        graph[words[i]].add(words[j])
        graph[words[j]].add(words[i])
        # building a duplicated, undirected graph
  
  return graph
 
""""
# graph = {
# 
# 
# }
"""

def djikstra(graph, begin, end):
  """
  Steven TBD
  """
  return []


def bfs(graph, begin, end):
  """
  Vats TBD
  """
  return []


def dfs(graph, begin, end):
  return []


class WeightedGraph:

  def __init__(self, dict_graph):
    self.dict_graph = dict_graph

  def neighbors(self, node):
    return self.dict_graph.get(node, set())

  def cost(self, start, end):
    return 1 if end in self.dict_graph.get(start) else math.inf


def reconstruct_path(came_from, start, end):
    current = end
    path = []
    while current and current != start:
        path.append(current)
        current = came_from.get(current)
    path.append(start) # optional
    path.reverse() # optional

    return path


def a_star(graph, begin, end):
  graph = WeightedGraph(graph)
  perimeter = queue.PriorityQueue()
  perimeter.put((0, begin))

  came_from = { begin : None }
  cost_so_far = { begin : 0 }

  while not perimeter.empty():
    priority, current = perimeter.get()

    if current == end:
      break

    for node in graph.neighbors(current):
      new_cost = cost_so_far[current] + graph.cost(current, node)
      
      if node not in cost_so_far or new_cost < cost_so_far[node]:
          cost_so_far[node] = new_cost

          # TODO: the heuristic is to minimize the search path (euclidean distance in the list? distance from node to node? current path size?) basically Djikstra's if the heuristic is constant for at every node vs goal 
          # not very fast, but basically...

          heuristic = len(reconstruct_path(came_from, begin, node))

          priority = new_cost + heuristic
          perimeter.put((priority, node))
          came_from[node] = current
        
  return reconstruct_path(came_from, begin, end)


def ladder_length(begin_word, end_word, word_list, get_shortest_path):
  graph = build_word_graph(word_list + [begin_word])
  
  print(graph)

  if end_word not in graph:
    return 0
  
  shortest_path = get_shortest_path(graph, begin_word, end_word)

  print(shortest_path)

  return len(shortest_path)


def test_ladder_length(ladder_length, shortest_path):
  print(f"Testing {ladder_length.__name__} with {shortest_path.__name__}...")

  assert ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"], shortest_path) == 5

  assert ladder_length("hit", "cog", ["hot","dot","dog","lot","log"], shortest_path) == 0

  print(f"Passed {ladder_length.__name__} with {shortest_path.__name__}.")


for strategy in [djikstra, bfs, dfs, a_star]:
  try:
    test_ladder_length(ladder_length, strategy)
  except Exception as e:
    print(e)
