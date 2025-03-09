import numpy as np
import cellpylib as cpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
matplotlib.use('TkAgg')

seed = cpl.init_simple2d(64, 64)

ca = cpl.evolve2d(seed, timesteps=100, neighbourhood="Moore" , apply_rule=lambda n, c, t: cpl.totalistic_rule(n, k=2, rule=90), memoize='recursive')

cpl.plot2d_animate(ca, interval=200)

# fig, axis = plt.subplots()
# mat = axis.matshow(ca, cmap='binary')
# plt.axis('off')

# def animate(i):
#     mat.set_data(ca[:i+1])
#     return [mat]

# ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit = True, repeat=False)
# plt.show()