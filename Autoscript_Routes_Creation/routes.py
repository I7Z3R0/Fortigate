import sys
import subprocess
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


def routes(path, gateway, port):
    f = open("/tmp/fortigate_routes/routes_script.txt", "a+")
    f.write("config router static\n")
    with open(path, "r") as file:
        for address in file:
            line = address.strip()
            f = open("/tmp/fortigate_routes/routes_script.txt", "a+")
            f.write("set gateway " + gateway)
            f.write("\nset dst " + line)
            f.write("\nset device port" + port)
            f.write("\nnext\n\n")
    f.write("end")
    f.close()
    sleep(2)
    log.progress("Process Completed!, Saving the file in /tmp/fortigate_routes \n")
    sleep(2)
    print("\n Success! Your script to copy paste is stored in /tmp/fortigate_routes/routes_script.txt\n")


if __name__ == '__main__':
    if len(sys.argv[1:]) < 3:
        print('''

    Usage : script.py <absolute path to ip address file> <gateway ip address> <destination port number>

    Example : script.py /home/dummy/Desktop/fortigate/file.txt 10.1.1.1 6


        ''')
    else:
        path = sys.argv[1].strip()
        gateway = sys.argv[2].strip()
        port = sys.argv[3].strip()
        log.progress("Removing the existing directory named fortigate_routes in tmp folder\n")
        subprocess.call("rm -rf /tmp/fortigate_routes 2>/dev/null", shell=True)
        log.progress("Creating a directory called fortigate_routes in /tmp path\n\n")
        subprocess.call("mkdir -p /tmp/fortigate_routes", shell=True)
        subprocess.call("touch /tmp/fortigate_routes/routes_script.txt", shell=True)
        routes(path, gateway, port)
