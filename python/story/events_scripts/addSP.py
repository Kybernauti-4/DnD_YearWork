import os
import json

def addSP(path, story_root, storyStack, story_index, SP_ID):
	for root, directories, files in os.walk(story_root):
		# Iterate over the files in the current folder
		for filename in files:
			# Check if the file is named "storypart.json"
			if filename == "storypart.json":
				ID = json.load(open(os.path.join(root, filename), 'r'))['ID']
				if ID == SP_ID:
					storyStack.insert(story_index+1, root)
					return