"""
[1, 1, 1, 3]

index = 0
val = 1
adjacent = 1
this next = 2

"""

from functools import lru_cache

def cached_dp_rob(numbers: list) -> int:
  @lru_cache(maxsize=None)
  def loot(index: int) -> int:
    if index >= len(numbers):
      return 0
    else:
      return max(numbers[index] + loot(index + 2), loot(index + 1))
      
  x = loot(0)
  print(x)
  return x


def iter_rob(numbers: list) -> int:
  """
  0 - store1 = 1 | store2 = 0
  1 - store1 = 1 | store2 = 1
  2 - store1 = 2 | store2 = 1
  3 - store1 = 8 | store2 = 2

  """

  store1 = 0
  store2 = 0

  for number in numbers:
    current = store1
    store1 = max(number + store2, store1)
    store2 = current

  return store1



def rob(nums: list) -> int:
    
  # total_sum = 0
  adjacent_value = 0
  this_next_value = 0
  
  i = 0 

  while i + 2 <= len(nums) -1:
    # adjacent_value = total_sum + nums[i+1]
    # this_next_value = total_sum + nums[i] + nums[i+2]
    adjacent_value = nums[i+1]
    this_next_value = nums[i] + nums[i+2]
    
    if this_next_value > adjacent_value:
      i+=3
      total_sum = this_next_value
    else:
      i += 2
      total_sum = adjacent_value

          
  if i == len(nums) - 2: 
    total_sum += nums[len(nums) - 1]
      
  if len(nums) == 1:
    total_sum += nums[0]
  
  if len(nums) == 2:
    return max(nums)

  return total_sum



def test_rob(rob):
  print(f"rob currently returns: {iter_rob([1,1,1,3])}")
  assert iter_rob([1,1,1,2]) == 3
  print(f"passed {iter_rob.__name__}")
  

x = "hello"
print(" {0} {1} ".format(x, "hello"))
print(f" {x} ")


test_rob(rob)
