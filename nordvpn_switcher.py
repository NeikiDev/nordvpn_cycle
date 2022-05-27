import os
def banner():
 os.system("clear")
 os.system("figlet Nordvpn Switcher")
 print("Code made by: CryptoCat44 and NeikiDev")
 print("")

op=str(input("Did you already login to NordVPN? (Y/n) :"))
if((op=="N") or (op=="n")):
 banner()
 print("Please Login to NordVPN and try again!")
 exit()
else:
 pass
banner()
os.system("bash vpn.sh")


