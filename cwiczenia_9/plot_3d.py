import numpy as np
import matplotlib.pyplot as plt 

# GEnerowanie losowych punktów w przestrzeni 3D:
x = np.random.normal(0, 1, 1000)
y = np.random.normal(0, 1, 1000)
z = np.random.normal(0, 1, 1000)

# Tworzenie projekcji 3D:
ax = plt.axes(projection="3d")

# Rysowanie punktów w 3D:
ax.scatter3D(x, y, z, color="green")

plt.show()
