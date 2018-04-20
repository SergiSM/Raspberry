#!/usr/bin/env python
import sys, paramiko

if len(sys.argv) < 3:
    print("args missing")
    sys.exit(1)

hostname = sys.argv[1]
command = sys.argv[2]

password = ""
username = "root"
port = 22

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
    client.connect(hostname, port=port, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read())

finally:
    client.close()
