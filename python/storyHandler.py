import os

def createStructure(folder):
    depth = 0
    path = os.path.join(os.getcwd(),folder)
    depth = list_files(path)
    
    print(depth)
            
def list_files(startpath):
    max_level = 0
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        max_level = level if level > max_level else max_level
        
    return max_level

def allFiles(layer):
	iterator = iter(layer)
	try:
		first = next(iterator)
	except StopIteration:
		return True
	return all(os.path.isfile(first) == os.path.isfile(x) for x in iterator)

createStructure('story')