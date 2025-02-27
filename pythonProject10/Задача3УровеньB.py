import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

R = 3
r = 1

theta = np.linspace(0, 2 * np.pi, 35)
phi = np.linspace(0, 2 * np.pi, 35)

theta, phi = np.meshgrid(theta, phi)

x = (R + r * np.cos(theta)) * np.cos(phi)
y = (R + r * np.cos(theta)) * np.sin(phi)
z = r * np.sin(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, color='coral', alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Тор (Бублик)')

ax.set_box_aspect([1, 1, 0.4])

plt.show()