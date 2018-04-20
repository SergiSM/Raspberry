#!/usr/bin/env python
import sys, paramiko
from scp import SCPClient

if len(sys.argv) < 2:
    print("args missing")
    sys.exit(1)

hostname = sys.argv[1]
#file = sys.argv[2]

password = ""
username = "root"
port = 22

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    client.connect(hostname, port=port, username=username, password=password)

    # SCPCLient takes a paramiko transport as its only argument
    scp = SCPClient(client.get_transport())
    
    scp.put('a.txt')
    scp.put('b.txt')
    scp.get('/home/root/prova.zip')

    scp.close()

finally:
    client.close()
