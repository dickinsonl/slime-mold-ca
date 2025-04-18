import caengine
import time
import numpy as np

start_time = time.time()
MAP_NAME = 'med2.txt'
f = open(MAP_NAME, "r")
num_cycles = 40
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

def printMap(map, isInputBinary=True, printBinary=False):
    if isInputBinary:
        if printBinary: 
          # This is the only branch of the conditional that prints here, otherwise printing is done at the end
          for i in range(rows):
              for j in range(cols):
                  print(f"{map[i][j]:04b}", end=' ')
              print()
          return
        newmap = np.empty((rows, cols), dtype=str)
        for i in range(rows):
            for j in range(cols):
                newmap[i][j] = caengine.biToCell(map[i][j])
                #print(f'old: {map[i][j]:04b}, new:{newmap[i][j]}')
    elif printBinary:
        newmap = np.empty((rows, cols), dtype=int)
        for i in range(rows):
            for j in range(cols):
                newmap[i][j] = caengine.cellToBi(map[i][j])

    #Doing the actual printing            
    for i in range(rows):
        line = ''
        m = newmap if isInputBinary else map
        for j in m[i]:
            line = line + j + ' '
        print(line)

bimap = caengine.mapToBi(map)
printMap(bimap, isInputBinary=True)
for i in range(num_cycles): 
    bimap = caengine.cycle(bimap,)
print(bimap)
printMap(bimap, isInputBinary=True, printBinary=True)
printMap(bimap, isInputBinary=True, printBinary=False)

#caengine.animate(2,50,map)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.8f}s")