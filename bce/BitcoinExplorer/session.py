import paramiko
import sys
import ast

nbytes = 4096
hostname = '158.129.140.201'
port = 3637
username = 'user022' 
password = 'JZUkRMG7'

def get_latest_blocks():	
	client = paramiko.Transport((hostname, port))
	client.connect(username=username, password=password)

	session = client.open_channel(kind='session')
	command = 'python latest_blocks.py'

	stdout_data = []
	session.exec_command(command)
	while True:
	    if session.recv_ready():
	        stdout_data.append(session.recv(nbytes))
	    if session.exit_status_ready():
	        break

	session.close()
	client.close()

	return ast.literal_eval(stdout_data[0][:-1].decode("utf-8"))

def get_block(block_height):
	client = paramiko.Transport((hostname, port))
	client.connect(username=username, password=password)

	session = client.open_channel(kind='session')
	command = 'python block.py ' + str(block_height)

	stdout_data = []
	session.exec_command(command)
	while True:
	    if session.recv_ready():
	        stdout_data.append(session.recv(nbytes))
	    if session.exit_status_ready():
	        break

	session.close()
	client.close()

	return ast.literal_eval(stdout_data[0][:-1].decode("utf-8"))


def close_session():
	session.close()
	client.close()
