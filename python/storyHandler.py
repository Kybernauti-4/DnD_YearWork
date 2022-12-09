import os

def createStructure(folder):
    depth = 0
    path = os.path.join(os.getcwd(),folder)
    folderDepthCounter(path)
    
    print(depth)
            
def folderDepthCounter(path):
    curr_path = path
    curr_depth = 0
    iterloop(curr_path,0)
    def iterloop(curr_path, my_number):
        layer = os.listdir(curr_path)
        for item in layer:
            if allFiles(os.listdir(os.path.join(curr_path,item))):
                return my_number
            if os.path.isdir(os.path.join(curr_path,item), my_number+1):
                iterloop(os.path.join(curr_path,item), my_number+1)
    return depth

def allFiles(layer):
	iterator = iter(layer)
	try:
		first = next(iterator)
	except StopIteration:
		return True
	return all(os.path.isfile(first) == os.path.isfile(x) for x in iterator)

createStructure('story')