################################################################################
# wrapper for passing variables to submit.py to perform parameter searches
################################################################################

#import#
import os
import numpy as np
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

################################################################################
# section for munit #

# mass accretion rate #
m_index = np.linspace(params.mstart, params.mend, params.mpoint, endpoint=True)
m_index = np.array([round(x, 1) for x in m_index]).astype(float)
m_rate = 10**(m_index)

################################################################################
# the main fitting loop #

# now run the process#
for i in range (0, 1):#len(params.thetacam)):
  for j in range (0, 1):#len(params.rhigh)):

    #make folder#
    angle_folder = img_dir+'/theta_'+str(params.thetacam[i])
    rhigh_folder = angle_folder+'-rhigh_'+str(params.rhigh[j]) 
    make_folder(rhigh_folder)
  
    #we limit ourself to small rlow#
    rlow_lim = min(params.rlow_min, params.rhigh[j])

    # create list of rlow #
    rlow = np.linspace(1, rlow_lim, params.nrlow, endpoint=True)  
    rlow = np.array([round(x, 1) for x in rlow]).astype(float)

    #loop over rlow#
    for k in range (0, len(rlow)):
      for l in range (0, len(m_rate)):

        #make folder#
        rlow_folder = rhigh_folder+'/rlow_'+str(rlow[k])
        mrate_folder = rlow_folder+'-mrate_'+str(m_index[l]) 
        make_folder(mrate_folder)

        #adjust input#
        dump_in = dump_dir
        img_in = mrate_folder
        rlow_in = rlow[k]
        rhigh_in = params.rhigh[j]
        munit_in = m_rate[l]
        theta_in = params.thetacam[i]

        #submit ipole job#
        call(['python3', '../src/submit.py', 
              str(dump_in), str(img_in), str(rlow_in), str(rhigh_in), str(munit_in), str(theta_in)])        

################################################################################
