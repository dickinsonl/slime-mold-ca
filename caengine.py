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
def cellToBi(cell, verbose=False, row=-1, col=-1):
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
    else: #Special cellstates (start with 0)
      if cell == 'o':
          return 0b000
      elif cell == 's':
          return 0b001
      elif cell == 'e':
          return 0b010
      elif cell == 'x':
          return 0b011
      else: #Directions(start with 1)
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
              raise Exception(f'Invalid Symbol: {cell} at ({row}, {col})')
          
# Input is binary representation of a cell, output is the character for that cell.
def biToCell(bin, verbose=False):
  # Verbose version includes the capacities in 6 bit state output, otherwise it gives 3 bit concise version without capacity
  if verbose:
    if bin == 0b000000:
      return 'o'
    elif bin == 0b000001:
        return 's'
    elif bin == 0b000010:
        return 'e'
    elif bin == 0b000011:
        return 'x'
    else:
        sym = bin % 0b100
        cap = bin >> 2
        prefix = cap << 2
        if sym == 0b00:
          suffix = 'u'
        elif sym == 0b10:
          suffix = 'r'
        elif sym == 0b10:
          suffix = 'd'
        elif sym == 0b11:
          suffix = 'l'
        else:
          print('Invalid direction')
          return -1
        return prefix + suffix
  else: #Special characters (start with 0)
    if bin == 0b000:
        return 'o'
    elif bin == 0b001:
        return 's'
    elif bin == 0b010:
        return 'e'
    elif bin == 0b011:
        return 'x'
    else: #Directions (start with 1)
        #bin = bin[0]
        if bin == 0b100:
            return 'u'
        elif bin == 0b101:
            return 'd'
        elif bin == 0b110:
            return 'l'
        elif bin == 0b111:
            return 'r'
        else:
              raise Exception(f'Invalid Binary: {bin:b}')
        
# Method which takes a neighborhood state matrix and returns its numerical representation
def stateToBi(nbrhd, isInputBinary=True, verbose=False):
  offset = 4
  if verbose:
    offset += 3

  neighborhood = 0
  r = 0
  for row in nbrhd:
    r += 1
    for i in row:
        cell = i if isInputBinary else cellToBi(i, row=r, col=i)
        neighborhood = (neighborhood << offset) + cell
  return neighborhood

# Method to iterate one tick of the CA, updating per the rulesets set within
def cycle(mat, verbose = False): # TODO: CHANGE THIS METHOD TO ASSUME MAT IS IN BINARY
    new_map = np.copy(mat)
    height = np.size(mat,0)
    width = np.size(mat,1)
    for i in range(height):
        for j in range(width):
            #Use strings for now i guess but should possibly change these to binary later for speed
            up = mat[i-1][j] if i > 0 else 0b011 #binary for a wall
            down = mat[i+1][j] if i < (height-1) else 0b011
            left = mat[i][j-1] if j > 0 else 0b011
            right = mat[i][j+1] if j < (width-1) else 0b011
            #ul = upper left, etc
            ul = mat[i-1][j-1] if i > 0 and j > 0 else 0b011
            ur = mat[i-1][j+1] if j < (width-1) and i > 0 else 0b011
            dl = mat[i+1][j-1] if j > 0 and i < (height-1) else 0b011
            dr = mat[i+1][j+1] if i < (height-1) and j < (width-1) else 0b011
            center = mat[i][j]

            #Concat all of these starting with up, going clockwise, ending with the center
            cur_state = [[ul, up, ur], [left, center, right], [dl, down, dr]]
            # print('current state: ')
            # [print(x) for x in cur_state]
            bistate = stateToBi(cur_state) #find binary neighborhood state representation

            #Check if expansion vs contraction:
            size = 2**27 #2^27 for nonverbose, 2^57 for verbose
            if bistate < size: #In effect, checking to see if first bit is set to 0 (for expansion) or 1 (for contraction)
                # Cheatsheet:
                # 00 -> up or o (empty)
                # 01 -> right or s (source)
                # 10 -> down or e (sink)
                # 11 -> left or x (wall)
                # RULES:
                if biToCell(center) == 'o':
                    # print(f'(i,j): {i}, {j}, bistate: {(bistate)}, Binary: {bin(bistate)}')
                    if ((bistate & 28728) == 8) or ((bistate & 28728) == 32) or ((bistate & 28728) == 56) or ((bistate & 28728) == 40) or ((bistate & 28728) == 48):
                        new_map[i][j] = 0b100                
                    elif ((bistate & 258048) == 32768) or ((bistate & 258048) == 131072) or ((bistate & 258048) == 229376) or ((bistate & 258048) == 163840) or ((bistate & 258048) == 196608):
                        new_map[i][j] = 0b101
                    elif ((bistate & 14708736) == 2097152) or ((bistate & 14708736) == 8388608) or ((bistate & 14708736) == 14680064) or ((bistate & 14708736) == 10485760) or ((bistate & 14708736) == 12582912):
                        new_map[i][j] = 0b110
                    elif ((bistate & 32256) == 512) or ((bistate & 32256) == 2048) or ((bistate & 32256) == 3584) or ((bistate & 32256) == 2560) or ((bistate & 32256) == 3072):
                        new_map[i][j] = 0b111
                #elif ((bistate & 56) == 16) or ((bistate & 229376) == 65536) or ((bistate & 14680064) == 4194304) or ((bistate & 3584) == 1024):
                   # Contraction
                   # new_map[i][j] = 'c'+center  
    return new_map

def mapToBi(map, verbose = False):
    height = np.size(map,0)
    width = np.size(map,1)
    bimap = np.zeros((height, width), dtype=int)
    if verbose: #aka if the pressure/capacity is included
        raise Exception("Error, verbose mode not yet implemented")
    else: #only directional model
      for i in range(height):
        for j in range(width):
           bimap[i][j] = cellToBi(map[i][j])
    return bimap
      
      

#WIP:
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
