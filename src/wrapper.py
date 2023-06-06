################################################################################
#
# This is the python script that generates parameter list to /var
# This is used to test if the HTCondor submission works smoothly
# Written by Ho Sang (Leon) Chan on 6.6.2023
# The Chinese University of Hong Kong and University of Colorado
#
################################################################################

#import#
import os
import sys
import htcondor
from pathlib import Path
from subprocess import call, DEVNULL 

#############################################################
# set parameters #

#varlist directroy#
var_dir = '../var'

# directory#
dump_dir = '../dat'

#output directory#
img_dir = '../imgs'

#rlow#
rlow = '10'

#rhigh#
rhigh = '160'

#munit#
munit = '1e19'

#inclination#
thetacam = '90'

###############################################################
# We extract all GRMHD snapshot filename and create an itemlist

# GRMHD snapshot name  #
filename = list(Path(dump_dir).glob("*.h5"))

#arrays for directory##
dp_dirs = [path.as_posix() for path in filename]
dp_name = [path.name for path in filename]
ig_dirs = [os.path.join(img_dir, path.name) for path in filename]

#open file#
f = open(var_dir+'/varlist', "w")

#write#
for i in range (0, len(dp_dirs)):
  f.write(str(rlow)+','+str(rhigh)+','+str(munit)+','+str(thetacam)+','+
          str(dp_dirs[i])+','+str(dp_name[i])+','+str(ig_dirs[i])+'\n')

#close
f.close()

#############################################################
