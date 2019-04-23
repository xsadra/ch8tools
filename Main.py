import MyScreen as screen
import MyOperation as command

screen.clear(4)
screen.sleep()

screen.drawTheLogo()
screen.showCreatorInfo()
screen.sleep()

option = screen.getMainMenuOption()
command.execute[option]()
