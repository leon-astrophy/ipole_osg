####################################################
#
# A bash script to submit ipole jobs to HTCondor
# This script load parameter list from /var/varlist
# And then submit jobs according to the parameters
# Written by Ho Sang (Leon) Chan on 6.6.2023
# The Chinese University of Hong Kong 
# and University of Colorado
#
####################################################
#!/bin/bash

# the ipole executable #
executable = ../bin/ipole

# arguements pass to ipole #
arguments = -par ipole.par --dump=$(dump_file) --M_unit=$(munit) --trat_large=$(rhigh) --trat_small=$(rlow) --thetacam=$(theta)

# force transferring files #
should_transfer_files = yes

# input file to be transferred #
transfer_input_files = ../par/ipole.par,$(dump_dir)

# output directory#
transfer_output_remaps = "image.h5=$(img_dir)"

# where to write terminal output #
output = ../out/ipole.out
error = ../err/ipole.err
log = ../log/ipole.log

# cpu, memory and storage #
request_cpus = 1
request_memory = 1GB
request_disk = 1GB

# Container stuff #
universe = vanilla
Requirements = HAS_SINGULARITY
+SingularityImage = "/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-ubuntu-20.04:latest"

# prevent too much idle #
max_idle = 2000

#submit#
queue rlow,rhigh,munit,theta,dump_dir,dump_file,img_dir from ../var/varlist
