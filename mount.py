#!/usr/bin/env python

import subprocess, re, os

cmd = "df -h"
df = subprocess.Popen(cmd, stdout=subprocess.PIPE,stdin=subprocess.PIPE,bufsize=10000000 ,shell=True)
output = df.stdout.readlines()
stroutput = str(output)

if re.search("Z_%s" % os.environ.get('USER'),stroutput) or re.search("%s_Z" % os.environ.get('USER'),stroutput):
        out =subprocess.Popen("zenity --info --title \"El Z_%s ya esta montado\" --width 200 --text \"El Z_%s ya esta montado\""% (os.environ.get('USER'),os.environ.get('USER')), stdout=subprocess.PIPE,stdin=subprocess.PIPE,bufsize=10000000 ,shell=True)
        print out.stdout.read()
else:
        comando="bash /stuff/login.sh"
        commandoutput = subprocess.Popen(comando,bufsize=1000000,shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE) 
        print commandoutput.stdout.read()
