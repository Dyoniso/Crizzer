import time
import os
import sys
import socket 
import random
import itertools
import threading
from base64 import b64encode
from datetime import datetime
from os import urandom

red = "\033[0;31m"
white = "\033[0m"
blue = "\033[94m"
green = "\033[92m"
magenta = "\033[1;35;40m"
WARNING = '\033[93m'

tag = red+"[+] "+white
tag1 = green+"[+] "+white
tag2 = blue+"[*] "+white
tag3 = red+"[-] "+white

os.system("")

print("")
print(red+    "  ,----..                                  	")
print(red+    " /   /   \                                 	")
print(red+    "|   :     :       ,----,  __  ,-.  __  ,-. 	")
print(red+    ".   |  ;. /     .'   .`|,' ,'/ /|,' ,'/ /|  	")
print(red+    ".   ; /--`   .'   .'  .''  | |' |'  | |' | 	")
print(red+    ";   | ;    ,---, '   ./ |  |   ,'|  |   ,' 	")
print(blue+   "|   : |    ;   | .'  /  '  :  /  '  :  /   	")
print(blue+   ".   | '___ `---' /  ;--,|  | '   |  | '    	")
print(blue+	  "'   ; : .'|  /  /  / .`|;  : |   ;  : |    	")
print(blue+   "'   | '/  :./__;     .' |  , ;   |  , ;    	")
print(magenta+"|   :    / ;   |  .'     ---'     ---'     	")
print(magenta+" \   \ .'  `---'                           	")
print(magenta+"  `---`                                     	"+white)  
print("v1.0, By Dyoniso") 
print("")
print("* "+red+"[1]"+white+" Lets instalation")	
print("* "+red+"[2]"+white+" Information of Packages")	
print("* "+red+"[3]"+white+" Exit")	
print("")

# current date and time
now = datetime.now() 
dateTimeNow = now.strftime("%m/%d/%Y, %H:%M:%S")

def letsCrizzer():
	
	done = False
	def animate():
		for c in itertools.cycle([
		red+white+" Instaling Package         ",
		red+">"+white+" Instaling Package        ",
		red+">>"+white+" Instaling Package       ",
		red+">>"+blue+">"+white+" Instaling Package      ",
		red+">>"+blue+">>"+white+" Instaling Package     ",
		red+">>"+blue+">>"+magenta+">"+white+" Instaling Package   ", 
		red+">>"+blue+">>"+magenta+">>"+green+" Instaling Package",
		""]):
			if done == True:
				break
			sys.stdout.write("\r"+tag+c)
			sys.stdout.flush()
			time.sleep(0.5)
			
	try:
		while(True):
			t = threading.Thread(target=animate)
			t.start()
			time.sleep(4)
			done = True
			break
		
		os.chdir(r"packages/") 
		os.system("ls")
		toolStatus("update    ", True)
		
		
	except(KeyboardInterrupt, SystemExit):
		print("\n"+tag3+"Tool Interrruped")
		done = True
		exit(0)
	
		
def toolStatus(package, doqPackage):
	
	done = False
	def animate():
		for c in itertools.cycle([
		white+" Instaling Package         ",
		WARNING+"->"+white+" Instaling Package        ",
		WARNING+"-->"+white+" Instaling Package       ",
		WARNING+"--->"+white+" Instaling Package      "]):
			if done == True:
				break
			sys.stdout.write("\r"+tag+c)
			sys.stdout.flush()
			time.sleep(0.2)
		

	os.system("clear")
	print(tag+"Do you want to install "+package+" /Package?")
	chserPackage = input(tag2+"Press yes to confirm instalation > ")
	print("")
	print("   *-----------------------------*")
	print("   |     * "+blue+"Crizzer status"+white+" *      |")
	print("   |                             |")
	print("   | "+WARNING+"Installing: "+magenta+package+white+"      |")
	print("   |"+WARNING,dateTimeNow,white+"       |")                            
	print("   *-----------------------------*")
	print("")
	
	try:
		while(True):
			t = threading.Thread(target=animate)
			t.start()
			time.sleep(0.7)
			done = True
			print("\n"+tag2+"Starting installation")
			break
			
	except(KeyboardInterrupt, SystemExit):
		print("\n"+tag3+"Tool Interrruped")
		done = True
		exit(0)
	
	if(doqPackage == True):
		if(package == "update    "):
			if (chserPackage == "yes" or chserPackage == "y"):
				os.system("exit")
				os.system("pkg upgrade && apt update && apt upgrade")
				print("")
				print(tag1+"Successful install")
				toolStatus("default   ", True)
			else:
				print(tag3+"Canceled")
				toolStatus("default   ", True)
				
		elif(package == "default   "):
			if (chserPackage == "yes" or chserPackage == "y"):
				os.system("chmod +x default.sh")
				os.system("./default.sh")
				print("")
				print(tag1+"Successful install")
				toolStatus("hydra     ", True)
			else:
				print(tag3+"Canceled")
				toolStatus("hydra     ", True)
				
		elif(package == "hydra     "):
			if (chserPackage == "yes" or chserPackage == "y"):
				os.system("apt install -y hydra")
				print("")
				print(tag1+"Successful install")
				toolStatus("crunch    ", True)
			else:
				print(tag3+"Canceled")
				toolStatus("crunch    ", True)
		
		elif(package == "crunch    "):
			if (chserPackage == "yes" or chserPackage == "y"):
				os.system("apt install -y unstable-repo")
				os.system("apt install -y crunch")
				print("")
				print(tag1+"Successful install")
				toolStatus("ipTracer  ", True)
			else:
				print(tag3+"Canceled")
				toolStatus("ipTracer  ", True)
				
		elif(package == "ipTracer  "):
			if (chserPackage == "yes" or chserPackage == "y"):
				os.system("apt install -y git")
				os.system("git clone https://github.com/Rajkumrdusad/IP-Tracer.git")
				os.chdir(r"IP-Tracer/") 
				os.system("chmod +x install.sh")
				os.system("./install.sh")
				print("")
				print(tag1+"Successful install")
				os.chdir(r"../") 
				toolStatus("blackNet  ", True)
			else:
				print(tag3+"Canceled")
				toolStatus("blackNet  ", True)
				
			
				
		elif(package == "blackNet  "):
			if (chserPackage == "yes" or chserPackage == "y"):
				os.system("apt install -y git")
				os.system("git clone https://github.com/Dyoniso/Blacknet-Online")
				os.system("mv Blacknet-online ~/")
				print("")
				print(tag1+"Successful install")
				toolStatus("sqlmap    ", True)
			else:
				print(tag3+"Canceled")
				toolStatus("sqlmap    ", True)
				
		elif(package == "sqlmap    "):
			if (chserPackage == "yes" or chserPackage == "y"):
				os.system("apt install -y git")
				os.system("git clone https://github.com/sqlmapproject/sqlmap")
				os.system("mv sqlmap ~/")
				print("")
				print(tag1+"Successful install")
				toolStatus("fl00d     ", True)
			else:
				print(tag3+"Canceled")
				toolStatus("fl00d     ", True)
				
				
		elif(package == "fl00d     "):
			if (chserPackage == "yes" or chserPackage == "y"):
				os.system("apt install -y curl")
				os.system("mkdir ~/fl00d")
				os.system("curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py")
				os.system("curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py")
				os.system("mv fl00d.py ~/fl00d && mv fl00d2.py ~/fl00d")
				print("")
				print(tag1+"Successful install")
				toolStatus("metasploit", True)
			else:
				print(tag3+"Canceled")
				toolStatus("metasploit", True)
				
				
		elif(package == "metasploit"):
			if (chserPackage == "yes" or chserPackage == "y"):
				os.system("apt install -y metasploit")
				os.system("curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh")
				os.system("chmod +x metasploit.sh")
				os.system("./metasploit.sh")
				print("")
				print(tag1+"Successful install")
				toolStatus("rtrsploit ", True)
			else:
				print(tag3+"Canceled")
				toolStatus("rtrsploit ", True)
				
		elif(package == "rtrsploit "):
			if (chserPackage == "yes" or chserPackage == "y"):
				os.system("apt install -y git")
				os.system("git clone https://github.com/threat9/routersploit.git")
				print(tag+"Installing pip - Requirements.txt and Requirements-dev.txt"+"\n")
				os.chdir(r"routersploit/") 
				time.sleep(1)
				os.system("pip install -r requirements.txt")
				os.system("pip install future")
				os.system("pip install -r requirements-dev.txt")
				os.chdir(r"../") 
				os.system("mv routersploit ~/")
				print("")
				print(tag1+"Successful install")
				toolStatus("nmap      ", True)
			else:
				print(tag3+"Canceled")
				toolStatus("nmap      ", True)
				
			
		elif(package == "nmap      "):
			if (chserPackage == "yes" or chserPackage == "y"):
				os.system('apt install -y nmap')
				print("")
				print(tag1+"Successful install")
				toolStatus("ngrok     ", True)
			else:
				print(tag3+"Canceled")
				toolStatus("ngrok     ", True)
			
		elif(package == "ngrok     "):
			if (chserPackage == "yes" or chserPackage == "y"):
				os.system("apt install -y git")
				os.system("git clone https://github.com/PSecurity/ps.ngrok.git")
				print("oi")
				os.chdir("ps.ngrok/")
				os.system("chmod +x ngrok")
				os.chdir("../")
				os.system("mv ps.ngrok ~/")
				print("")
				print(tag1+"All Packages Succeful instaled. Enjoy")
				print(tag1+"Thanks for using this tool")
				exit()
			else:
				print("")
				print(tag1+"All Packages Succeful instaled. Enjoy")
				print(tag1+"Thanks for using this tool")
				exit()
	
			
	elif(doqPackage == False):
		print("")
		print(tag1+"All Packages Succeful instaled. Enjoy")
		print(tag1+"Thanks for using this tool")
		exit()
		

	
