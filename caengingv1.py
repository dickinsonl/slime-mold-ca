import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#import ffmpeg
#from IPython.display import HTML
#import matplotlib.animation as animation

# Function which takes in a cell state and returns a binary literal of that state
# 6 bits for a (verbose) state
# First four bits: either the capacity or if all zeroes then selecting the 2nd (base) option for the next 2 bits:
# 00 -> up or o (empty)
# 01 -> right or s (source)
# 10 -> down or e (sink)
# 11 -> left or x (wall)
# Directional cells formatted as either u, r, d, l suffixed by a number 1-16 indicating the capacity/pressure at the cell, e.g. 'u12', 'd03', 'l11'
def cellToBi(cell, verbose=False):
    #Verbose version includes the capacities in 6 bit state output, otherwise it gives 3 bit concise version without capacity
    if verbose:
      if cell == 'o':
          return 0b000000
      elif cell == 's':
          return 0b000001
      elif cell == 'e':
          return 0b000010
      elif cell == 'x':
          return 0b000011
      else:
          dir = cell[0]
          cap = int(cell[1:])
          prefix = cap << 2
          if dir == 'u':
            suffix = 0b00
          elif dir == 'r':
            suffix = 0b10
          elif dir == 'd':
            suffix = 0b10
          elif dir == 'l':
            suffix = 0b11
          else:
            print('Invalid direction')
            return -1
          return prefix + suffix
    else:
      if cell == 'o':
          return 0b000
      elif cell == 's':
          return 0b001
      elif cell == 'e':
          return 0b010
      elif cell == 'x':
          return 0b011
      else:
          cell = cell[0]
          if cell == 'u':
              return 0b100
          elif cell == 'd':
              return 0b101
          elif cell == 'l':
              return 0b110
          elif cell == 'r':
              return 0b111
          else:
              raise Exception('Invalid Symbol')
          
def stateToBi(nbrhd, verbose=False):
  if verbose:
    offset = 6
  else:
    offset = 3

  neighborhood = 0
  for row in nbrhd:
    for i in row:
        cell = cellToBi(i)
        neighborhood = (neighborhood << offset) + cell
  return neighborhood

def cycle(mat):
    new_map = np.copy(mat)
    height = np.size(mat,0)
    width = np.size(mat,1)
    for i in range(height):
        for j in range(width):
            #Use strings for now i guess but should possibly change these to binary later for speed
            up = mat[i-1][j] if i > 0 else 'x'
            down = mat[i+1][j] if i < (height-1) else 'x'
            left = mat[i][j-1] if j > 0 else 'x'
            right = mat[i][j+1] if j < (width-1) else 'x'
            #ul = upper left, etc
            ul = mat[i-1][j-1] if i > 0 and j > 0 else 'x'
            ur = mat[i-1][j+1] if j < (width-1) and i > 0 else 'x'
            dl = mat[i+1][j-1] if j > 0 and i < (height-1) else 'x'
            dr = mat[i+1][j+1] if i < (height-1) and j < (width-1) else 'x'
            center = mat[i][j]

            #Concat all of these starting with up, going clockwise, ending with the center
            cur_state = [[ul, up, ur], [left, center, right], [dl, down, dr]]
            # print('current state: ')
            # [print(x) for x in cur_state]
            bistate = stateToBi(cur_state) #find binary neighborhood state representation

            #rules
            if center == 'o':
                # print(f'(i,j): {i}, {j}, bistate: {(bistate)}, Binary: {bin(bistate)}')
                if bistate in [50430656, 56722112]:
                    new_map[i][j] = 'l'
                elif bistate in [57409544]:
                    new_map[i][j] = 'u'
                elif bistate in [820739]:
                    new_map[i][j] = 'r'
                elif bistate in [2097371, 2195675, 52527323,52528859]:
                    new_map[i][j] = 'd'
                elif bistate in [32768, 2097152, 512, 8]:
                    new_map[i][j] = 1
                elif bistate in [57443843, 2885339, 50430683, 57508040, 57508544, 57411083, 820955, 52527323]:
                    new_map[i][j] = 1
            #elif center == '1':
    return new_map

def animate(frames, intrvl, mat):
    fig, ax = plt.subplots(figsize=(10,10))
    # ims = []

    # for i in range(frames):
    #     im = plt.imshow(mat, animated=True, cmap='Greys')
    #     ims.append([ims])
    #     mat = cycle(mat)
    # plt.close
    a = FuncAnimation(mat, cycle, interval = 50, repeat = True)
    plt.show
