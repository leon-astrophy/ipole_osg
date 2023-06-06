################################################
#
# Cleaning all unwanted template text files
# Written by Ho Sang (Leon) Chan on 6.6.2023
# The Chinese University of Hong Kong and
# The University of Colorado
# 
################################################
#!/bin/bash

cd ../var
rm -rf varlist
cd ../log
rm -rf *.log
cd ../out
rm -rf *.out
cd ../err
rm -rf *.err
