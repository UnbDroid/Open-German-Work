import GridMap as gm 
aff = gm.WeightedGrid(400, 400)
with open('mapFile', 'r') as mf:
	for line in mf.readlines():
		line = line.rstrip()
		line = line.split(',')
		if(line[0] == 'rect'):
			aff.createXYLine(int(line[1]),int(line[2]), int(line[1]) + int(line[3]),int(line[2]) + int(line[4]))
		elif(line[0] == 'semirect'):
			pass
		elif(line[0] == 'circle'):
			pass
aff.printmap_bfs()