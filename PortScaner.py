import socket , sys
import MyScreen   as screen


def scan():
  hostIp = screen.getTargetIp()
  rangeStart = screen.getTargetStartRange()
  rangeEnd   = screen.getTargetEndRange()

  for portNumber in range(rangeStart,rangeEnd):
    scanPort(portNumber)
              
			  
def scanPort(portNumber):
  currentSocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
  currentSocket.settimeout(1)
  result = currentSocket.connect_ex((host,portNumber))
  if result == 0:
    service = getservbyport(portNumber)
	screen.printOpenPortInfo(service, portNumber)
	return
  screen.printClosePortInfo(portNumber)
   
	
