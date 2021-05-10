## 16.4 Tic Tac Win: Design an algorithm to figure out if someone has won a game of tic-tac-toe

def check_has_won(board):
  pass


def test_check_has_won():
  # simple grid

  grid = [
    ["O", "X", "O"],
    ["X", "X", "O"],
    ["O", "O", "X"]
  ]

  print(grid)

  assert not check_has_won(grid, "X")

  # simple grid


  # solution = 2N + 2
  # solutions = { : [] }

  grid = [
    ["O", "X", "O"],
    ["X", "X", "X"],
    ["O", "X", "O"]
  ]
  '''
  
  101 011 100

  '''

  print(grid)

  assert not check_has_won(grid, "X")
  assert check_has_won(grid, "O")

  # large grid

  N = 10

  grid = [
    [
      random.choice(("O", "X")) for n in range(N)
    ] for n in range(N) 
  ]

  print(grid)

  x_has_won = check_has_won(grid, "X")
  o_has_won = check_has_won(grid, "O")
  print(f"Who won? X:{x_has_won} O:{o_has_won}")