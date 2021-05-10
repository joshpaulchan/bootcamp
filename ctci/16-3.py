# 16.3 Intersection: Given two straight line segments (represented as a start point and an end point), compute the point of intersection, if any.


class Point:
  
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"({self.x}, {self.y})"

class Line:
  def __init__(self, start, end):
    self.start = start
    self.end = end

# Find x, y where A = B



def find_derivative(b, a):
  if a.x == b.x:
    return math.Inf
  return (a.y - b.y) / (a.x - b.x)


def solve_offset(slope, point):
  return point.y - slope * point.x


def find_intersection(line_a, line_b):
  m_a = find_derivative(line_a.start, line_a.end)
  m_b = find_derivative(line_b.start, line_b.end)

  if m_a == m_b:
    return None

  b_a = solve_offset(m_a, line_a.start)
  b_b = solve_offset(m_b, line_b.start)
  
  x = (b_b - b_a) / (m_b - m_a)
  y = m_a * x + b_a
  
  return Point(x, y)


def test_find_intersections():
  A = Line(Point(0, 0), Point(10, 10))
  B = Line(Point(10, 10), Point(0, 0))

  intersection = find_intersection(A, B)
  print(intersection)