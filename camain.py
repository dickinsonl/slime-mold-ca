import caengine
import time

start_time = time.time()
f = open('med1.txt', "r")
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

def printMap(map, binary=True):
    if binary:
        for i in range(rows):
            for j in range(cols):
                map[i][j] = caengine.biToCell(map[i][j])
    for i in range(rows):
        line = ''
        for j in map[i]:
            line = line + j + ' '
        print(line)

bimap = caengine.mapToBi(map)
printMap(bimap)
for i in range(50): 
    bimap = caengine.cycle(bimap)
print()
printMap(bimap)

#caengine.animate(2,50,map)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.8f}s")