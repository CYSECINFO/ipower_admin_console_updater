import os
import time
time.sleep(2)
print("initializing ipower admin console updater......")
time.sleep(2)
print("checking present file condition......")
os.system("pkg update")
os.system("pkg upgrade")
os.system("pkg install unzip")
os.system("ls")
print("updating in progress.....")
time.sleep(3)
os.system("rm -r ipower-admin-console-v2")
os.system("fetching  all details.....")
time.sleep(2)                                                                                                                    
os.system("apt update")
os.system("apt upgrade")             
os.system("pkg install git")
print("please wait........")
time.sleep(5)
print("In which platform you want to update our sofware")
print("press 1 for version 1 installation")
print("press 2 for version 2 installation")
input_1 = input("Enter your choice here:" )
if (input_1=="1"):
            os.system("git clone https://github.com/CYSECINFO/ipower-admin-console-v2")
                                                                                                                        
else:
   print("Error 404 not found")
if (input_1=="2"):
                os.system("git clone https://github.com/CYSECINFO/ipower-admin-console-v2")
                                                                           
else:
   print("Error 404 not found")
if (input_1=="3"):
                os.system("git clone https://github.com/CYSECINFO/ipower-admin-console-v2")
                                                                             
else:
   print("Error 404 not found")
                                                                                                                          
                                                                                                                                                    
                                                       
