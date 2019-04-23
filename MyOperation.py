import MyScreen   as screen
import DDosAttack as DDoS
import HashMaker  as hMaker
import PortScaner as pScanner


execute = {
  1:dDosAttack,
  2:hashMaker
  3:portScaner
  99:exit
}

def dDosAttack():
  DDoS.attack()
  
def hashMaker():
  hMaker.make()
  
def portScaner():
  pScanner.scan()

def exit():
  screen.clear()