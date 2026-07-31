import socket 

def scanner_banner():
    print("=" * 30)
    print("Simple Port Scanner v2")
    print("=" * 30)

def get_target():
    ip = input("Enter Target IP: \n")
    start_port = int(input("Enter start port: \n"))
    end_port = int(input("Enter end port: \n"))
    
    return ip, start_port, end_port

def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        s = socket.socket()
        s.settimeout(1)
        
        try:
            s.connect((ip, port))
            open_ports.append(port)
        except:
            pass
        s.close()
    return open_ports
    
def show_results(ip, open_ports):
    
    print("\n" + "=" * 30)
    print("Scan Finished")
    print(f"Target --> {ip}")
    print("=" * 30)
    
    print("Open Ports:")
    for port in open_ports:
        
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unkown"
        print(f"Port    : {port}")
        print(f"Service : {service}")
        print("-" * 30)
    print(f"Total Open Ports : {len(open_ports)}")      
    
scanner_banner()
ip, start_port, end_port = get_target()
open_ports = scan_ports(ip, start_port, end_port)
show_results(ip, open_ports)
