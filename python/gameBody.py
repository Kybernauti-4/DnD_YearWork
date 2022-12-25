import comm
import deviceHandler

#TODO Create a game body

#? I need to implement an event stack that advances each round
#* Create a list of players either through comm or through searching in files

def getPlayers():
    devicesList = deviceHandler.findDevices()
    playerlist = []
    for player in devicesList:
        comm.sendMessage(player, 'sendpdata')
        comm.readMessageBlock(player, True)