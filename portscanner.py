# socket library allows us to communicate with the machine using tcp and udp protocols.
import socket

def final_results():
    pass

def scan_port(ipaddress, port):
    # if the scanner manages to connect to the port, try block will run, else the program will go to the except block.
	try:
        	# sock is a socket object.
		sock = socket.socket()
        	# connecting to our target and port.
		sock.connect((ipaddress, port))
        	# closing the socket object
		sock.close()
		return "[+] Port " + str(port) + " Open"

	except:
		return "[-] Port " + str(port) + " Closed"

target_option = int(input("[*] Press: -\ni) 1 to scan a single IP address.\nii) 2 to scan multiple IP addresses.\n"))

port_option = int(input("[*] Press: -\ni) 1 to scan first n ports.\nii) 2 to scan specified ports.\n"))

if target_option == 1:
    target = input("[*] Enter the target IP address: ")
else:
    raw_targets = input("[*] Enter the target IP addresses separated by comma: ")
    targets = raw_targets.split(",")

if port_option == 1:
    n = int(input("[*] Enter the Port number upto which you want to scan: "))
else:
    raw_ports = input("[*] Enter the Port Numbers separated by comma: ")
    ports = raw_ports.split(",")

print("[*] Beginning the scan...")

if target_option == 1:
    if port_option == 1:
        print("Result for " + str(target) + ": -")
        for port in range(1, n+1):
            print(scan_port(target, port))
    else:
        print("Result for " + str(target) + ": -")
        for port in ports:
            print(scan_port(target, int(port)))
else:
    if port_option == 1:
        for target in targets:
            print("Result for " + str(target) + ": -")
            for port in range(1, n+1):
                print(scan_port(target, port))
    else:
        for target in targets:
            print("Result for " + str(target) + ": -")
            for port in ports:
                print(scan_port(target, int(port)))

