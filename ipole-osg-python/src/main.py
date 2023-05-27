#############################################################
# this is main.py python file which act as a testing module
# to try passing terminal variables to the submit.py script
#############################################################

#import#
from subprocess import call, DEVNULL 

#############################################################
# set parameters #

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

#############################################################
# main function #

# call submit.py #
call(['python3', 'submit.py', str(dump_dir), str(img_dir), str(rlow), str(rhigh), str(munit), str(thetacam)])

#############################################################
