import sys
import os
if sys.version_info.major < 3:
    print("Crinzzer supports only Python3. Run the application in Python3 environment.")
    exit(0)
from core.crCore import *

def main():
	
	crizzerInput = input("*"+blue+" Crinzzer > "+white) 
	
	if(crizzerInput == "1"):
		confirmAcc = input(tag+"Press yes to confirm action > ") 	
		
		if(confirmAcc == "yes" or confirmAcc == "y"):
			letsCrizzer()
		else:
			exit()
	elif(crizzerInput == "2"):
		print("* Included packages *")
		print("+ Default Termux Packages")
		print("+ Hydra")
		print("+ Crunch")
		print("+ IpTracer")
		print("+ Blacknet-Online")
		print("+ Routersploit")
		print("+ SqlMap")
		print("+ Metaspoit")
		print("+ Nmap")
		print("+ Ngrok")
		print("")
		main()
		
if __name__ == "__main__":
	main()


	

