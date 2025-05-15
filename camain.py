import caengine
import time
import numpy as np


MAP_NAME = 'small1.txt'
PRESSURE_MODEL = False
TICKS = 12

f = open(MAP_NAME, "r")
num_cycles = TICKS
cols = int(f.readline()) #int(input()) 
rows = int(f.readline()) #int(input()) 
map = [0]*rows

for i in range(rows):
   map[i] = f.readline().split()#str(input)
   #map[i].pop()
   
   #finds & stores coords of agent, blockages, and sample locations
#    for j in range(cols):
#       if map[i][j] == "@":
#          agent = [i,j]
#       if map[i][j] == "#":
#          blocked.append([i,j])
#       if map[i][j] == "*":
#          samp.append([i,j])

def printMap(map, isInputBinary=True, printBinary=False, pressure=False):
    offset = 4 + (4*int(pressure))
    if isInputBinary:
        if printBinary:
          # This is the only branch of the conditional that prints here, otherwise printing is done at the end
          for i in range(rows):
              for j in range(cols):
                  print(f"{map[i][j]:0{offset}b}", end=' ')
              print()
          return
        newmap = [[None for _ in range(cols)] for _ in range(rows)] 
        for i in range(rows):
            for j in range(cols):
                #print(f'prelim {caengine.biToCell(map[i][j], pressure, i, j)}')
                newmap[i][j] = caengine.biToCell(map[i][j], pressure, i, j)
                #print(f'post {newmap[i][j]}')
    elif printBinary:
        newmap = np.empty((rows, cols), dtype=int)
        for i in range(rows):
            for j in range(cols):
                newmap[i][j] = caengine.cellToBi(map[i][j], pressure, i, j)

    #Doing the actual printing
    for i in range(rows):
        line = ''
        m = newmap if isInputBinary else map
        for j in m[i]:
            line = line + j + ' '
        print(line)

start_time = time.time()
bimap = caengine.mapToBi(map, pressure=PRESSURE_MODEL)
print('Starting map: ')
printMap(bimap, isInputBinary=True, printBinary=True,)
for i in range(num_cycles): 
    bimap = caengine.cycle(bimap, pressure=PRESSURE_MODEL)
    # print(f'tick {i}:')
    # printMap(bimap, printBinary=True)
# print('\nEnd map (decimal): ')
# print(bimap)
print('\nEnd map (binary): ')
printMap(bimap, isInputBinary=True, printBinary=True, pressure=PRESSURE_MODEL)
print('\nEnd map (symbolic): ')
printMap(bimap, isInputBinary=True, printBinary=False, pressure=PRESSURE_MODEL)

#caengine.animate(2,50,map)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.8f}s")