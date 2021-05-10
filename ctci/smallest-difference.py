


# 16.6 Smallest Difference
# Given two arrays of integrrs, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the diff

'''

{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8} 

       v
1 2  3 11 15 18

  v
8 19 23 127 235

'''

def find_diff(arr1, arr2):

  # NlogN
  arr1.sort()
  # MlogM
  arr2.sort()

  i = 0
  j = 0

  ans = float('inf')

  # N + M
  while i < len(arr1) and j < len(arr2):

    curr_diff = abs(arr1[i] - arr2[j])
    ans = min(ans, curr_diff)

    if arr1[i] == arr2[j]:
      return 0
    elif arr1[i] < arr2[j]:
      i += 1
    else:
      j += 1

  return ans


def test_small_diff(find_diff):

  assert find_diff(
  [1, 3, 5, 11, 2],
  [23, 127, 235, 19, 8]
  ) == 3
  assert find_diff(
  [1, 2, 4, 6, 8, 10],
  [10, 8, 6, 4, 2, 1]
  ) == 0

  print(f"{find_diff.__name__} worked")

test_small_diff(find_diff)


