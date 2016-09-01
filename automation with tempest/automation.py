#!/usr/bin/env python


import os
from tests import *


#--------------------------------------------------------------------------------
#Create extra specs for volumetype 'scaleio'

def ExtraSpec_thin():
    os.system("cinder type-key scaleio set sio:provisioning_type=thin")
    os.system("cinder type-key scaleio set sio:iops_limit=0")
    os.system("cinder type-key scaleio set sio:bandwidth_limit=0")

def ExtraSpec_thik():
    os.system("cinder type-key scaleio set sio:provisioning_type=thik")
    os.system("cinder type-key scaleio set sio:iops_limit=0")
    os.system("cinder type-key scaleio set sio:bandwidth_limit=0")

def ExtraSpec_iops_limit():
    os.system("cinder type-key scaleio set sio:provisioning_type=thin")
    os.system("cinder type-key scaleio set sio:iops_limit=100")
    os.system("cinder type-key scaleio set sio:bandwidth_limit=0")

def ExtraSpec_bandwidth_limit():
    os.system("cinder type-key scaleio set sio:provisioning_type=thin")
    os.system("cinder type-key scaleio set sio:bandwidth_limit=1024")
    os.system("cinder type-key scaleio set sio:iops_limit=0")



#--------------------------------------------------------------------------------
#Change size of default volume

def change_vol_size(SIZE=17):
    def replace_line(file_name, line_num, text):
        lines = open(file_name, 'r').readlines()
        lines[line_num] = text
        out = open(file_name, 'w')
        out.writelines(lines)
        out.close()

    replace_line('/usr/lib/python2.7/site-packages/tempest/config.py', 718, '               default = %s ,\n' % SIZE)


#--------------------------------------------------------------------------------
#Running tests

li = [TEST_1,TEST_2,TEST_3,TEST_4,TEST_5,TEST_6,TEST_7,TEST_8,TEST_9,TEST_10,TEST_11,TEST_12,TEST_13,TEST_14,TEST_15,TEST_16,TEST_17,TEST_18,TEST_19,TEST_20,TEST_21,TEST_22,TEST_23,TEST_24,TEST_25,TEST_26,TEST_27,TEST_28,TEST_29,TEST_30,TEST_31,TEST_32,TEST_33,TEST_34]

def running_tests():
    for i in li:
        all = "testr run " + i + " &> /dev/null"
        TEST_ACTION = os.system(all)
        if TEST_ACTION == 0:
            print (i + "... OK")
        else:
	    os.system(all + "&>> fail_log.txt")
            print (i + "... FAILED")

#----------------------------------------------------------------------------------
#Scenario tests

##1. Full sets of tests for thik volume with volume size multiple 8:

#print("\n---------------Full sets of tests for thik volume with volume size multiple 8-----------------\n")
#ExtraSpec_thik()
#change_vol_size(16)
#running_tests()

##2. Full sets of tests for thik volume with volume size not multiple 8:

#print("\n---------------Full sets of tests for thik volume with volume size not multiple 8-----------------\n")
#ExtraSpec_thik()
#change_vol_size(10)
#running_tests()

##3. Full sets of tests for thin volume:

print("\n---------------Full sets of tests for thin volume-----------------\n")
ExtraSpec_thin()
change_vol_size(16)
running_tests()

##4. Full sets of tests with thin volume and iops_limit = 100

print("\n---------------Full sets of tests with thin volume and iops_limit = 100-----------------\n")
ExtraSpec_iops_limit()
change_vol_size(16)
running_tests()

##5. Full sets of tests with thin volume and bandwidth_limit = 1024K

print("\n---------------Full sets of tests with thin volume and bandwidth_limit = 1024K-----------------\n")
ExtraSpec_bandwidth_limit()
change_vol_size(16)
running_tests()

