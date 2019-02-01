import pygame
from pygame.locals import *
class abstractCell:
	def __init__ (self):
		"cell basic class"
		self.northWallBroken = False
		self.eastWallBroken = False
		self.westWallBroken = False 
		self.southWallBroken = False

		"if visited"
		self.visited = False 
		self.neighbours = []

		"coords"
		self.x = 0 
		self.y = 0

		self.height = 0 
		self.width = 0


	def render(self, surface, linecolour):
		if not self.northWallBroken:
			pygame.draw.line(surface, linecolour, (self.x, self.y), (self.x+self.width, self.y), 1)
		if not self.eastWallBroken:
			pygame.draw.line(surface,linecolour, (self.x+self.width, self.y), (self.x+self.width, self.y+self.height), 1)
		if not self.westWallBroken:
			pygame.draw.line(surface, linecolour, (self.x, self.y), (self.x, self.y+self.height), 1)
		if not self.southWallBroken:
			pygame.draw.line(surface, linecolour, (self.x, self.y+self.height), (self.x+self.width, self.y+self.height),1)
	def findvalidNeighbours(self, maze):

		try :
			self.neighbours = []
			positionX = int(self.x/maze.cellWidth)
			positionY = int(self.y/maze.cellHeight)
			#north neighbour
			if positionY > 0 and maze.cells[positionY-1][positionX].visited == False :
				self.neighbours.append( maze.cells[positionY-1][positionX] )

			#east neighbour
			if positionX*maze.cellWidth < maze.oWidth-maze.cellWidth and maze.cells[positionY][positionX+1].visited == False:
				self.neighbours.append( maze.cells[positionY][positionX+1] )

			#south neighbour
			if positionY*maze.cellHeight < maze.oHeight-maze.cellHeight and maze.cells[positionY+1][positionX].visited == False :
				self.neighbours.append( maze.cells[positionY+1][positionX] )

			#west neighbour
			if positionX > 0 and maze.cells[positionY][positionX-1].visited == False :
				self.neighbours.append( maze.cells[positionY][positionX-1] )

		except :
			print ( self, "@", self.x, ", ", self.y, ", failed to find neighbour" )
			print ("")

	def findWall (self, cell):
		if self.x == cell.x and self.y - cell.height == cell.y:
			return 0 #N
		if self.y == cell.y and self.x + cell.width == cell.x:
			return 1 #E
		if self.x == cell.x and self.y + cell.height == cell.y: 
			return 2 #S
		if self.y == cell.y  and self.x - cell.width == cell.x:
			return 3 #W
