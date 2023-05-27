#####################################################################
# parameter files for doing radiative transfer parameter searches
#####################################################################

# dump directory #
dump_dir = "/home/leon.chan/sgra-sims/Ma+0.94_w5"

# image directory #
img_dir = "/home/leon.chan/sgra-imgs/Ma+0.94_w5"

# figure directory #
fig_dir = "/home/leon.chan/sgra-figs/Ma+0.94_w5"

###########################################################

#camera location along the polar direction#
thetacam = [90, 0.1, 30, 60, 120, 150, 179.9]

# sets of rlow-rhigh to be fit#
rhigh = [180, 10, 50, 90, 120, 150, 200]

# arrays for plotting domain
domain = [20, 50, 100, 500, 1000]

###########################################################
# section for munit #

# starting munit #
mstart = 17

# ending munit#
mend = 21

# number of munit #
mpoint = 10

###########################################################
# section for rlow #

# number of rlow #
nrlow = 10

# limit of r low#
rlow_min = 50

###########################################################