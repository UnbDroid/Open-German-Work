import collections
import GridMap
import heapq
class MyPriorityQueue:
    def __init__(self):
        self.elements = []
    def isEmpty(self):
        return len(self.elements) == 0
    
    def add(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def pop(self):
        return heapq.heappop(self.elements)[1]

def heuristic(a, b):
	(x1, y1) = a
	(x2, y2) = b
	return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, inicio, final):
	current = final
	path = []
	while current != inicio:
		path.append(current)
		current = came_from[current]
	path.append(inicio)
	#path.reverse()
	return path

def A_star(graph,inicial, final):
	pqueue = MyPriorityQueue()
	pqueue.add(inicial, 0)
	came_from = {}
	cost_so_far = {}
	came_from[inicial] = None
	cost_so_far[inicial] = 0
	while not pqueue.isEmpty():
		current = pqueue.pop()
		if current == final:
			break #se chegar no final, sai
		#for nextTo in graph.getNeighbors(current):
		for i, k in zip(graph.getNeighbors(current)[0::2], graph.getNeighbors(current)[1::2]):
			nextTo = (i, k)
			print nextTo
			new_cost = cost_so_far[current] + graph.cost(current, nextTo)
			if nextTo not in cost_so_far or new_cost < cost_so_far[nextTo]:
				cost_so_far[nextTo] = new_cost
				priority = new_cost + heuristic(final, nextTo)
				pqueue.add(nextTo, priority)
				came_from[nextTo] = current
	return came_from, cost_so_far
def A_star_teste():
	#gm = GridMap.WeightedGrid(30,30)
	#gm.createWallsFromLine(3,0, 3, 20)
	#gm.createWallsFromLine(20,10, 20,30)
	#gm.createWallsFromLine(25,20, 30,20)
	width = 800
	height = 400
	gm = GridMap.WeightedGrid(width, height)
	gm.createWallsFromLine(width*0.3, 0, width*0.3, height/3.5)
	gm.createWallsFromLine(width*0.3, height, width*0.3, 2.2*height/3.5)
	gm.createWallsFromLine(width*0.5, height/4, width*0.5, 3*height/4)
	gm.createWallsFromLine(width*0.7, height/4, width*0.7, 3*height/4)
	final = (width-50,int(height/2))
	inicio = (0,0)
	#final = (29,29)
	mypath, lala = A_star(gm, inicio, final)
	path = reconstruct_path(mypath, inicio, final)
	for i in path:
		gm.walls[i] = 20
	print path.pop()
	#path

	#gm.printmap_bfs()

import timeit

start = timeit.default_timer()
A_star_teste()
#Your statements here

stop = timeit.default_timer()

print stop - start 