import socket
#ip = input("Enter Target ip: ")
#start_port = int(input("Enter start port: "))
#end_port = int(input("Enter end port: "))

#for port in range(start_port, end_port + 1):
#    s = socket.socket()
#    s.settimeout(1)
    
#    try:
#        s.connect((ip, port))
#        print(f"Port {port} : Open")
#    except:
#        print(f"Port {port} : Closed")
#    s.close()

#-----------------------------------------------------------------------

ip = input("Enter Target IP: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

for port in range(start_port, end_port + 1):
    s = socket.socket()
    s.settimeout(1)
    
    try:
        s.connect((ip, port))
        print(f"Port {port} : Open")
    except:
        pass
    s.close()