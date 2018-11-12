import paramiko

transport = paramiko.Transport(('172.18.10.126',22))
transport.connect(username='root',password='2cw@China')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin,stdout,stderr = ssh.exec_command('df')
print(stdout.read())

transport.close()

