#SCRIPT FOR FORTIGATE BULK ADDRESS CREATION AND ROUTES CREATION

This Script is to create a Bulk IP address and routes creation on the fortigate firewall.

Once this is created we can directly paste this on the web gui, cli and save our time alot.


I have done the proof of concept, Make sure you have included the ip address properly on a file without any line break


(Address creation)Once you run the script it will create two files in /tmp/fortigate directory called object_script.txt and groups.txt
(Routes Creation)Once you run the script it will create a file called routes_script.txt

Take that and copy paste on to the fortigate firewall from Gui cli, NOT FROM SSH.

This script will identify the object based upon the CIDR and create H-X.X.X.X for /32 and N-X.X.X.X for network


NOTE : Make sure you have pwntools installed on the computer. If you dont have pwn tools installed replace log.progress with print and then delete from pwn import *

NOTE : I have default directory to save the exploit as /tmp/fortigate/, If you want change that path to obsolute one to whereever you required but i would suggest to leave in the default location which i have specified.

USAGE(Address) : python3 script.py <absolute path to ip address file> <group name>
        
EXAMPLE(Address) : python3 script.py /home/dummy/Desktop/fortigate/file.txt Malicious-Group
        
Usage(Routes) : python3 script.py <absolute path to ip address file> <gateway ip address> <destination interface port number>

Example(Routes) : python3 script.py /home/dummy/Desktop/fortigate/file.txt 10.1.1.1 6
        
                                                        (6 here is the exit interface port number/Gateway port number)
        
