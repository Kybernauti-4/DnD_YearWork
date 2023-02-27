import os
import json

def addSP(path, storyStack, story_index, SP_ID):

	for root, directories, files in os.walk('story'):
		# Iterate over the files in the current folder
		for filename in files:
			# Check if the file is named "storypart.txt"
			if filename == "storypart.json":
				ID = json.load(open(os.path.join(root, filename), 'r'))['ID']
				if ID == SP_ID:
					path_parts = path.split('\\')
					for part in path_parts:
						if part == 'story':
							path_parts = path_parts[:path_parts.index(part)]
					path = '\\'.join(path_parts)

					storyStack.insert(story_index+1, os.path.join(path, root))
					return