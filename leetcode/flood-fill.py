'''
https://leetcode.com/problems/flood-fill/

https://leetcode.com/problems/rotting-oranges/

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

input:
[[1,1,1],
[1,1,0],
[1,0,1]]

Output: 
[[2,2,2],
[2,2,0],
[2,0,1]]

---- Number of islands reference ----
def numIslands(grid:list) -> int:
  row = len(grid)
  col = len(grid[0])

  visited = [[False] * col for _ in range(row)]
  islands = 0

  for i in range(row):
    for j in range(col):
      if grid[i][j] == '1' and not visited[i][j]:
        stack = [(i,j)]
        visited[i][j] = True

        while stack:
          ix, jx = stack.pop()


          for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
            ni = ix + di
            nj = jx + dj


            
            if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == '1' and not visited[ni][nj]:
              stack.append((ni,nj))
              visited[ni][nj] = True
        islands += 1
  return islands



inorder left root right
preorder root left right
postorder left right root

toplogical sort question:
https://leetcode.com/problems/course-schedule-ii/

dynamic programming question:
https://leetcode.com/problems/knight-dialer/


'''
import collections
from collections import deque
def flood(image, sr, sc, newColor):
  if sr not in range(len(image)) or sc not in range(len(image[0])):
    return False

  oldColor = image[sr][sc]
  queue = collections.deque([(sr, sc)])
    
  while queue:
    r, c = queue.popleft()

    image[r][c] = newColor
  
    for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
      next_r = r + di
      next_c = c + dj

      # if not 0 <= next_r < len(image) or not 0 <= next_c < len(image[0]):
      #   continue
  
      if 0 <= next_r < len(image) and 0 <= next_c < len(image[0]):
        if image[next_r][next_c] == oldColor:
          queue.append((next_r, next_c))

  return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

print(flood(image, sr, sc, newColor))