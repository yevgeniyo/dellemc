import os, time, paramiko

print(" ")
ip = input("IP or hostname -> ")
print(" ")
device = input("Device name (example: sda or scinia) -> ")
print("\n")




ssh = paramiko.SSHClient()
# Uncomment the following line for the equivalent of -oStrictHostKeyChecking=no
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username='root', password='password')
stdin, stdout, stderr = ssh.exec_command("fio --name=f_thread --ioengine=libaio --rw=write --bs=4k --direct=1 --size=500G --numjobs=1 --runtime=6000000000 --time_based --thread --rwmixread=0 --rwmixwrite=100 --filename=/dev/%s" % device)
for line in stdout:
        print ('...' + line.strip('\n'))
print("\n")
x = input("Press enter to exit...\n")
