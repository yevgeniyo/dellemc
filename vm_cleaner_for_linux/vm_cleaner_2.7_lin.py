#!/usr/bin/env python

import sys
import time
import re
import os

'''#### Predifined variables'''
ESXES = (0,)
VC_UNAME = 'root'
ESX_UNAME = 'root'
ESX_PASSWORD = 'password'
PLATFORM = sys.platform


try:
        import paramiko
except ImportError:
    if PLATFORM == 'linux2':
        try:
            print("\nWARNING: On your machine was not found Paramiko module (for SSH connection), it will be installed automatically: \n ")
            os.system('curl \"https://bootstrap.pypa.io/get-pip.py\" -o \"get-pip.py\" && python get-pip.py')
            time.sleep(5)
            os.system("sudo yum -y install gcc libffi-devel python-devel openssl-devel")
            time.sleep(5)
            os.system("pip install pycrypto")
            time.sleep(3)
            os.system("pip install paramiko")
            print("\nMESSAGE: All depedencies were installed successfuly, start again and  enjoy using vM cleaner \n ")
	    sys.exit()
        except: 
            raise
    else:
        print("""
WARNING: Paramiko module (for SSH communication) is not installed on your local machine\n
Solution#1 - Install PyCharm IDE and just import paramiko from IDE
Solution#2 - Ask Yevgeniy Ovsyannikov\n""")
        sys.exit()

    
'''################# Rebooting for ESXes'''
def reboot_ESX():
    for x in ESXES:
        if x != 0:
            print("\n---rebooting ESX %s\n" % x)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(x, username=ESX_UNAME, password=ESX_PASSWORD, look_for_keys=False)
            stdin, stdout, stderr = ssh.exec_command("reboot")
            time.sleep(5)
        else:
            pass

'''################# Removing SDC from ESXes (doesnt matter version)'''            
def Removing_SDC_from_ESX():
    for x in ESXES:
        if x != 0:
            print("######Removing SDC files from ESX %s    " % x)
            print(" ")
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(x, username=ESX_UNAME, password=ESX_PASSWORD, look_for_keys=False)
            stdin, stdout, stderr = ssh.exec_command("esxcli system module parameters set -m scini -p \"\"")
            print("---Changing module of parameters...")
            for line in stdout:
                print('...' + line.strip('\n'))
            time.sleep(3)
            
            stdin, stdout, stderr = ssh.exec_command("esxcli software vib list | grep -I sdc")
            for line in stdout:
                x = line

            regexp = re.compile(r'scaleio-sdc-esx5.5*')
     
            if regexp.search(x) is not None:
                print ("---Removing SDC from ESX 5.5\n")
                stdin, stdout, stderr = ssh.exec_command("esxcli software vib remove -n scaleio-sdc-esx5.5\n")
                for line in stdout:
                    print('...' + line.strip('\n'))
                print("---SDC removed successfuly...")
                time.sleep(5)    
            else:
                print ("---Removing SDC from ESX 6.0\n")    
                stdin, stdout, stderr = ssh.exec_command("esxcli software vib remove -n scaleio-sdc-esx6.0\n")
                for line in stdout:
                    print('...' + line.strip('\n'))
                print("----SDC removed successfuly...")
                time.sleep(5)
        else:
            pass 
    print("\n#####Removing passed successfuly, don't forget reboot ESX...\n")
               
'''################# Removing files from VC'''
def Cleaning_VC():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(VC_IP, username=VC_UNAME, password=VC_PASSWORD, look_for_keys=False)
    stdin, stdout, stderr = ssh.exec_command("vpxd -v")
    for line in stdout:
        x = line
    print ("\nCleaninng %s \n" % x)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(VC_IP, username=VC_UNAME, password=VC_PASSWORD, look_for_keys=False)
    stdin, stdout, stderr = ssh.exec_command("service vsphere-client stop")
    for line in stdout:
        print('...' + line.strip('\n'))
    time.sleep(15)
    stdin, stdout, stderr = ssh.exec_command("rm -rf /var/lib/vmware/vsphere-client/vc-packages/vsphere-client-serenity/*")
    time.sleep(2)
    stdin, stdout, stderr = ssh.exec_command("rm -rf /etc/vmware/vsphere-client/vc-packages/vsphere-client-serenity/*")
    print("\nPlugin removed...\n")
    time.sleep(10)
    stdin, stdout, stderr = ssh.exec_command("rm -rf /opt/.vmware/*")
    time.sleep(2)
    stdin, stdout, stderr = ssh.exec_command("rm -rf /etc/vmware/vsphere-client/vc-packages/scaleio")
    print("Plugin logs and other files removed...\n")
    time.sleep(10)
    stdin, stdout, stderr = ssh.exec_command("service vsphere-client start")
    for line in stdout:
        print('...' + line.strip('\n'))
    time.sleep(15)
    print("\n   Removing passed successful   \n")

'''################# Addition ESXES '''
def Addition_ESXES():
    '''#### Setting ip address for 1-st ESX'''
    ESX_1 = raw_input("\nProvide IP of the 1-st ESX -> ")
    while ESX_1 == " " or (not ESX_1):
        print("ERROR: Set right format of ESX IP or hostname\n")
        ESX_1 = raw_input("Provide IP of the 1-st ESX -> ")
    else:
        pass

    '''#### Setting ip address for other ESX'es'''
    ESX_2 = raw_input("Provide IP of the 2-nd ESX -> ")
    if ESX_2 == " " or (not ESX_2):
        ESX_2 = ESX_3 = ESX_4 = ESX_5 = ESX_6 = ESX_7 = ESX_8 = 0
    else:
        pass

    if ESX_2 != 0:
        ESX_3 = raw_input("Provide IP of the 3-rd ESX -> ")
        if ESX_3 == " " or (not ESX_3):
            ESX_3 = ESX_4 = ESX_5 = ESX_6 = ESX_7 = ESX_8 = 0
    else:
        pass
    
    if ESX_3 != 0:
        ESX_4 = raw_input("Provide IP of the 4-th ESX -> ")
        if ESX_4 == " " or (not ESX_4):
            ESX_4 = ESX_5 = ESX_6 = ESX_7 = ESX_8 = 0
    else:
        pass

    if ESX_4 != 0:
        ESX_5 = raw_input("Provide IP of the 5-th ESX -> ")
        if ESX_5 == " " or (not ESX_5):
            ESX_5 = ESX_6 = ESX_7 = ESX_8 = 0
    else:
        pass
    
    if ESX_5 != 0:
        ESX_6 = raw_input("Provide IP of the 6-th ESX -> ")
        if ESX_6 == " " or (not ESX_6):
            ESX_6 = ESX_7 = ESX_8 = 0
    else:
        pass    

    if ESX_6 != 0:
        ESX_7 = raw_input("Provide IP of the 7-th ESX -> ")
        if ESX_7 == " " or (not ESX_7):
            ESX_7 = ESX_8 = 0
    else:
        pass

    if ESX_7 != 0:
        ESX_8 = raw_input("Provide IP of the 8-th ESX -> ")
        if ESX_8 == " " or (not ESX_8):
            ESX_8 = 0
    else:
        pass
        
    global ESXES
    ESXES = (ESX_1, ESX_2, ESX_3, ESX_4, ESX_5, ESX_6, ESX_7, ESX_8)
    
        
        
        
while [1]:
    main_menu = input("""                        
    Choose action:\n
    0 - Removing SIO files from vCenter  
    1 - Removing SDC from ESX's\n
    2 - Exit\n\n""")
    main_menu = int(main_menu)

    if main_menu == 0:
        VC_IP = raw_input("\nvCenter IP address: ")
        VC_PASSWORD = raw_input("\nSet vCenter password for root user: ")
        print("\nWill be removed all SIO files from your vCenter")
        print("Warning: Before romoving, please UNREGISTER plugin from ESX via powerCLI and close SSH connection to your vCenter")
        raw_input("Press Enter to continue...\n")
        try:
            Cleaning_VC()
        except:
            print("Operation was not successful, check credentials and SSH access to your vCenter\n")
            
    elif main_menu == 1:
    
    
        while True:
            main_menu_1 = input("""                        
    Choose action:\n
    0 - Add ESXes
    1 - List of ESXes
    2 - Remove SDC from ESXes
    3 - Reboot ESXes\n
    4 - Return to main menu\n\n""")
            main_menu_1 = int(main_menu_1)
        
       
            if main_menu_1 == 0:
                print("\nAdd ESXes for finish press ENTER")
                Addition_ESXES()
            
            elif main_menu_1 == 1:
                print("\nList of provided ESXes\n")
                for j in ESXES:
                    if j != 0:
                        print (j)
                    else:
                        print("-Empty-")
                        pass
                raw_input("\nPress Enter for previous menu...\n")
            
            elif main_menu_1 == 2:
                print("\nWARNING: Will be removed SDC from provided ESXes\n")
                for i in ESXES:
                    if i != 0:
                        print (i)
                    else:
                        pass
                raw_input("\nPress Enter to continue...\n")
        
                try:
                    Removing_SDC_from_ESX()
                except:
                    print("Operation was not successful, check credentials and SSH access to your ESXes\n")
                
            elif main_menu_1 == 3:
                print("\nThese ESXes will be rebooted\n")
                for k in ESXES:                
                    if k != 0:
                        print (k)            
                    else:
                        pass
                w = raw_input("\nPress Enter for continue or 'q' for cancel...\n")
                if w != 'q':
                    try:
                        reboot_ESX()
                    except:
                        print("Operation was not successful, check credentials and SSH access to your ESXes\n")
                else:
                    pass
            else:
                break
            
    else:
        break
