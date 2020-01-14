import paramiko
import sys
import ast

nbytes = 4096
hostname = '158.129.140.201'
port = 3637
username = 'user022' 
password = 'JZUkRMG7'
command = 'python block.py 612787'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.exit_status_ready():
        break

print(session.recv_exit_status())
print(stdout_data[0][:-1].decode("utf-8"))
x = stdout_data[0][:-1].decode("utf-8")
x = ast.literal_eval(stdout_data[0][:-1].decode("utf-8"))

print (x[0])
session.close()
client.close()