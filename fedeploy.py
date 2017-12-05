
from sys import exit
from fireeye import Fireeye
import getpass



def menu(fireeye):
	print("""Welcome to the FireEye Deployment Script - Platinum Deluxe Edition.\n""")
	print("Choose an option: \n")
	options = input("1. Create backup jobs. \n2. Hail Mary (All of the above). \n3. Device Management \n4. Query Devices \n5. Update and Reboot Devices \nQ. Quit \n\nEnter: ") 
	if options == "1": 
		fireeye.backup()
	elif options == "2":
		fireeye.backup()  
		fireeye.ldap()
	elif options == "3":
		fireeye.info()
	elif options == "4":
		fireeye.query()
	elif options == "5":
		fireeye.update()
	elif options == "Q" or "q":
		exit()
	else:
		print("Invalid option.")
		pass


if __name__ == '__main__':
	fireeye = Fireeye()
	fireeye.user = input("Enter username: ").lower()
	fireeye.token = getpass.getpass("Enter password: ")
	fireeye.devices = []
	with open("iplist.txt" , "r") as file:
		for line in file:
			line = line.replace("\n" , "")
			fireeye.devices.append(line)
		file.close()
		
	while True:
		menu(fireeye)

