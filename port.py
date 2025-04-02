# Written By OM [byt-ctrl]
# PORT - SCANNER

import socket
from datetime import datetime

def scanning_port (targeted_ip,port):
    try:
        # Creating a socket object and stting the timeout
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.5)

        # We try to connect to target the IP and port 
        result=sock.connect_ex((targeted_ip,port))


        if result==0 :
            print(f"PORT {port} is OPEN")

        else :
            print(f"PORT {port} is CLOSED")


        sock.close()# Close the socket after the connection attempt 
    
    except socket.error:  
        print(f"Couldn't connect to {targeted_ip} on PORT {port}")
        return
    


def scan_ports (target_ip,start_port,end_port):
    print(f"Starting The Scanning to {target_ip} at {datetime.now()}")

    for port in range(start_port,end_port+1):
         scanning_port(target_ip, port)
    
    print(f"Scan Completed at {datetime.now()}")


if __name__ == "__main__":
    default_start = 0
    default_end = 65565
    target_id= input("Enter the IP address or domain to scan :")
    start_port = input("Enter the starting PORT Number :")
    end_port = input("Enter The ending PORT Number :")

    if (start_port == '\n'):
        start_port = default_start
    else:
        start_port = int(start_port)

    if (end_port == '\n'):
        end_port = default_end
    else:
        end_port = int(end_port)
    
    scan_ports(target_id,start_port,end_port)


#END
