"""
https://leetcode.com/problems/target-sum/

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation:                                        6+9 > 5 > 6-9 
                          [1,2,3,4,5].         [[1,2,3],[4,5]] = 5  
-1+1+1+1+1 = 3            1+2+3+4+5 = 15         6    9
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.


Cache: 

  Final = 3

pass 1: 

1 ->  1 | -1


"""

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

      solution_dict = {0: 1}
      
      
        




      return helper(S, 0)






class GetConfigurations:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

      def helper(S: int, index: int):





      return helper(S, 0)