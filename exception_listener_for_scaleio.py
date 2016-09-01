import smtplib,paramiko,os,time


print("\n\n")
mdm_ip = input("Enter your mdm ip -> ")
print(" ")
mail1 = input("Enter your email address -> ")
mdm = 'stat -c%s /opt/emc/scaleio/mdm/logs/exp.0'
sds = 'stat -c%s /opt/emc/scaleio/sds/logs/exp.0'

def mail():
    SERVER = "10.106.48.137"

    FROM = "ScaleIO_Exception_listener@emc.com"
    TO = [mail1] # must be a list
    
    SUBJECT = ("Exception on MDM %s" % mdm_ip)
    
    TEXT = ("Your MDM or SDS %s got exception, check it into /opt/emc/scaleio/mdm(sds)/logs/exp.0" % mdm_ip)  
    # Prepare actual message
    message = TEXT

    # Send the mail
    
    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, message)
    server.quit()




ssh = paramiko.SSHClient()
# Uncomment the following line for the equivalent of -oStrictHostKeyChecking=no
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(mdm_ip, username='root', password='password')
stdin, stdout, stderr = ssh.exec_command(mdm)
mdm0 = stdout.read()
mdm1 = int(mdm0)
stdin, stdout, stderr = ssh.exec_command(sds)
sds0 = stdout.read()
sds1 = int(sds0)
#print(mdm1)
#print(sds1)
#c = '10' in output1
#print(c)

print("\n\n")
print('Please, don`t close this window\n"Exception listener" is working...\n\n\n')


while [1]:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(mdm_ip, username='root', password='password')
    stdin, stdout, stderr = ssh.exec_command(mdm)
    mdm2 = stdout.read()
    mdm3 = int(mdm2)
    stdin, stdout, stderr = ssh.exec_command(sds)
    sds2 = stdout.read()
    sds3 = int(sds2)
#    print(mdm3)
#    print(sds3)
    if mdm3 - mdm1 < 100 and sds3 - sds1 < 100 :
        pass
    else:
        mail()
        input("You have exception on MDM or SDS, check logs!\n\nPress enter to exit...")
        break
    time.sleep(20)




