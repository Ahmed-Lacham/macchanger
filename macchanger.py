#!/usr/bin/venv python3

import subprocess
import argparse

try:
	ar=argparse.ArgumentParser(description="Mac Changer by Ahmed Lacham ")
	ar.add_argument("-i","--interface",help="inser you interface")
	ar.add_argument("-m","--mac",help="inser you mac")
	args=ar.parse_args()

	a=subprocess.check_output("ifconfig "+args.interface+" | grep ether | awk {'print $2'}",shell=True)

	print("[+] The old mac adress "+str(a.decode('utf-8')))
	subprocess.run(["ifconfig", args.interface, "down"])

	# Set the new MAC address
	subprocess.run(["ifconfig", args.interface, "hw", "ether", args.mac])

	# Bring the interface back up
	subprocess.run(["ifconfig", args.interface, "up"])
	b=subprocess.check_output("ifconfig "+args.interface+" | grep ether | awk {'print $2'}",shell=True)

	print("[+] The new mac address is "+str(b.decode('utf-8')))
	if  a != b:
		print("[+] The mac address has been changed ")

	else:
		print("[-] No change in mac address")
except TypeError:
	print("Syntax: python3 macchanger.py --help")

