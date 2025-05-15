import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import rules
import re
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
            elements = re.findall(r'(\d+)(\w)', cell)[0]
            capacity = int (elements[0])
            cellType = elements[1]
            #print(cellType)
            dir = cellType#[0]

            prefix = capacity << 3
            if dir == 'u':
                suffix = 0b100
            elif dir == 'r':
                suffix = 0b110
            elif dir == 'd':
                suffix = 0b110
            elif dir == 'l':
                suffix = 0b111
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
def biToCell(binum, pressure=False, row=-1, col=-1):
  # pressure version includes the capacities in 7 bit state output, otherwise it gives 3 bit concise version without capacity
  if pressure:
    binum = binum % 0b10000000 #Done to remove the contraction bit
    sym = binum % 0b1000
    prefix = (str) (binum >> 3)
    if sym == 0b000:
      return 'o'
    elif sym == 0b001:
        return 's'
    elif sym == 0b010:
        return 'e'
    elif sym == 0b011:
        return 'x'
    else:
        if sym == 0b100:
          suffix = 'u'
        elif sym == 0b101:
          suffix = 'r'
        elif sym == 0b110:
          suffix = 'd'
        elif sym == 0b111:
          suffix = 'l'
        else:
          raise Exception(f'Invalid direction: sym = 0b{sym:03b} and binum = 0b{binum:07b} at: ({row},{col})')
        #print(f'{prefix} + {suffix}, {"".join([prefix, suffix])}')
        return "".join([prefix, suffix])    
  else: #Special characters (start with 0)
    binum = binum % 0b1000
    if binum == 0b000:
        return 'o'
    elif binum == 0b001:
        return 's'
    elif binum == 0b010:
        return 'e'
    elif binum == 0b011:
        return 'x'
    else: #Directions (start with 1)
        #binum = binum[0]
        if binum == 0b100:
            return 'u'
        elif binum == 0b101:
            return 'r'
        elif binum == 0b110:
            return 'd'
        elif binum == 0b111:
            return 'l'
        else:
              raise Exception(f'Invalid Binary: {binum:0b}')
        
# Method which takes a neighborhood state matrix and returns its numerical representation
def stateToBi(nbrhd, isInputBinary=True, pressure=False):
    offset = 4
    #   if pressure:
    #     offset += 3
    # at one point used to account for pressure, no longer
    neighborhood = 0
    r = 0
    for row in nbrhd:
        r += 1
        for i in row:
            cell = ((i % 0b1000)) if isInputBinary else cellToBi(i, pressure=pressure, row=r, col=i)
            neighborhood = (neighborhood << offset) + cell
    return neighborhood

# Method to iterate one tick of the CA, updating per the rulesets set within.
# mat: binary matrix
# pressure: tells method whether or not to use capacity model
def cycle(mat, pressure = False):
    #print(f'CHECKPOINT 0: mat:{mat}')
    new_map = np.copy(mat)
    height = np.size(mat,0)
    width = np.size(mat,1)

    offset = 3
    if pressure:
       offset += 4
       
    contract_value = 2**(offset) # should be either 0b1000 (16) if directional or 0b10000000 (128) if pressure model
    #print(f'CHECKPOINT 1: mat:{mat}')
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

            if pressure:
                cur_pressure = getPressure(center)

            # 2D list representing the neighborhood around the current cell
            cur_state = [[ul, up, ur], [left, center, right], [dl, down, dr]]
            # print('current state: ')
            # [print(x) for x in cur_state]
            #print(f'CHECKPOINT 2: {cur_state}')
            bistate = stateToBi(cur_state, isInputBinary = True, pressure=pressure) #find binary neighborhood state representation

            #Check if expansion vs contraction:
            contract_bit = center >= contract_value  #total is 2^27 for nonpressure, 2^57 for pressure
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

                # if pressure and center == s: # setting pressure at the source to the max value
                #     new_map[i][j] = 0b1111000 + s
                # RULES:
                if (center == 0b000): #TODO: make sure it works when pressure = true
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

                    # set the current cells pressure value to the largest adjacent pressure minus 1
                    if pressure and isLive(new_map[i][j]):
                        new_max = getMaxPressure(cur_state) - 1
                        print(f'max pressure setting {(new_max)} at {i},{j}')
                        if new_max > 0:                           
                            new_map[i][j] += (new_max << 3) 

                #BRANCH TO PROPAGATE CONTRACTION SIGNAL:
                elif ((center == u or center == r or center == d or center == l) and
                      ((0b0010 in cur_state[0] or 0b0010 in cur_state[1] or 0b0010 in cur_state[2]) or # checking if next to the sink
                      (any(x >= contract_value for row in cur_state for x in row)))): #checking if next to other contraction cell
                    # if (x >= contract_value for x in cur_state):
                    #     print(f'success to this one bugcheck')

                            # for i in cur_state:
                            #     for x in cur_state[i]
                        # Contraction
                    #print(f'CONTRACT SIGNALLED AT {i},{j}; TRUTH VALUES: 1:{(0b0010 in cur_state[0] or 0b0010 in cur_state[1] or 0b0010 in cur_state[2])}, 2: {(x >= contract_value for x in cur_state)}')
                    new_map[i][j] = new_map[i][j] + contract_value


            #BRANCH TO UNDERGO CONTRACTION:
            else:
                # Cheatsheet:
                # 00 -> up or o (empty)
                # 01 -> right or s (source)
                # 10 -> down or e (sink)
                # 11 -> left or x (wall)
                o = 0b1000
                e = 0b0010
                ncount = neighborCount(cur_state)

                # if center == 0b1111:
                #     print(f'bistate: {bistate:b}\nmasked:  {(bistate & 68467757040):b}\ncheck:   {13694337840:b}')
                #     printNeighborhood(cur_state)
                print(f'check at {i},{j}: {rules.check4(bistate, cur_state)} for bistate = {bistate:036b} and cur_state =')
                printNeighborhood(cur_state)
                if (isLive(center) and
                    ncount < 2 or # Simple rule if live cells only have less than two live neighbors
                    rules.check1(bistate) or
                    rules.check2(bistate) or
                    rules.check3(bistate) or 
                    rules.check4(bistate, cur_state)
                    ):

                    # print(f'{biToCell(new_map[i][j])}, ncount:{ncount}')
                    new_map[i][j] = o
    return new_map


# takes in a binary representation of a cell and returns true if that cell is live, false otherwise
def isLive(cell, pressure = False):
    if pressure:
        contract = 0b10000000
    else:
        contract = 0b1000
    cell = cell % contract
    return (cell >= 0b0100 and cell <= 0b0111) or (cell == 0b0001) or (cell == 0b0010)

# takes in binary state matrix and a list of cells numbers, returns true if the cells in the matrix at the given numbers (counting from left to right, top to bottom), false otherwise
def areLive(cur_state, cells, pressure = False):
    live = True
    count = 1
    for row in cur_state:
        for i in row:
            if count in cells and not isLive(i, pressure):
                return False
            count += 1
    return True

# Returns the pressure value for one cell, input as binary format
def getPressure(cell):
    return (cell % 0b10000000) >> 3 # modulo to remove contraction bit and then bit shift to remove cell type

# takes in a cell neighborhood in binary format and returns the max pressure of any cell in the neighborhood
def getMaxPressure(nbrhd):
    max = -1
    for row in nbrhd:
        for cell in row:
            p = getPressure(cell)
            if p > max:
                max = p
    return max

def mapToBi(map, pressure = False):
    max_pressure = 0b1111
    height = np.size(map,0)
    width = np.size(map,1)
    bimap = np.zeros((height, width), dtype=int)
    if pressure: #aka if the pressure/capacity is included
        for i in range(height):
            for j in range(width):
                    bimap[i][j] = cellToBi(map[i][j])
                    if (bimap[i][j] == 0b001) or (bimap[i][j] == 0b010):
                        bimap[i][j] += (max_pressure << 3)
            
    else: #only directional model
          for i in range(height):
            for j in range(width):
                   bimap[i][j] = cellToBi(map[i][j])
    return bimap

# bi = integer which is binary representation of a neighborhood state
# pressure = whether or not to use the pressure model
# isCheck = whether the neighborhood represented by 'bi' is a check value or not. used for debugging
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

# Used for debugging, prints a neighborhood given as 3x3 list parameter nbrhd
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
