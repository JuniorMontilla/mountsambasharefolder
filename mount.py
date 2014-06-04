#!/usr/bin/env python
# -*-coding: utf-8 -*-
#by Junior Montilla

from re import search 
from os import environ
from subprocess import PIPE, Popen 

cmd = "df -h"
df = Popen(cmd, stdout=subprocess.PIPE,stdin=subprocess.PIPE,bufsize=10000000 ,shell=True)
output = df.stdout.readlines()
stroutput = str(output)

user = environ.get('USER')
cmd1= "zenity --info --title \"El Z_{0} ya esta montado\" --width 200 --text \"El Z_{0} ya esta montado\"".format(user)

if search("Z_{0}".format(user) ,stroutput) or search("{0}_Z".format(user),stroutput):
        out = Popen(cmd1, stdout=subprocess.PIPE,stdin=subprocess.PIPE,bufsize=10000000 ,shell=True)
        print out.stdout.read()
else:
        cmd2="bash /stuff/login.sh"
        commandoutput = Popen(cmd2,bufsize=1000000,shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE) 
        print commandoutput.stdout.read()
