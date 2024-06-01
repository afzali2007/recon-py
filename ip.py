import socket

#       name site vorody
a = input("")
domain = a

ip_address = socket.gethostbyname(domain)

print(f"The IP address of {domain} is {ip_address}")

