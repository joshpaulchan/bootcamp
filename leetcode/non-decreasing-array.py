"""
665. Non-decreasing Array

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).


Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
 

Constraints:

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105


num[i] <= next num

[-1, 4, 2, 3]
  0  1  2  3
    
4, 2, 3

[3, 4, 2, 5, 2]

"""


def checkPossibility(nums: list) -> bool:

  num_changes = 0

  for index in range(1, len(nums)):
    if nums[index - 1] > nums[index]:
      num_changes += 1
      
      if num_changes > 1:
        return False
      elif index < 2 or nums[index - 2] <= nums[index]:
        nums[index - 1] = nums[index]
      else:
        nums[index] = nums[index - 1]

  return True

# def checkPossibility(nums: list) -> bool:

#   num_changes = 0

#   for index, n in enumerate(nums):
#     if nums[index] > nums[min(index + 1, len(nums) -1)]:
#       num_changes += 1

#       nums[index] = nums[index-1]

#       if not nums[index - 1] <= nums[index] <= nums[index+1]:
#         return False

#       if num_changes > 1:
#         return False
  
#   return True

def test_solution(func):
  
  assert func([4, 2, 3]) == True
  print("Test 1 Passed.")
  assert func([4, 2, 1]) == False
  print("Test 2 Passed.")
  assert func([3, 4, 2, 3]) == False
  print("Test 3 Passed.")
  assert func([-1, 4, 2, 3]) == True
  print("Test 4 Passed.")

  print("Success!")


test_solution(checkPossibility)