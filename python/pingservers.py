import socket
from pythonping import ping
filename="myservers.txt"

with open(filename,'r') as f:
    for line in f:
        try:
            server=line.strip()
            print("checking connectivity with server address: "+ server)
            r=ping(server, verbose=True)
            if r.success():
                print(server+" is live")
            else:
                print("Site is not live")
        except (socket.gaierror, RuntimeError):
             print(f"{server} is not live (Invalid Address or DNS issue)\n")        
f.close

