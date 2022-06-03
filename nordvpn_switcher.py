import os
import subprocess
def banner():
 os.system("clear")
 os.system("figlet Nordvpn Switcher")
 print("Code made by: CryptoCat44 and NeikiDev")
 print("Version: 1.0.3 | https://github.com/neikidev")
 print("")
login_status = "Default"
banner()
print("Searching for NordVPN connection, please wait...!\n\n")
try:
    login_status = subprocess.check_output(["nordvpn", "account"])
except Exception as e:
    print("We run in some Error! (Failed to Connect to NordVPN)\n")
    print(e)
    os.system("nordvpn account")
    input("Press any Key to Exit!...")
    exit()
login_status = str(login_status)
account_email = login_status.split("Email Address: ")[1].split("\\n")[0]
account_info = login_status.split("VPN Service: ")[1].split('\\n')[0]
print('We found this Account Informations: ')
print('Email Address: '+account_email)
print('VPN Service: '+account_info)
right=str(input("Is this the right Informations? (Y/n) :"))
if((right=="N") or (right=="n")):
    print("The Informations are Wrong?")
    print('Please relogin with "nordvpn login" or check your account with "nordvpn account!"\n')
    input("Press any Key to Exit!...")
    exit()
banner()
os.system("bash vpn.sh")


