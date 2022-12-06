import os

def createStructure(folder):
    folderContains = os.listdir(os.getcwd()+'\\python\\'+folder)

createStructure('story')