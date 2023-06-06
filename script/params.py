#####################################################################
# parameter files for doing radiative transfer parameter searches
#####################################################################

# dump directory #
dump_dir = "/home/leon.chan/sgra-sims/Ma+0.94_w5"

# image directory #
img_dir = "/home/leon.chan/sgra-imgs/Ma+0.94_w5"

# figure directory #
fig_dir = "/home/leon.chan/sgra-figs/Ma+0.94_w5"

# for studying variability #
var_dir = "/home/leon.chan/sgra-vars/Ma+0.94_w5"

# discrete list#
dicr_dir = "/home/leon.chan/dicr_dir/Ma+0.94_w5"

# one set of snapshot figure#
oneset_dir = "/home/leon.chan/oneset_dir/Ma+0.94_w5"

# queueing list #
queue_dir = "/home/leon.chan/ipole-osg-python/var"

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
mpoint = 20

# step size in munit#
mstep = 0.1

###########################################################
# section for rlow #

# number of rlow #
nrlow = int((mend - mstart)/mstep + 1)

# limit of r low#
rlow_min = 60

###########################################################
