import random, pygame 

class stack:
	def __init__ (self):
		self.stack = []

	def finished (self, cells):
		result = True
		for celllist in cells:
			for cell in celllist: 
				if cell.visited == False: 
					result = False
					break
		return result 

	def generate (self, maze):
		cells = maze.cells
		currentCell = cells[0][0]
		currentCell.visited = True
		while not self.finished(cells):
			currentCell.visited = True
			currentCell.findvalidNeighbours(maze)
			if currentCell.neighbours != []:
				chosen = random.choice(currentCell.neighbours)
				self.stack.append(currentCell)
				joiningwall = currentCell.findWall(chosen)
				if joiningwall == 0:
					currentCell.northWallBroken = True 
					chosen.southWallBroken = True
				if joiningwall == 1:
					currentCell.eastWallBroken = True 
					chosen.westWallBroken = True
				if joiningwall == 2:
					currentCell.southWallBroken = True
					chosen.northWallBroken = True
				if joiningwall == 3:
					currentCell.westWallBroken = True
					chosen.eastWallBroken = True
				currentCell = chosen 
			else: 
				chosen = self.stack.pop()
				currentCell = chosen 
		return cells 








