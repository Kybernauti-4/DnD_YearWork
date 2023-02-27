import os
import json

def addSP(storyStack, story_index, SP_ID):

	for root, directories, files in os.walk('story'):
		# Iterate over the files in the current folder
		for filename in files:
			# Check if the file is named "storypart.txt"
			if filename == "storypart.json":
				ID = json.load(open(os.path.join(root, filename), 'r'))['include']
				if ID == SP_ID:
					storyStack.insert(story_index, os.path.join(root, filename))
					return