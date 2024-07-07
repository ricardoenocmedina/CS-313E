"""
File: Spiral.py

Description: Generate a spiral matix and output the sum of all the numbers adjacent to the inputed number.

Student Name: Ricardo Medina

Student UT EID: rem3885

Course Name: CS 313E
"""

def create_spiral ( n ):
  """Function to create a spiral matrix with """
  # if input is even add 1 to make it odd
  if n % 2 == 0:
    n += 1

  # generates 2D matrix with 0s
  mat = [[0 for x in range(n)] for x in range(n)]

  row_pos = n // 2
  col_pos = n// 2

  mat[row_pos][col_pos] = 1

  x = 1        # slider index
  curr_val = 2 # current value

  # iterate while slider is less than the dimensions
  while x < n:
    
    # fill columns
    for i in range(x):
      col_pos = (col_pos + 1) if (x % 2 != 0) else (col_pos - 1)
      mat[row_pos][col_pos] = curr_val
      curr_val += 1

    # fill rows
    for j in range(x):
      row_pos = (row_pos + 1) if (x % 2 != 0) else (row_pos -1)
      mat[row_pos][col_pos] = curr_val
      curr_val += 1

    x += 1

  # fill last row
  for i in range(n-1):
    col_pos = (col_pos + 1) if (x % 2 != 0) else (col_pos - 1)
    mat[row_pos][col_pos] = curr_val
    curr_val += 1

  return mat

def print_mat(mat):
  """Helper function to print matrix nicely"""
  for row in mat:
    for num in row:
      print('{: <5}'.format(num), end='')
    print()
    

def sum_adjacent_numbers (spiral, n):
  """Returns an interger that is the sum of the numbers adjacent to n in the spiral. If n is outside the range return 0."""
  coordinates = get_index_2d(spiral, n)

  # if n is not in spiral return 0
  try:
    i = coordinates[0]
    j = coordinates[1]

  except:
    return 0 

  dim = -1 
  for item in spiral:
    dim += 1

  sum = 0
  # top row (excluding corners)
  if ((i == 0) and (j > 0) and (j < dim)):
    right = spiral[i][j + 1]
    left = spiral[i][j - 1]
    bottom = spiral[i + 1][j]
    bottom_right = spiral[i + 1][j + 1]
    bottom_left = spiral[i + 1][j - 1]

    sum += (right + left + bottom + bottom_right + bottom_left)

  # bottom row (excluding corners)
  elif ((i == dim) and (j > 0) and (j < dim)):
    right = spiral[i][j + 1]
    left = spiral[i][j - 1]
    top  = spiral[i - 1][j]
    top_left = spiral[i - 1][j - 1]
    top_right = spiral[i - 1][j + 1]

    sum += (right + left + top + top_left + top_right)

  # left-hand side column (excluding corners)
  elif ((j == 0) and (i > 0) and (i < dim)):
    right = spiral[i][j + 1]
    top  = spiral[i - 1][j]
    top_right = spiral[i - 1][j + 1]
    bottom = spiral[i + 1][j]
    bottom_right = spiral[i + 1][j + 1]
    
    sum += (right + top + top_right + bottom + bottom_right)
  
  # right-hand side column (excluding corners)
  elif ((j == dim) and (i > 0) and (i < dim)):
    left = spiral[i][j - 1]
    top  = spiral[i - 1][j]
    top_left = spiral[i - 1][j - 1]
    bottom = spiral[i + 1][j]
    bottom_left = spiral[i + 1][j - 1]

    sum += (left + top + top_left + bottom + bottom_left)

  # top left corner
  elif ((i == 0) and (j == 0)):
    right = spiral[i][j + 1]
    bottom = spiral[i + 1][j]
    bottom_right = spiral[i + 1][j + 1]

    sum += (right + bottom + bottom_right)

  # top right corner
  elif ((i == 0) and (j == dim)):
    left = spiral[i][j - 1]
    bottom = spiral[i + 1][j]
    bottom_left = spiral[i + 1][j - 1]

    sum += (left + bottom + bottom_left)

  # bottom left corner
  elif ((i == dim) and (j == 0)):
    top  = spiral[i - 1][j]
    right = spiral[i][j + 1]
    top_right = spiral[i - 1][j + 1]

    sum += (top + top_right + right)

  # bottom right corner
  elif ((i == dim) and (j == dim)):
    top  = spiral[i - 1][j]
    left = spiral[i][j - 1]
    top_left = spiral[i - 1][j - 1]

    sum += (top + left + top_left)

  # any interger inside of matrix
  else:
    right = spiral[i][j + 1]
    left = spiral[i][j - 1]
    bottom = spiral[i + 1][j]
    top  = spiral[i - 1][j]
    bottom_right = spiral[i + 1][j + 1]
    top_left = spiral[i - 1][j - 1]
    bottom_left = spiral[i + 1][j - 1]
    top_right = spiral[i - 1][j + 1]

    sum += (right + left + bottom + top + bottom_right + bottom_left + top_left + top_right)

  return sum

def get_index_2d(myList, target):
  """Helper function to get the index of a 2D array"""
  for i, x in enumerate(myList):
    if target in x:
      return (i, x.index(target))
    
def main():
  # read the dimension of the grid and value from input file
  dim = int(input())

  # create a 2-D list representing the spiral
  mat = create_spiral(dim)

  while True:
    try:
      sum_val = int(input())

      # find the sum of the adjacent terms
      adj_sum = sum_adjacent_numbers(mat, sum_val)

      # print the terms
      print(adj_sum)
    except EOFError:
      break

if __name__ == "__main__":
  main()