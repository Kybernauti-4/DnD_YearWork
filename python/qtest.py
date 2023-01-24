import os

data = {
		'cd':[[item for item in os.listdir() if os.path.isdir(item)], 'No directory found'],
}
extra_data = {
	'up':[[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0], 'No data found'],
}

data.update(extra_data)
print(data)