################################################################################
#
# Once GRRT one set of snapshots for one set of (Rlow, Rhigh, Munit, theta)
# This python script plot the GRRT images and the origion of emission 
# of the GRMHD simulations
# Written by Ho Sang (Leon) Chan on 6.6.2023
# The Chinese University of Hong Kong and the University of Colorado
#
################################################################################

#import#
import os
import h5py
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
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

# directory for outputing one set of GRRT snapshot #
dicr_dir = params.dicr_dir

# one set of snapshot output directory #
oneset_dir = params.oneset_dir

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
# the main fitting loop #

#make folder#
angle_folder = dicr_dir+'/theta_'+str(thetacam)
rhigh_folder = angle_folder+'-rhigh_'+str(rhigh)
make_folder(rhigh_folder)

#mrate folder#
rlow_folder = rhigh_folder+'/rlow_'+str(rlow)
mrate_folder = rlow_folder+'-mrate_'+str(m_index)
make_folder(mrate_folder)

################################################################################
#read all files in the folder#
filename = list(Path(mrate_folder).glob("*.h5"))

# itemdata #
itemdata = [path.as_posix() for path in filename]
imgsdata = [path.name for path in filename]

################################################################################
# save #
figure_folder = oneset_dir+'/theta_'+str(thetacam)+'-rhigh_'+str(rhigh)+'/rlow_'+str(rlow)+'-mrate_'+str(m_index)
make_folder(figure_folder)

#loop over and read the luminosity#
for q in range (0, len(itemdata)):
  imag = h5py.File(itemdata[q],'r')
  nx = imag['header']['camera']['nx'][()]
  ny = imag['header']['camera']['ny'][()]
  dx = imag['header']['camera']['dx'][()]
  dy = imag['header']['camera']['dy'][()]
  dsource = imag['header']['dsource'][()]
  scale = imag['header']['scale'][()]
  Lunit = imag['header']['units']['L_unit'][()]
  Munit = imag['header']['units']['M_unit'][()]
  freqcgs = imag['header']['freqcgs'][()]
  image = imag['unpol'][:,:] * scale

  #plot#
  COLORMAP = 'afmhot'
  MAXCOLOR = None
  interpolationtype = 'none'
  fovx_uas = dx * Lunit / dsource * 2.06265e11
  fovy_uas = dy * Lunit / dsource * 2.06265e11
  extent = [ -fovx_uas/2., fovx_uas/2., -fovy_uas/2., fovy_uas/2. ]
  if MAXCOLOR is None: MAXCOLOR = image.max()
  im = plt.imshow(image.T,interpolation=interpolationtype,cmap=COLORMAP,origin='lower',vmax=MAXCOLOR,extent=extent)
  plt.colorbar(im)
  plt.savefig(figure_folder+'/'+str(imgsdata[q])+'.png')
  plt.clf()
  plt.close()

################################################################################
