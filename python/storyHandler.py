import os

def createStructure(folder):
    
    depth = 0
    path = os.path.join(os.getcwd(),folder)
    list_files(path)
    depth = depthFinder(path)
    
    #TODO build the multi dimensional dict and story.json

            
def depthFinder(startpath):
    max_level = 0
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        max_level = level if level > max_level else max_level

    return max_level

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

createStructure('story')