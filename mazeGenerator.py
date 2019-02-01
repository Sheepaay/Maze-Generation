import cell as cellClass
import array
import pygame
from pygame.locals import *
import generationAlgorithm

class maze:
	def setUp(self):
		try:
			countx = 0
			county = 0
			holdingList = []
			for county in range( 0, int( self.numberOfYCell ) ) :
				for countx in range( 0, int( self.numberOfXCell ) ) :
					cellAdding = cellClass.abstractCell()

					cellAdding.width = self.cellWidth
					cellAdding.height = self.cellHeight

					cellAdding.x = countx*self.cellWidth
					cellAdding.y = county*self.cellHeight

					holdingList.append( cellAdding )
				self.cells.append( holdingList )
				holdingList = []

			for cellList in self.cells :
				for cell in cellList :
					cell.findvalidNeighbours( self )

			generator = generationAlgorithm.stack()

			self.cells = generator.generate( self )

		except :
			print ("setup failure")

			
	def __init__ ( self, passedoWidth, passedoHeight, passedcellWidth, passedcellHeight ) :
		self.oWidth = passedoWidth
		self.oHeight = passedoHeight
		self.cellWidth = passedcellWidth
		self.cellHeight = passedcellHeight
		self.numberOfXCell = self.oWidth/self.cellWidth
		self.numberOfYCell = self.oHeight/self.cellHeight
		self.cells = []
		self.setUp()

	def render(self):
		linecolour = (255, 136, 197)
		backgroundColour = ( 255, 255, 255, 255)
		pygame.init()
		surface = pygame.display.set_mode([self.oWidth,self.oHeight])
		surface.fill(backgroundColour)
		for x in self.cells:
			for cell in x: 
				cell.render(surface, linecolour)

