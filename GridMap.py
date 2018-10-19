import numpy as np
class WeightedGrid():

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.walls = np.zeros(width*height)
		self.walls = self.walls.reshape(width, height)
#		for i in range(0, width):
#			for j in range(0, height):
#				self.walls[(i,j)] = 0
	def wallPositions(self, posit):
		for k in posit:
			(i, j) = k
			self.walls[i][j] = 1

	def createXYLine(self, xi, yi, xf, yf):
		for x in range(xi, xf+1):
			for y in range(yi, yf+1):
				self.wallPositions([(x,y)])
	def createWallsFromLine(self, xi, yi, xf, yf):
		xi = int(xi)
		xf = int(xf)
		yi = int(yi)
		yf = int(yf)

		if(xf == xi or yf == yi):
			self.createXYLine(xi,yi,xf,yf)
		else:
			self.wallPositions([(xi,yi)])
			self.wallPositions([(xi,yi+1)])
			self.wallPositions([(xf,yf)])
			m = float((yf-yi))/(xf-xi)
			lastx = xi
			lasty = yi
			passox = 1
			passoy = 1
			if(xi > xf):
				passox = 1
			if(yi > yf):
				passoy = 1
			for x in range(xi+1, xf, passox):
				for y in range(yi+1, yf, passoy):
					m2 = float(y - lasty)/(x - lastx)
					if(m2 >= m):
						self.wallPositions([(x,y)])
						self.wallPositions([(x,y+1)])
						yi = y
						lasty = y
						break
					self.wallPositions([(x,y)])
				lastx = x
	def createMachineSpot(self, xi, xf, width, height):
		pass
	def printmap_bfs(self):
		for j in range(0,self.height):
			mystring = ""
			for i in range(0, self.width):
				#if((i,j) == (0,1)): print self.walls[(i, j)]
				if(self.walls[(i, j)] == 1):
					mystring += "# "
				elif(self.walls[(i, j)] == 20):
					mystring+= "@ "
				else : mystring += ". "
			print mystring
	def printForReal(self, haha):
		pass
	def inBounds(self, node):
		(x,y) = node
		return (0 <= x < self.width) and (0 <= y < self.height)
	def isPassable(self, node):
		(i, j) = node
		return self.walls[i][j] == 0

	def myFilterPassable(self, nodes):
		arr = np.zeros(0)
		for n in range(0, len(nodes), 2):
			i = int(nodes[n])
			j = int(nodes[n+1])
			if (self.walls[i][j] == 0):
				arr = np.append(arr, n)
		return arr
	def myFilterBounds(self, nodes):
		arr = np.zeros(0)
		for a in nodes:
			(x,y) = a
			if ((0 <= x < self.width) and (0 <= y < self.height)):
				arr = np.append(arr, a)
		return arr
	def getNeighbors(self, node):
		(x,y) = node
		neighbors = [(x+1, y), (x+1, y+1),(x, y+1), (x-1, y+1),(x-1, y),(x-1, y-1),(x, y+1),(x+1, y-1)]
		#filtrar vizinhos invalidos
		neighbors = self.myFilterBounds(neighbors)
		neighbors = self.myFilterPassable(neighbors)
		#neighbors = filter(self.inBounds, neighbors)
		#neighbors = filter(self.isPassable, neighbors)
		#for k in neighbors:
		#	(i, j) = k
		#	if(self.walls[i][j]==1): 
		#		neighbors.remove(k)
		return neighbors
	def cost(self, from_node, to_node):
		(xo,yo) = from_node
		(xf, yf) = to_node
		if(abs(xo - xf) + abs(yo - yf) >= 2):
			return 1.4
		else :   
			return 1
		
if __name__ == '__main__':
	gm = WeightedGrid(100,100)
	gm.createWallsFromLine(0,0, 30,30)
	gm.createWallsFromLine(30,30, 60, 0)
	gm.printmap_bfs()