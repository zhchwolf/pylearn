import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='172.18.10.126',port=22,username='root',password='2cw@China')
stdin,stdout,stderr = ssh.exec_command('ls')

result = stdout.read()
print(result)
ssh.close()

