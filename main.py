import mazeGenerator as maze
import pygame
from pygame.locals import *  

class window:
	def __init__ (self):
		self.maze = maze.maze(400, 400, 20, 20)

	

window = window()
window.maze.render()
# print (window.maze.cells)
# print ("")
# print (window.maze.cells[0].x, ", ", window.maze.cells[0].y)
# print (window.maze.cells[0].height, "x", window.maze.cells[0].width)
# print ("")
# print (window.maze.cells[1].x, ", ", window.maze.cells[1].y)
# print (window.maze.cells[1].height, "x", window.maze.cells[1].width)
# print ("")
# print (window.maze.cells[2].x, ", ", window.maze.cells[2].y)
# print (window.maze.cells[2].height, "x", window.maze.cells[2].width)
# print ("")
# print (window.maze.cells[3].x, ", ", window.maze.cells[3].y)
# print (window.maze.cells[3].height, "x", window.maze.cells[3].width)
# print ("")

while True:
    for event in pygame.event.get() :
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # screen.renderMaze()
    pygame.display.update()
