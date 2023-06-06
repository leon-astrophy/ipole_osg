################################################################################
#
# Once having luminosities of a series of snapshot given from GRRT calculation
# This script calculates the modulation index M3 of the desired wavelength flux
# Written by Ho Sang (Leon) Chan on 6.6.2023
# The Chinese University of Hong Kong and University of Colorado
#
################################################################################

#import#
import os
import h5py
import pandas as pd
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

# figure directory #
fig_dir = params.fig_dir

# variability #
var_dir = params.var_dir

################################################################################
# section for munit #

# mass accretion rate #
m_index = np.linspace(params.mstart, params.mend, params.mpoint, endpoint=True)
m_index = np.array([round(x, 1) for x in m_index]).astype(float)
m_rate = 10**(m_index)

################################################################################
# get ndarray#

# for mean and sigma #
mean = np.ndarray(shape=(params.nrlow,params.mpoint), dtype=float)
sigma = np.ndarray(shape=(params.nrlow,params.mpoint), dtype=float)

################################################################################
# the main fitting loop #

# now run the process#
for i in range (0, 1):#len(params.thetacam)):
  for j in range (0, 1):#len(params.rhigh)):

    ############################################################################
    #make folder#
    angle_folder = img_dir+'/theta_'+str(params.thetacam[i])
    rhigh_folder = angle_folder+'-rhigh_'+str(params.rhigh[j])
    make_folder(rhigh_folder)

    #we limit ourself to small rlow#
    rlow_lim = min(params.rlow_min, params.rhigh[j])

    # create list of rlow #
    rlow = np.linspace(1, rlow_lim, params.nrlow, endpoint=True)
    rlow = np.array([round(x, 1) for x in rlow]).astype(float)

    ############################################################################
    # loop over rlow #
    for k in range (0, len(rlow)):
      for l in range (0, len(m_rate)):

        #mrate folder#
        rlow_folder = rhigh_folder+'/rlow_'+str(rlow[k])
        mrate_folder = rlow_folder+'-mrate_'+str(m_index[l])
        make_folder(mrate_folder)

        #read all files in the folder#
        filename = list(Path(mrate_folder).glob("*.h5"))

        # itemdata #
        itemdata = [path.as_posix() for path in filename]

        ########################################################################
        #empty array#
        lum_tmp = []
   
        #loop over and read the luminosity#
        for q in range (0, len(itemdata)):
          imag = h5py.File(itemdata[q],'r')
          lum = imag['Ftot_unpol'][()]
          lum_tmp.append(lum)

        #get mean and sigma#
        mean[k,l] = np.average(lum_tmp)
        sigma[k,l] = np.std(lum_tmp)

    ############################################################################
    #pandas#
    mean = pd.DataFrame(mean)
    sigma = pd.DataFrame(sigma)

    # save #
    figure_folder = var_dir+'/theta_'+str(params.thetacam[i])+'-rhigh_'+str(params.rhigh[j])
    make_folder(figure_folder)

    #save#
    mean.to_csv(figure_folder+'/mean.csv', header=False, index=False)
    sigma.to_csv(figure_folder+'/sigma.csv', header=False, index=False)

################################################################################
