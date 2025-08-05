import caengine
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

MAP_NAME = 'larger3'
PRESSURE_MODEL = False
TICKS = 250

f = open(f'maps/{MAP_NAME}.txt', "r")
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

def stateToVis():
    global current_grid
    visual_grid = np.zeros_like(current_grid)
    for value, category in stateToCategory.items():
        visual_grid[current_grid == value] = category
    return visual_grid

def animUpdate(frame):
    mid = 16
    # if(frame == 0 or frame == int(mid/2) or frame == mid):
    #     plt.savefig(f'imgs/exp_{MAP_NAME}_{frame:03d}.png')
    # if(frame == int((((TICKS-mid))*0.333)+mid) or frame == int(((TICKS-mid)*0.667)+mid) or frame == TICKS-1):
    #     plt.savefig(f'imgs/cont_{MAP_NAME}_{frame:03d}.png')
    global current_grid
    visual_grid = stateToVis()
    img.set_array(visual_grid)
    ax.set_title(f"Slime Mold Cellular Automaton - Generation {frame+1}")
    for i in range(rows):
        for j in range(cols):
            text = caengine.biToCell(current_grid[i][j])

            texts[i][j].set_text(text)
            texts[i][j].set_color('white' if text == 'o' else 'black')
            # ax.text(j, i, text, 
            #         ha='center', va='center', 
            #         color=text_color,
            #         fontsize=14,
            #         fontweight='bold')
    current_grid = caengine.cycle(current_grid, pressure=PRESSURE_MODEL)
    return [img] + [text for row in texts for text in row]

start_time = time.time()
bimap = caengine.mapToBi(map, pressure=PRESSURE_MODEL)
animap = bimap.copy()

print('Starting map: ')
printMap(bimap, isInputBinary=True, printBinary=False,)
# for i in range(num_cycles): 
#     bimap = caengine.cycle(bimap, pressure=PRESSURE_MODEL)
#     # print(f'tick {i}:')
#     # printMap(bimap, printBinary=True)
# # print('\nEnd map (decimal): ')
# # print(bimap)
# print('\nEnd map (binary): ')
# printMap(bimap, isInputBinary=True, printBinary=True, pressure=PRESSURE_MODEL)
# print('\nEnd map (symbolic): ')
# printMap(bimap, isInputBinary=True, printBinary=False, pressure=PRESSURE_MODEL)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.8f}s")


# RUNNER CODE FOR ANIMATION: 
symbol_map = {
    0: {'values': [0b0011], 'color': 'grey', 'label': 'Wall'},
    1: {'values': [0b0100,0b0101,0b0110,0b0111,0b1100,0b1101,0b1110,0b1111], 'color': 'yellow', 'label': 'Live'},
    2: {'values': [0b0001],'color': 'red', 'label': 'Source'}, 
    3: {'values': [0b0010],'color': 'red', 'label': 'Sink'}, 
    4: {'values': [0b0000, 0b1000],'color': 'black', 'label': 'Empty'} 
}

# creating a mapping from state values to categories
stateToCategory = {}
for category, data in symbol_map.items():
    for value in data['values']:
        stateToCategory[value] = category
print(stateToCategory[0b0010])

# Create colormap
categories = symbol_map.keys()
colors = [symbol_map[cat]['color'] for cat in categories]
cmap = ListedColormap(colors)

# Set up figure
fig, ax = plt.subplots(figsize=(8, 8), constrained_layout=True)
ax.set_xticks([])
ax.set_yticks([])

current_grid = animap.copy()

img = ax.imshow(stateToVis(), cmap=cmap, vmin=min(symbol_map), vmax=max(categories))
ax.set_title("Cellular Automata Simulation - Generation 0")

# Add grid lines
ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
ax.grid(which='minor', color='black', linestyle='-', linewidth=0.5)
ax.tick_params(which='minor', size=0)

# character representation set-up (mostly for testing)
texts = [[None for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        state = current_grid[i, j]
        texts[i][j] = ax.text(
            j, i, caengine.biToCell(animap[i][j]),
            ha='center', va='center',
            color='white' if state == 'o' else 'black',
            fontsize=10
        )

# Add legend
legend_elements = [Patch(facecolor=symbol_map[i]['color'], label=symbol_map[i]['label']) 
                  for i in range(len(symbol_map))]
ax.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left')

# fig.show()
print('before anim map: ')
printMap(bimap, isInputBinary=True, printBinary=False,)

animation = FuncAnimation(fig, animUpdate, frames=TICKS, interval=40, blit=False, repeat=False)

#set conditional to 1 to display animation, 0 to save animation
if 1 : 
    plt.tight_layout()
    plt.show()
else:
    animation.save(f'animations/smca_{MAP_NAME}_{end_time}.mp4', writer='ffmpeg', fps=5, dpi=300)