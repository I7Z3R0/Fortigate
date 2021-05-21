#!/usr/bin/env python3
import sys
import subprocess
from time import sleep
from pwn import *

print("""\033[1;31;40m
         /$$$$$$       /$$$$$$$$       /$$$$$$$$        /$$$$$$        /$$$$$$$         /$$$$$$ 
        |_  $$_/      |_____ $$/      |_____ $$        /$$__  $$      | $$__  $$       /$$$_  $$
          | $$             /$$/            /$$/       |__/  \ $$      | $$  \ $$      | $$$$\ $$
          | $$            /$$/            /$$/           /$$$$$/      | $$$$$$$/      | $$ $$ $$
          | $$           /$$/            /$$/           |___  $$      | $$__  $$      | $$\ $$$$
          | $$          /$$/            /$$/           /$$  \ $$      | $$  \ $$      | $$ \ $$$
         /$$$$$$       /$$/            /$$$$$$$$      |  $$$$$$/      | $$  | $$      |  $$$$$$/
        |______/      |__/            |________/       \______/       |__/  |__/       \______/ 
        Save time, Time is precious\n \033[1;32;40m""")

def object(path):
    f = open("/tmp/fortigate/object_script.txt", "a+")
    f.write("config firewall address\n")
    with open(path, "r") as file:
        for address in file:
            line = address.strip()
            f = open("/tmp/fortigate/object_script.txt", "a+")
            if "/32" in line:
                f.write("edit H-" + line.replace("/32", ""))
                f.write("\nset subnet " + line)
                f.write("\nnext\n\n")
            else:
                ip = re.findall('(.*)/', line)[0]
                f.write("edit N-" + ip)
                f.write("\nset subnet " + line)
                f.write("\nnext\n\n")
    f.write("end\n")
    f.close()
    
def groups(path, group):
    f = open("/tmp/fortigate/group.txt", "a+")
    f.write("config firewall addrgrp\n")
    f.write('edit "' + group + '"')
    group_ips = []
    with open(path, "r") as file:
        for address in file:
            line = address.strip()
            f = open("/tmp/fortigate/group.txt", "a+")
            if "/32" in line:
                group_ips.append('"H-' + line.replace("/32", "") + '" ')
            else:
                ip = re.findall('(.*)/', line)[0]
                group_ips.append('"N-' + ip + '" ')
    listing = "".join(group_ips)
    f = open("/tmp/fortigate/group.txt", "a+")
    f.write("\nappend member ")
    f.write(listing)
    f.write("\nnext")
    f.write("\nend\n")
    f.close()
    sleep(2)
    log.progress("Process Completed!, Saving the file in /tmp/fortigate \n")
    sleep(2)
    print("\n Success! Your script to copy paste is stored in /tmp/fortigate/object_script.txt and /tmp/fortigate/groups.txt\n")


if __name__ == '__main__':
    if len(sys.argv[1:]) < 2:
        print('''
        
    Usage : python3 script.py <absolute path to ip address file> <group name>
        
    Example : python3 script.py /home/dummy/Desktop/fortigate/file.txt Malicious-Group
        
        
        ''')
    else:
        path = sys.argv[1].strip()
        group = sys.argv[2].strip()
        log.progress("Removing the existing directory named fortigate in tmp folder\n")
        subprocess.call("rm -rf /tmp/fortigate 2>/dev/null", shell=True)
        log.progress("Creating a directory called fortigate in /tmp path\n\n")
        subprocess.call("mkdir -p /tmp/fortigate", shell=True)
        subprocess.call("touch /tmp/fortigate/object_script.txt", shell=True)
        subprocess.call("touch /tmp/fortigate/group.txt", shell=True)
        object(path)
        groups(path,group)
