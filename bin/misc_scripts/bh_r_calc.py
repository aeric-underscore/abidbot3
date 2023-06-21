# quick unintegrated script for calculating the black hole radius and diameter
# only need to change the name of the .3d file
# 
# used for getting the bh_radius for calculating grid seeds
# and getting the bh_diameter used to calculating a scale bar



import numpy as np

bh_f=open("bh1_000000.3d", "r")   # change file name here

bh_lines = bh_f.readlines()
cm_x = 0.; cm_y = 0.; cm_z = 0.
for i in range(len(bh_lines)):
    if i == 0: continue
    line_values = bh_lines[i].split()
    cm_x += float(line_values[0])
    cm_y += float(line_values[1])
    cm_z += float(line_values[2])
cm_x /= len(bh_lines) - 1
cm_y /= len(bh_lines) - 1
cm_z /= len(bh_lines) - 1
values = []
mag_summed = 0.
for i in range(len(bh_lines)):
    if i == 0: continue
    line_values = bh_lines[i].split()
    x = float(line_values[0])
    y = float(line_values[1])
    z = float(line_values[2])
    mag= np.sqrt((x-cm_x)**2 + (y-cm_y)**2 + (z-cm_z)**2)
    mag_summed+=mag
average_radius = mag_summed/(len(bh_lines) - 1)
print("radius: " + str(average_radius))
print("diameter: " + str(average_radius * 2))
bh_f.close()