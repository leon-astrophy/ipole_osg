####################################################################################
#
# this python script generate parameter list to /var that will be load by submit.sh
# this script generates only parameter list only for one set of 
# (Rlow, Rhigh, Munit, theta)
# Written by Ho Sang (Leon) Chan on 6.6.2023
# The Chinese University of Hong Kong and the University of Colorado
#
####################################################################################

#import#
import os
import numpy as np
from pathlib import Path
from subprocess import call, DEVNULL

# parameter files #
import params

################################################################################
# define function #

# make folder #
def make_folder(dir_in):
  isExist = os.path.exists(dir_in)
  if not isExist:
    os.makedirs(dir_in)

################################################################################
# base parameter, you can change these according to your task #

# dump directory #
dump_dir = params.dump_dir

# image directory #
img_dir = params.img_dir

# var list directory #
queue_dir = params.queue_dir

# directory for outputing one set of GRRT snapshot #
dicr_dir = params.dicr_dir

################################################################################
# section for free parameters #

#rlow#
rlow = '10'

#rhigh#
rhigh = '160'

#munit#
m_index = 19
m_rate = str(10**(m_index))

#inclination#
thetacam = '90'

################################################################################
#make folder#
angle_folder = img_dir+'/theta_'+str(thetacam)
rhigh_folder = angle_folder+'-rhigh_'+str(rhigh)
make_folder(rhigh_folder)

################################################################################
# openfile #
f = open(queue_dir+'/varlist', "w")

################################################################################

#make folder#
rlow_folder = rhigh_folder+'/rlow_'+str(rlow)
mrate_folder = rlow_folder+'-mrate_'+str(m_index)
make_folder(mrate_folder)

#adjust input#
dump_in = dump_dir
img_in = mrate_folder
rlow_in = rlow
rhigh_in = rhigh
munit_in = m_rate
theta_in = thetacam

################################################################################
# GRMHD snapshot name  #
filename = list(Path(dump_in).glob("*.h5"))

#arrays for directory##
dp_dirs = [path.as_posix() for path in filename]
dp_name = [path.name for path in filename]
ig_dirs = [os.path.join(img_in, path.name) for path in filename]

#write#
for o in range (0, len(dp_dirs)):
  f.write(str(rlow_in)+','+str(rhigh_in)+','+str(munit_in)+','+str(theta_in)
          +','+ str(dp_dirs[o])+','+str(dp_name[o])+','+str(ig_dirs[o])+'\n')

################################################################################
#close file#
f.close()

################################################################################

