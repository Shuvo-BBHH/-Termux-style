#!/usr/bin/python3

#coded by Braderlala

#IMPORT OS

import os
import sys
import time

#start


os.system("clear")
os.system("cat banner")
print("starting")
time.sleep(2.0)
print(".")
print("..")
print("...")
print("....")


os.system('rm -rf /data/data/com.termux/files/usr/etc/motd-playstore')
os.system('rm -rf /data/data/com.termux/files/usr/etc/motd.dpkg-old')
os.system('rm -rf /data/data/com.termux/files/usr/etc/motd')
os.system('cp bash.bashrc /data/data/com.termux/files/usr/etc/')
time.sleep(5.0)

os.system("clear")
print 
print 
print("Finish !!")
time.sleep(1.0)

os.system('login')
