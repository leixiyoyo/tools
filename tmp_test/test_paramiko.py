#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Leiyangfeng

import paramiko
def cct(hostname,username,password,port):
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname=hostname,username=username,password=password,port=port)
    stdin, stdout, stderr=client.exec_command('ifconfig')
    client.close()
    if stderr:
        return stderr.read().decode('utf-8')
    return stdout.read().decode('utf-8')
def my_test(arg1,arg2):
    print arg1
    print arg2



if __name__ == '__main__':
    # arg={'arg1':1,'arg2':2}
    # ret=my_test(**arg)
    # print ret
    arg={'username': 'root', 'password': '123456', 'hostname': '192.168.66.100', 'port': 22}
    ret=cct(**arg)
    print ret