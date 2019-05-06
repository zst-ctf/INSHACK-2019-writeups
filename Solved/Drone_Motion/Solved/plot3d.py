#!/usr/bin/env python3
# INS'HACK 2019 - Drone Motion

# https://matplotlib.org/gallery/mplot3d/scatter3d.html
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
# https://matplotlib.org/examples/mplot3d/lines3d_demo.html
# https://stackoverflow.com/questions/12904912/how-to-set-camera-position-for-3d-plots-using-python-matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
import re

# Data for a three-dimensional line
with open('sensors.log') as f:
	log = f.readlines()

# Keep track of current position
ax = plt.axes(projection='3d')
x_abs = 0.0
y_abs = 0.0
z_abs = 0.0

# Process each line of the log file
for item in log:
	if 'dir' not in item:
		continue

	# Get relative direction
	m = re.match(r".*dir: \(x=(.+),y=(.+),z=(.+)\).*", item)
	x_dir = float(m.group(1))
	y_dir = float(m.group(2))
	z_dir = float(m.group(3))

	# Calculate next position
	x_abs += x_dir
	y_abs += y_dir
	z_abs += z_dir
	# print(x_dir, y_dir, z_dir)

	# Draw line from previous position to next
	ax.plot(
		xs=[x_abs-x_dir, x_abs],
		ys=[y_abs-y_dir, y_abs],
		zs=[z_abs-z_dir, z_abs])

# Adjust graph camera, top view
ax.view_init(elev=90.0, azim=-90.0)
# Adjust graph camera, expand plot size
plt.subplots_adjust(left=-.25, right=1.25, top=0.90, bottom=0.70, wspace=0.2, hspace=0.2)
# Display graph
plt.show()
