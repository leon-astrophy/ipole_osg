#################################################################
#
# A simple python script to submit ipole jobs to OSG 
# this script accept several inputs from the terminal including 
# 1. the GRMHD snapshot directory
# 2. the desired ipole output directory
# 3. Rlow 
# 4. Rhigh
# 5. Muniti
# 6. Inclination angle
# Written by Ho Sang (Leon) Chan on 6.6.2023
# The Chinese University of Hong Kong and University of Colorado
#
#################################################################

# import required packages#
import os
import sys
import htcondor
from pathlib import Path

#################################################################
# input parameters from terminal #

#dumps directory#
dump_dir = sys.argv[1]

#output directory#
img_dir = sys.argv[2]

#rlow#
rlow = sys.argv[3]

#rhigh#
rhigh = sys.argv[4]

#munit#
munit = sys.argv[5]

#inclination#
thetacam = sys.argv[6]

#################################################################
# We extract all GRMHD snapshot filename and create an itemlist

# GRMHD snapshot name  #
filename = list(Path(dump_dir).glob("*.h5"))

# itemdata #
itemdata = [{"rlow": rlow,
             "rhigh": rhigh,
             "munit": munit,
             "theta": thetacam,
             "dump_dir": path.as_posix(), 
             "dump_file": path.name, 
             "img_dir": os.path.join(img_dir, path.name)} 
             for path in filename]

#print to debug#
#for item in itemdata:
#    print(item)

#################################################################
# HTcondor parameters #

#output directory#
out_dir = "../out/ipole.out"
err_dir = "../err/ipole.err"
log_dir = "../log/ipole.log"

#number of cpus#
n_cpu = "1"
n_ram = "1GB"
n_disk = "1GB"

#################################################################

#create a htcondor job#
cat_job = htcondor.Submit({
    "executable": "../bin/ipole",
    "arguments": "-par ipole.par --dump=$(dump_file) --M_unit=$(munit) --trat_large=$(rhigh) --trat_small=$(rlow) --thetacam=$(theta)",
    "should_transfer_files": "yes",         
    "transfer_input_files": "../par/ipole.par,$(dump_dir)",  
    "transfer_output_remaps": '"image.h5=$(img_dir)"',
    "output": out_dir,
    "error": err_dir,
    "log": log_dir,
    "universe": "vanilla",
    "request_cpus": n_cpu,
    "request_memory": n_ram,
    "request_disk": n_disk,
    "Requirements": "HAS_SINGULARITY",
    "+SingularityImage": '"/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-ubuntu-20.04:latest"',
    "max_idle": "2000"
})

#print result to debug#
#print(cat_job)

#submit the job#
schedd = htcondor.Schedd()
submit_result = schedd.submit(cat_job, itemdata = iter(itemdata))

# print result to debug #
#print(submit_result.cluster())

#################################################################

# query #
query = schedd.query(
    constraint=f"ClusterId == {submit_result.cluster()}",
    projection=["Out", "Args", "TransferInput"],
)

# print to debug #
#print(query)

#################################################################
