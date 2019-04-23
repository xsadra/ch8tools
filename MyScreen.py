import os , time


class color:

    purple = '\033[34m'
    blue = '\033[94m'
    Green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'

def sleep():
  time.sleep(3)

def clear(count = 1):
  for tmp in range(count):
    os.system("clear")
		
def drawTheLogo():
  print color.red +  '''

       ,#############################,
       ################################
      ##################################
      ###                            ###
      ###   $$$$$            $$$$$   ###
      ###   $$$$$            $$$$$   ###
      ###    ```      """     ```    ###
       ###           """""          ###
       ###           """""          ###
        ###                        ###
         ###                      ###
          ###                    ###
             ====================
             =||||||||||||||||||=
             =------------------=
             =||||||||||||||||||=
             ====================

''' + color.end

def showdrawCreatorInfo():
  print color.purple + ''' Code By : Crazy8          Telegram : @LightGreen_heart
''' + color.end



def getMainMenuOption():
  print color.yellow +  '''

[1] DDoS Attack

[2] Hash Maker

[3] Port Sccaner

[99] Exit

''' + color.end
  return raw_input(color.Green + " CH8 > " + color.end)
  
def getUrl():
  return raw_input(color.blue + "Enter your site url => ")

def getThreadCount():
  return input("Enter your thread => ")


def showTargetInfo(ip, port):
 print "UDP target IP:", ip
 print "UDP target port:", port

def setColorToBlue():
  print color.blue + "   "
  
  
def showHashMakerTitle():
  print pyfiglet.figlet_format('Hash Maker' , font = 'slant')


def getHashMakerMenuOption():
  
 print color.yellow +  '''

[1] MD5

[2] SHA-1

[3] SHA-224

[4] SHA-256

[99] EXIT

''' + color.end

 return raw_input(" enter the number : ")

def getTextToEncode():
  return raw_input(color.red + "Enter Your Text for hashing : " )
  
def printHash(hashName, hashValue):
  print color.Green + "{+} "+ hashName +" your password is >>> ",hashValue

def getTargetIp():
  return raw_input(color.Green + "Enter Your Target ip : ")

def getTargetStartRange():
  return int(input("Enter start range Port : "))

def getTargetEndRange():
  return int(input("Enter end range Port : "))
  
def printOpenPortInfo(service, portNumber):
  print "[+] Port : " ,service,portNumber,"open"
  
def printClosePortInfo(portNumber):
  print "[+] Port : " , portNumber, "close"
  