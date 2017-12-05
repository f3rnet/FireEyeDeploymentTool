import socket
import pexpect
import colorama
from colorama import Fore , Back , Style


class Fireeye():

	def __init__(self):
		colorama.init()
		self.devices = []
		self.user = ''
		self.token = ''

	def update(self):

		def guest_image_download():
			print("This takes a very long time. Get comfortable.")
			for i in self.devices:
				try:
					ip = i
					print(" \nLogging into  {} as {}.\n".format(ip , self.user))
					#logging in
					child = pexpect.spawn("ssh {}@{}".format(self.user , ip) , timeout=3) 
					child.expect("Password: ")
					child.sendline(self.token)
					child.expect(">")
					child.sendline("en")
					child.expect("#")
					child.sendline("guest-image download")
					child.expect("#")
					child.sendline("exit")
					print("Guest Image fetched for {}".format(ip))
				except pexpect.TIMEOUT:
					child.close()
					print("Timeout on {}".format(i))
					pass

		def guest_image_install():
			for i in self.devices:
				ip = i
				print(" \nLogging into  {} as {}.\n".format(ip , self.user))
				#logging in
				child = pexpect.spawn("ssh {}@{}".format(self.user , ip)) 
				child.expect("Password: ")
				child.sendline(self.token)
				child.expect(">")
				child.sendline("en")
				child.expect("#")
				child.sendline("guest-image install")
				child.expect("#")
				child.sendline("exit")
				print("Installing image for {}".format(ip))
		
		def image_fetch():
			for i in self.devices:
				try:
					ip = i
					print(" \nLogging into  {} as {}.\n".format(ip , self.user))
					#logging in
					child = pexpect.spawn("ssh {}@{}".format(self.user , ip) , timeout=3) 
					child.expect("Password: ")
					child.sendline(self.token)
					child.expect(">")
					child.sendline("en")
					child.expect("#")
					child.sendline("configure terminal cmc-force")
					child.expect("#")
					child.sendline("fenet image fetch")
					child.expect("#")
					child.sendline("exit")
					print("Imaged fetched for {}".format(ip))
				except pexpect.TIMEOUT:
					child.close()
					print(Back.RED + "Timeout on {}".format(i) + Style.RESET_ALL)
					pass


		def image_install():
			for i in self.devices:
				try:
					ip = i
					print(" \nLogging into  {} as {}.\n".format(ip , self.user))
					#logging in
					child = pexpect.spawn("ssh {}@{}".format(self.user , ip)) 
					child.expect("Password: ")
					child.sendline(self.token)
					child.expect(">")
					child.sendline("en")
					child.expect("#")
					child.sendline("configure terminal cmc-force")
					child.expect("#")
					child.sendline("write mem")
					child.expect("#")
					child.sendline("exit")
					print("Latest imaged installed on {}".format(ip))
				except pexpect.TIMEOUT:
					child.close()
					print(Back.RED + "Timeout on {}".format(i) + Style.RESET_ALL)
					pass

		def reboot():
			import time
			import progressbar
			print(Back.RED + "****Do you really want to do this?****" + Style.RESET_ALL)
			print("Stop and think for a minute. You are about to systematically reboot every device in your list. Is this what you really want to do right now? Each device that is rebooted will be offline for approximately 10 minutes. Would be a shame to get fired for this, so make sure you know what you're doing.")
			rebootnow = input("Continue Y/N: ").lower()
			if rebootnow == "y":
				print("Okay this is gonna take awhile. You might wanna get some coffee or update your resume.")
				for i in self.devices:
					try:
						bar = progressbar.ProgressBar()
						ip = i
						print(" \nLogging into  {} as {}.\n".format(ip , self.user))
						#logging in
						child = pexpect.spawn("ssh {}@{}".format(self.user , ip)) 
						child.expect("Password: ")
						child.sendline(self.token)
						child.expect(">")
						child.sendline("en")
						child.expect("#")
						child.sendline("configure terminal cmc-force")
						child.expect("#")
						child.sendline("write mem")
						child.expect("#")
						child.sendline("reload")
						child.close()
						print("Rebooting {}".format(i))
						for i in bar(range(100)):
							time.sleep(6.0)
					except pexpect.TIMEOUT:
						child.close()
						print(Back.RED + "Timeout on {}".format(i) + Style.RESET_ALL)
					

		print(Back.RED + "***WARNING*** " * 3 + Style.RESET_ALL)
		print("This action will update the FireEye Appliances. \nUpdating requires each device to fetch the new images (approx 20 mins), then install the image (approx 10 mins), and then swapping to the new image. Finally, you will need to reboot each appliance for the install to finalize.")
		print("[1] Image Fetch \n[2] Image Install \n[3] Guest Image Download \n[4] Guest Image Install \n[5] Reboot")
		user_choice = input("Choose Wisely: ")
		if user_choice == "1":
			image_fetch()
		elif user_choice == "2":
			image_install()
		elif user_choice == "3":
			guest_image_download()
		elif user_choice == "4":
			guest_image_install()
		elif user_choice == "5":
			reboot()
		elif user_choice == "6":
			testtest()
		else:
			print("Invalid Option")
			pass



	def query(self):
		offline_count = 0
		online_count = 0
		print("\nQuerying your infrastructure from items in your device list...")

		print(Back.GREEN + "[ID]\t" +"[DEVICE]" , "\t", "[STATUS]" + Style.RESET_ALL)
		for i in self.devices:
			try:
				print(self.devices.index(i) , "\t" , i , "\t", socket.gethostbyaddr(i)[0])
				online_count += 1
			except Exception as ex:
				print(self.devices.index(i) , "\t" , i , "\t", Fore.RED , ex , Style.RESET_ALL)	#Style formatting by colorama
				offline_count += 1

		print("\nYou have {} devices in your list. There are {} reporting online and {} reporting offline.\n".format(len(self.devices), online_count , offline_count))

	def info(self):	

		def devices(self):
			print("\nYou have {} devices in your infrastructure.".format(len(self.devices)))
			print(Back.GREEN + "[ID]\t" +"[DEVICE]" , "\t", "[STATUS]" + Style.RESET_ALL)
			for i in self.devices:
				try:
					print(self.devices.index(i) , "\t" , i , "\t", socket.gethostbyaddr(i)[0])
				except Exception as ex:
					print(self.devices.index(i) , "\t" , i , "\t", Fore.RED , ex , Style.RESET_ALL)	#Style formatting by colorama
			print("\n1. Add Devices\n2. Work from a temporary device list.\n3. Remove all devices.")
			user_choice = input("Select: ")
			if user_choice == "1":
				add(self)
			elif user_choice == "2":
				delete(self)
			elif user_choice =="3":
				self.devices = []
				devices(self)
			else:
				pass



		def delete(self):
			print("Select a device / devices for removal. Enter device [ID] separated by commas.\n")
			for i in self.devices:
				print("[" , self.devices.index(i) , "] " , i)
			user_choice = input("Which devices would you like to delete? ")
			user_choice = user_choice.split(",")
			user_choice = [int(i) for i in user_choice]
			print("Deleting the folllowing devices from your working list. (non-permanent)")
			for i in user_choice:
				print(self.devices[int(i)])
			confirm = input("Are you sure you want to delete these from your list y/n? ").lower()
			if confirm == "y": 
				garbage_list = [name for index, name in enumerate(self.devices) if index not in user_choice]
				self.devices = garbage_list
			elif confirm == "n":
				delete(self)
			else:
				pass	

		def add(self):
			print("Enter device ip to add to pool.\n")
			new_device = input("ip: ")
			confirm = input("Are you sure you want to temporarily add {} to your pool? y/n ".format(new_device).lower())
			if confirm == "y":
				self.devices.append(new_device)
			elif confirm == "n":
				add(self)
			else:
				info(self)

		devices(self)

	#work in progress
	def run_backups(self):
		print("backing devices.....")
		password = self.token
		for i in self.devices:
			ip = i
			print(" \nLogging into  {} as {}.\n".format(ip , self.user))
			if ip == "done":
				print("Logging out... Goodbye!")
				return()
			#logging in
			child = pexpect.spawn("ssh {}@{}".format(self.user , ip)) 
			child.expect("Password: ")
			child.sendline(self.token)
			child.expect(">")
			child.sendline("en")
			child.expect("#")
			child.sendline("configure terminal cmc-force")
			child.expect("#")


	def backup(self):
		print("Creating backup jobs.....")
		password = self.token
		for i in self.devices:
			ip = i
			print(" \nLogging into  {} as {}.\n".format(ip , self.user))
			if ip == "done":
				print("Logging out... Goodbye!")
				return()
			#logging in
			child = pexpect.spawn("ssh {}@{}".format(self.user , ip)) 
			child.expect("Password: ")
			child.sendline(self.token)
			child.expect(">")
			child.sendline("en")
			child.expect("#")
			child.sendline("configure terminal cmc-force")
			child.expect("#")
			#will have to manually enter backup location & auth here. be smart about this. 
			#FE requires you to use a password that they will store in clear text. :-| 
			#You will need to configure the acct, pass, and location. I highly suggest you use a least priv acct.
			child.sendline("job 1 command 1 \"backup profile full to scp://your_fireeye_backup_acct:YOURACCTPASSWRDGOESHERE@yourbackuplocation.local/drive/d/backups/\"")
			child.expect("#")
			child.sendline("job 1 enable")
			child.expect("#")
			child.sendline("job 1 fail-continue")
			child.expect("#")
			child.sendline("job 1 schedule weekly day-of-week sun")
			child.expect("#")
			child.sendline("job 1 schedule weekly time 01:30:00")
			child.expect("#")
			child.sendline("show job 1")
			child.expect("#")
			child.sendline("write memory")
			child.expect("#")
			child.sendline("exit")
			child.expect("#")
			child.sendline("exit")
			print("Done.... on to the next one...")


	
