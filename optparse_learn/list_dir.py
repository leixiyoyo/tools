#!/usr/bin/env python27
# -*- coding:utf-8 -*- 
#Author: Leiyangfeng
import  os,optparse,argparse,paramiko
def input_args():
    hstr = '%prog -i host or host_file -u user -p password -P port'
    parser = optparse.OptionParser(hstr, description='help info of %prog 1.0', version='%prog 1.0') #指定版本,通过scripts.py --version查看
    # print parser.usage
    # # print parser.option_list
    # # print parser.option_class
    parser.add_option('-i', '--host', dest='hostname', default='127.0.0.1', help='target host or host_file')
    parser.add_option('-u', '--user', dest='username', default='root', help='username')
    parser.add_option('-p', '--password', dest='password', default=None, help='password')
    parser.add_option('-P', '--port', dest='port',default=22, help='ssh_port of target host')


    return parser


def cct(hostname, username, password, port):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname=hostname, username=username, password=password, port=port)
    # ret = client.exec_command('ipconfig')
    # client.close()

    return client

if __name__ == '__main__':
    parser=input_args()
    opt,arg_list=parser.parse_args() # arg_list为列表
    # client=cct(**opt) # opt是个instance相当于对象,看着跟字典一样,所以不能这样打散
    cmd=arg_list[0] # 如果命令里带-,如ls -l就会报错了
    client=cct(hostname=opt.hostname,username=opt.username,password=opt.password,port=opt.port)
    stdin, stdout, stderr = client.exec_command(cmd)
    if stderr:
        print stderr.read().decode('utf-8')
    print stdout.read().decode('utf-8')
    client.close()

