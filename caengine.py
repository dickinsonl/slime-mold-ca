import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import rules
#import ffmpeg
#from IPython.display import HTML
#import matplotlib.animation as animation

# Function which takes in a cell state and returns a binary literal of that state
# 6 bits for a (pressure) state
# First four bits: either the capacity or if all zeroes then selecting the 2nd (base) option for the next 2 bits:
# 00 -> up or o (empty)
# 01 -> right or s (source)
# 10 -> down or e (sink)
# 11 -> left or x (wall)
# Directional cells formatted as either u, r, d, l suffixed by a number 1-16 indicating the capacity/pressure at the cell, e.g. 'u12', 'd03', 'l11'
def cellToBi(cell, pressure=False, row=-1, col=-1):
    #pressure version includes the capacities in 6 bit state output, otherwise it gives 3 bit concise version without capacity
    if pressure:
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
          elif cell == 'r':
              return 0b101
          elif cell == 'd':
              return 0b110
          elif cell == 'l':
              return 0b111
          else:
              raise Exception(f'Invalid Symbol: {cell} at ({row}, {col})')
          
# Input is binary representation of a cell, output is the character for that cell.
# Currently this does not display if a cell is contracting or expanding
def biToCell(bin, pressure=False):
  # pressure version includes the capacities in 6 bit state output, otherwise it gives 3 bit concise version without capacity
  if pressure:
    bin = bin % 0b1000000 
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
        cap = bin >> 2 #This and the next line could probably be consolidated to one pretty easily
        prefix = cap << 2
        if sym == 0b00:
          suffix = 'u'
        elif sym == 0b01:
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
    bin = bin % 0b1000 
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
            return 'r'
        elif bin == 0b110:
            return 'd'
        elif bin == 0b111:
            return 'l'
        else:
              raise Exception(f'Invalid Binary: {bin:b}')
        
# Method which takes a neighborhood state matrix and returns its numerical representation
def stateToBi(nbrhd, isInputBinary=True, pressure=False):
  offset = 4
  if pressure:
    offset += 3

  neighborhood = 0
  r = 0
  for row in nbrhd:
    r += 1
    for i in row:
        cell = i if isInputBinary else cellToBi(i, row=r, col=i)
        neighborhood = (neighborhood << offset) + cell
  return neighborhood

# Method to iterate one tick of the CA, updating per the rulesets set within.
# mat: binary matrix
# pressure: tells method whether or not to use capacity model
def cycle(mat, pressure = False):
    new_map = np.copy(mat)
    height = np.size(mat,0)
    width = np.size(mat,1)

    offset = 4
    contract_value = 0b1000
    if pressure:
       offset += 3
       contract_value = 0b10000000 #TODO: CHECK TO MAKE SURE THIS VALUE IS RIGHT

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
            contract_bit = center >= 2**(offset-1) #total is 2^27 for nonpressure, 2^57 for pressure
            u = 0b0100
            r = 0b0101
            d = 0b0110
            l = 0b0111
            s = 0b0001
            if not contract_bit: #In effect, checking to see if first bit is set to 0 (for expansion) or 1 (for contraction)
                # Cheatsheet:
                # 00 -> up or o (empty)
                # 01 -> right or s (source)
                # 10 -> down or e (sink)
                # 11 -> left or x (wall)
                

                # RULES:
                if biToCell(center) == 'o':
                    #print(f'(i,j): {i}, {j}, bistate & mask: {(bistate)}, Binary: {bin(bistate)}')
                    # Rule format is (bistate & mask) == check
                    if (((bistate & 983280) == 16) or 
                        ((bistate & 983280) == 64) or 
                        ((bistate & 983280) == 112) or 
                        ((bistate & 983280) == 80) or 
                        ((bistate & 983280) == 96)):
                        new_map[i][j] = u # UP               
                    elif (((bistate & 16711680) == 1048576) or 
                          ((bistate & 16711680) == 4194304) or 
                          ((bistate & 16711680) == 7340032) or 
                          ((bistate & 16711680) == 5242880) or 
                          ((bistate & 16711680) == 6291456)):
                        new_map[i][j] = r # RIGHT
                    elif (((bistate & 4027514880) == 268435456) or 
                          ((bistate & 4027514880) == 1073741824) or 
                          ((bistate & 4027514880) == 1879048192) or 
                          ((bistate & 4027514880) == 1342177280) or 
                          ((bistate & 4027514880) == 1610612736)):
                        new_map[i][j] = d # DOWN
                    elif (((bistate & 1044480) == 4096) or 
                          ((bistate & 1044480) == 16384) or 
                          ((bistate & 1044480) == 28672) or 
                          ((bistate & 1044480) == 20480) or 
                          ((bistate & 1044480) == 24576)):
                        new_map[i][j] = l # LEFT

                #BRANCH TO PROPAGATE CONTRACTION SIGNAL:
                elif ((center == u or center == r or center == d or center == l) and 
                      ((0b0010 in cur_state[0] or 0b0010 in cur_state[1] or 0b0010 in cur_state[2]) or # checking if next to the sink
                      (any(x >= contract_value for row in cur_state for x in row)))): #checking if next to other contraction cell
                    # if (x >= contract_value for x in cur_state):
                    #     print(f'success to this one bugcheck')
                        
                            # for i in cur_state:
                            #     for x in cur_state[i]
                        # Contraction
                    print(f'CONTRACT SIGNALLED AT {i},{j}; TRUTH VALUES: 1:{(0b0010 in cur_state[0] or 0b0010 in cur_state[1] or 0b0010 in cur_state[2])}, 2: {(x >= contract_value for x in cur_state)}')
                    new_map[i][j] = new_map[i][j] + contract_value

                
            #BRANCH TO UNDERGO CONTRACTION:
            else:
                # Cheatsheet:
                # 00 -> up or o (empty)
                # 01 -> right or s (source)
                # 10 -> down or e (sink)
                # 11 -> left or x (wall)
                o = 0b0000
                e = 0b0010
                ncount = neighborCount(cur_state)
                
                # if center == 0b1111:
                #     print(f'bistate: {bistate:b}\nmasked:  {(bistate & 68467757040):b}\ncheck:   {13694337840:b}')
                #     printNeighborhood(cur_state)

                if (isLive(center) and
                    ncount < 2 or # Simple rule if live cells only have less than two live neighbors                   
                    rules.check1(bistate) or
                    rules.check2(bistate) or
                    rules.check3(bistate)
                    ):
                    
                    # print(f'{biToCell(new_map[i][j])}, ncount:{ncount}')
                    new_map[i][j] = o
    return new_map

def isLive(cell, pressure = False):
    contract = 0b1000
    cell = cell % contract
    return (cell >= 0b0100 and cell <= 0b0111)

def mapToBi(map, pressure = False):
    height = np.size(map,0)
    width = np.size(map,1)
    bimap = np.zeros((height, width), dtype=int)
    if pressure: #aka if the pressure/capacity is included
        raise Exception("Error, pressure mode not yet implemented")
    else: #only directional model
          for i in range(height):
            for j in range(width):
                   bimap[i][j] = cellToBi(map[i][j])
    return bimap

def biToState(bi, pressure=False, isCheck=False):
  if pressure:
    offset = 0b10000000
    shift = 7
  else:
    offset = 0b10000
    shift = 4
  neighborhood = [['','',''],
                  ['','',''],
                  ['','','']]
  for j in [2,1,0]:
    row = neighborhood[j]
    for i in [2,1,0]:
        bicell = bi % offset
        bi = bi >> shift
        cell = biToCell(bicell, isCheck)
        #print(f"Cell: {cell}")
        row[i] = cell
  return neighborhood

# Used for debugging, prints a neighborhood given as parameter nbrhd
def printNeighborhood(nbrhd, pressure=False):
    for row in nbrhd:
        print(biToCell(row[0], pressure) + biToCell(row[1], pressure) + biToCell(row[2], pressure))
    print()

# Count the number of live cells in the neighborhood
def neighborCount(nbrhd, pressure=False):
    count = 0
    contract = 0b1000
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                n = nbrhd[i][j] % contract
                if (n >= 0b100 and n <= 0b111) or (n == 0b10 or n == 0b01):
                    count += 1
    return count
#WIP:
# def animate(frames, intrvl, mat):
#     fig, ax = plt.subplots(figsize=(10,10))
    # ims = []

    # for i in range(frames):
    #     im = plt.imshow(mat, animated=True, cmap='Greys')
    #     ims.append([ims])
    #     mat = cycle(mat)
    # plt.close
    # a = FuncAnimation(mat, cycle, interval = 50, repeat = True)
    # plt.show
