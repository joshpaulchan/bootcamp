

# 16.5 Factorical Zero
# Write an algorithm which computes the number of trailing zeros in `n` factorial


# Solution 1. Calculate the factorial and then count number of least significant zeros
import math

def factorial(n):
  amt = 1
  for i in range(1, n):
    amt *= i
  return amt

def factorial_zero(n):
  fact = math.factorial(n)
  str_fact= str(fact)
  count = 0
  # for s in str_fact[::-1]:
  #   if s == '0':
  #     count += 1
  #   else:
  #     break

  # alternative: mod and don't use string
  while fact > 0 and fact % 10 == 0:
    count += 1
    fact /= 10
  return count


def factorial_zero_five(n):
  return n // 5


def test_factorial_zero(factorial_zero):
  # 5! -> 120 -> 1
  # 8! -> 8x7x6x... = 40320 -> f(40320) -> 1
  # 10! -> 3,628,800 -> f() -> 2
  assert factorial_zero(3) == 0
  assert factorial_zero(5) == 1
  assert factorial_zero(8) == 1
  assert factorial_zero(10) == 2
  assert factorial_zero(12) == 2

  print(f"{factorial_zero.__name__} worked")

test_factorial_zero(factorial_zero)
test_factorial_zero(factorial_zero_five)

