import os

def createStructure(folder):
    path = os.getcwd()+'\\python\\'+folder
    folderContains = os.listdir(path)
    for file in folderContains:
        if os.path.isfile(os.path.join(path,file)):
            print("a")

createStructure('story')