#!/usr/bin/env python


import paramiko, os, time, sys

print("\n")
vc_ip = raw_input("Provide IP of vCenter -> ")
esx1_ip = raw_input("Provide IP of the 1st ESX -> ")
esx2_ip = raw_input("Provide IP of the 2nd ESX -> ")
esx3_ip = raw_input("Provide IP of the 3rd ESX -> ")
SDC_reboot = raw_input("Perform reboot of ESX after removing of SDC? y/n -> ")
esxs = (esx1_ip, esx2_ip, esx3_ip)
vc_uname = 'root'
vc_password_5_5 = 'Scaleio123'
vc_password_6_0 = 'Scaleio123!'
ESX_uname = 'root'
ESX_password = 'password' 

print(" ")

def vc5_5():
	print("---REMOVING SIO FILES FROM VCENTER 5.5---")
	print(" ")
	paramiko.util.log_to_file('paramiko.log')
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(vc_ip, username=vc_uname, password=vc_password_5_5,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command("service vsphere-client stop")
	print stdout.read()
	time.sleep(20)
	paramiko.util.log_to_file('paramiko.log')
	stdin, stdout, stderr = ssh.exec_command("rm -rf /var/lib/vmware/vsphere-client/vc-packages/vsphere-client-serenity/*")
	print stdout.read()
	time.sleep(20)
	paramiko.util.log_to_file('paramiko.log')
	stdin, stdout, stderr = ssh.exec_command("rm -rf /opt/.vmware/*")
	print stdout.read()
	time.sleep(20)
	paramiko.util.log_to_file('paramiko.log')
	stdin, stdout, stderr = ssh.exec_command("service vsphere-client start")
	print stdout.read()
	time.sleep(30)
	print(" ")
	print("+++REMOVING PASSED SUCCESSFUL+++\n")	


def vc6_0():
        print("---REMOVING SIO FILES FROM VCENTER 6.0---")
        print(" ")
        paramiko.util.log_to_file('paramiko.log')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(vc_ip, username=vc_uname, password=vc_password_6_0,look_for_keys=False)
        stdin, stdout, stderr = ssh.exec_command("service vsphere-client stop")
        print stdout.read()
        time.sleep(20)
        paramiko.util.log_to_file('paramiko.log')
        stdin, stdout, stderr = ssh.exec_command("rm -rf /etc/vmware/vsphere-client/vc-packages/vsphere-client-serenity/*")
        print stdout.read()
        time.sleep(20)
        paramiko.util.log_to_file('paramiko.log')
        stdin, stdout, stderr = ssh.exec_command("rm -rf /etc/vmware/vsphere-client/vc-packages/scaleio")
        print stdout.read()
        time.sleep(20)
        paramiko.util.log_to_file('paramiko.log')
        stdin, stdout, stderr = ssh.exec_command("service vsphere-client start")
        print stdout.read()
        time.sleep(30)
        print(" ")
        print("+++REMOVING PASSED SUCCESSFUL+++\n")


def SDC_from_ESX_5_5():
	for x in esxs:	
	        print("---REMOVING SDC files from ESX %s ---" % x)
	        print(" ")
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(x, username=ESX_uname, password=ESX_password, look_for_keys=False)
		stdin, stdout, stderr = ssh.exec_command("esxcli system module parameters set -m scini -p \"\"")
		print stdout.read()
		time.sleep(5)
		stdin, stdout, stderr = ssh.exec_command("esxcli software vib remove -n scaleio-sdc-esx5.5")
		print stdout.read()
		time.sleep(5)
		if SDC_reboot == "y" or "yes":
			print("==Reeboting==")
			stdin, stdout, stderr = ssh.exec_command("reboot")
			print stdout.read()
		else:
			pass
		print(" ")
       		print("+++REMOVING PASSED SUCCESSFUL+++\n")

	
def SDC_from_ESX_6_0():
        for x in esxs:
                print("---REMOVING SDC files from ESX %s ---" % x)
                print(" ")
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(x, username=ESX_uname, password=ESX_password, look_for_keys=False)
                stdin, stdout, stderr = ssh.exec_command("esxcli system module parameters set -m scini -p \"\"")
                print stdout.read()
                time.sleep(5)
		if SDC_reboot == "y" or "yes":
			print("==Reeboting==")
                        stdin, stdout, stderr = ssh.exec_command("reboot")
			print stdout.read()
                else:
                        pass
                stdin, stdout, stderr = ssh.exec_command("esxcli software vib remove -n scaleio-sdc-esx6.0")
                print stdout.read()
                time.sleep(5)
                print(" ")
                print("+++REMOVING PASSED SUCCESSFUL+++\n")



def reboot_ESX():
	 for x in esxs:
                print("---rebooting ESX %s ---" % x)
                print(" ")
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(x, username=ESX_uname, password=ESX_password, look_for_keys=False)
                stdin, stdout, stderr = ssh.exec_command("reboot")
                print stdout.read()
                time.sleep(5)
                print(" ")





while [1]:
    main_menu = input("Choose action:\n\n 0 - Removing SIO files from vCenter\n 1 - Removing SDC from ESX's\n 2 - Reboot all ESX's (useful in installation phase)\n 3 - List of provided ip's (VC and ESX's)\n 4 - Change default credentials of VC and ESX\n 5 - Exit\n\n")

    if main_menu == 0:
                      
            type_of_vc = input("Choose vCenter version:\n 0 - vCenter 5.5\n 1 - vCenter 6.0\n\n")

            if type_of_vc == 0:
		    print("\n") 
                    print("Will be removed all SIO files from vCenter 5.5")
                    raw_input("Press Enter to continue...\n")
                    vc5_5()
            elif type_of_vc == 1:
                    print("\n")  
                    print("Will be removed all SIO files from vCenter 6.0")
                    raw_input("Press Enter to continue...\n")
                    vc6_0()
            else:
                    print("returned to previous menu\n")

    elif main_menu == 1:

            type_of_ESX = input("Choose ESX version:\n 0 - ESX 5.5\n 1 - ESX 6.0\n\n")        

            if type_of_ESX == 0:
		      print("\n")
                      print("Will be removed SDC from ESX5.5")
                      raw_input("Press Enter to continue...\n")
                      SDC_from_ESX_5_5()  
            elif type_of_ESX == 1:
                      print("\n")
                      print("Will be removed SDC from ESX6.0")
                      raw_input("Press Enter to continue...\n")                            
                      SDC_from_ESX_6_0()
            else:
                      print("returned to previous menu\n")
                      
    elif main_menu == 2:
	   print("\n")
           print("All ESX's will be rebooted")
	   raw_input("Press Enter to continue...\n")
	   reboot_ESX()

    elif main_menu == 3:
	   print("\n")
           print("vCenter IP - %s" % vc_ip)
           print(" ")
           print("ESX-1 IP -  %s" % esx1_ip)
           print("ESX-2 IP -  %s" % esx2_ip)  		
	   print("ESX-3 IP -  %s" % esx3_ip)
           print("\n")
	   raw_input("Press Enter to continue...\n")

    elif main_menu == 4:
           
           print(" ")
	   type_of_server = input("Changing credentials:\n 0 - vCenter 5.5\n 1 - vCenter 6.0\n 2 - ESX\n 3 - Back\n\n")
           print(" ")                

	   if type_of_server == 0:
               vc_uname_5_5 = input("Set username of the vCenter -> ")
               vc_password = input("Set password of the vCenter - > ")
	       print(" ")

           elif type_of_server == 1:
               vc_uname_6_0 = input("Set username of the vCenter -> ")
               vc_password = input("Set password of the vCenter - > ")
               print(" ")               

           elif type_of_server == 2:
               ESX_uname = input("Set username of the ESX's -> ")
               ESX_password = input("Set password of the ESX's - > ")
               print(" ")               

           else:
               pass

    else:
           print(" ") 
           sys.exit()



	







