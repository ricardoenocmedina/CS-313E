"""
File: Spiral.py

Description: 

Student Name: Ricardo Medina

Student UT EID: Ricardo Medina

Course Name: CS 313E
"""

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral ( n ):
  """Function to create a spiral matrix with """

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
    

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):
  pass

def main():
  mat = create_spiral(11)
  print_mat(mat)
  # read the input file

  # create the spiral

  # add the adjacent numbers

  # print the result

if __name__ == "__main__":
  main()