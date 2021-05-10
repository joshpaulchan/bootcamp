"""
Can Place Flowers
https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed =0[1,0,0,0,1]0, n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

[0000000]
[1010101]
[101010101]

[1, 0, 1, 0, 1, 0, 1, 0]
1/0   1, 0, 1, 0, 1, 0, 1  1/0
[0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0]


"""
class CPFlowers:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
      if n == 0:
        return True
      # add to end of list to account for last real value of list
      flowerbed.append(0)
      # assume you passed a zero at the beginning, to account for first real value of list
      count = 1
      for flower in flowerbed:
        if flower == 0:
          count += 1
        else:
          count = 0
        
        if count == 3:
          n -= 1
          count = 1

        if n == 0:
          return True

      return False
       

ans = CPFlowers()
print(ans.canPlaceFlowers([0, 0, 0, 0, 0, 0, 0], 4))