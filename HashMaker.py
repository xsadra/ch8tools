import hashlib
import MyScreen as screen


execute = {
  1:md5,
  2:sha1,
  3:sha224,
  4:sha256,
  99:exit
}

def make():
  screen.setColorToBlue()
  screen.showHashMakerTitle()
  screen.showCreatorInfo()
  screen.sleep()
  
  text = screen.getTextToEncode()
  option = screen.getHashMakerMenuOption()
  
  execute[option](text)
  
  
def md5(text):
  md5 = hashlib.md5()
  md5.update(text)
  hashValue = md5.hexdigest()
  screen.printHash("MD5", hashValue)

def sha1(text):
  sha1 = hashlib.sha1()
  sha1.update(text)
  hashValue = sha1.hexdigest()
  screen.printHash("SHA-1", hashValue)


def sha224(text):
  sha224 = hashlib.sha224()
  sha224.update(text)
  hashValue = sha224.hexdigest()
  screen.printHash("SHA-224", hashValue)
  
def sha256(text):
  sha256 = hashlib.sha256()
  sha256.update(text)
  hashValue = sha256.hexdigest()
  screen.printHash("SHA-256", hashValue)

def exit(text):
  screen.clear()