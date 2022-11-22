comm = {'0':'Serial1', 'Giganto':0,'1':'Serial2','Magneto':1}

fix_count = 0
key = list(comm.keys())
val = list(comm.values())

while fix_count < (len(key) - 1):
	if(key[fix_count] == str(val[fix_count+1])):
		comm[str(key[fix_count+1])] = comm[str(key[fix_count])]
		comm.pop(str(key[fix_count]))
		key = list(comm.keys())
		val = list(comm.values())
		fix_count+=1
	else:
		fix_count+=1

print(comm)