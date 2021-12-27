import pygame
import pygame_menu
import random
# from Button import Button
import math as Math
from pygame.constants import RESIZABLE
from pygame_menu.locals import INPUT_FLOAT, INPUT_INT
from GraphAlgoInterface import GraphAlgoInterface

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 60)


class GUI:
    def _init_(self, graphAlgo: GraphAlgoInterface) -> None:
        self.graphAlgo = graphAlgo
        self.posX = 0
        self.posY = 0
        self.minX = float('inf')
        self.minY = float('inf')
        self.maxX = float('-inf')
        self.maxY = float('-inf')
        self.minMaxForMargins()
        pygame.init()
        pygame.font.init()

        self.GAME_FONT = pygame.font.SysFont('david', 15)
        self.screen = pygame.display.set_mode([800, 600], RESIZABLE)  # build screen

        self.display()

    def minMaxForMargins(self):
        #   finds the max and min x and y in order to understand the margins of the graph
        for vertex in self.graphAlgo.graph.nodes.values():
            if vertex.location is None or vertex.location == ():
                vertex.location = (random.uniform(0, 0.90), random.uniform(0, 0.90))
            x = vertex.location[0]
            y = vertex.location[1]
            if self.minY > y:
                self.minY = y
            elif self.maxY < y:
                self.maxY = y
            if self.minX > x:
                self.minX = x
            elif self.maxX < x:
                self.maxX = x

    def drawVertex(self):
        for vertex in self.graphAlgo.graph.nodes.values():
            diff_metric_x = vertex.location[0] - self.minX
            diff_metric_y = vertex.location[1] - self.minY
            # calculates the vertex position on the screen
            pos_x = diff_metric_x * self.posX + 25
            pos_y = diff_metric_y * self.posY + 25
            # draw vertex
            pygame.draw.circle(self.screen, red, (pos_x, pos_y), 8)
            # build text surface
            text_surface = self.GAME_FONT.render(str(vertex.key), 8, white)
            # write text on the vertex
            self.screen.blit(text_surface, (pos_x - 5, pos_y - 8))

    def drawEdges(self):
        allEdges = self.graphAlgo.graph.edges
        for edge in allEdges.keys():
            # get position of the vertices:
            # calculates the src point (x,y)
            srcX = self.graphAlgo.graph.nodes[edge[0]].location[0]
            srcX = (srcX - self.minX) * self.posX + 25
            srcY = self.graphAlgo.graph.nodes[edge[0]].location[1]
            srcY = (srcY - self.minY) * self.posY + 27

            # calculates the dest point (x,y)
            destX = self.graphAlgo.graph.nodes[edge[1]].location[0]
            destX = (destX - self.minX) * self.posX + 25
            destY = self.graphAlgo.graph.nodes[edge[1]].location[1]
            destY = (destY - self.minY) * self.posY + 27

            # draw the arrows line
            pygame.draw.line(self.screen, white, (srcX, srcY), (destX, destY), 4)

            # draw arrow
            self.arrow((srcX, srcY), (destX, destY), 15, 10)
            text_surface = self.GAME_FONT.render(f'{allEdges[edge]:.2f}', 10, white)

            # calculates the point for writing the text
            xText = srcX * 0.28 + destX * 0.77
            yText = srcY * 0.28 + destY * 0.77
            self.screen.blit(text_surface, (xText, yText))

    def addEdge(self):
        graph = self.graphAlgo.graph
        menu = pygame_menu.Menu('Add Edge', 450, 300, theme=pygame_menu.themes.THEME_ORANGE)
        src = menu.add.text_input('Src: ', input_type=INPUT_INT)
        dest = menu.add.text_input('Dest: ', input_type=INPUT_INT)
        weight = menu.add.text_input('Weight: ', input_type=INPUT_FLOAT)
        menu.add.button(f'Enter', self.doAddEdge, src, dest, weight, menu)
        menu.add.button('Exit', menu.disable)
        menu.mainloop(self.screen)
        return menu

    def doAddEdge(self, src, dest, weight, menu):
        print(f"src {src.get_value()}, dest {dest.get_value()}, w {weight.get_value()}")
        print(self.graphAlgo.graph.add_edge(src.get_value(), dest.get_value(), weight.get_value()))
        menu.disable()

    def arrow(self, startPoints, endPoints, d, height):
        # gets 2 lists-
        # 1. list of start point, where drawing the arrow supposed to start
        # 2. list of start point, where drawing the arrow supposed to end
        subX = endPoints[0] - startPoints[0]
        dX = float(subX)
        subY = endPoints[1] - startPoints[1]
        dY = float(subY)
        dYPower = Math.pow(dY, 2)
        dXPower = Math.pow(dX, 2)

        # vectors length
        length = float(Math.sqrt(dXPower + dYPower))
        xm = float(length - d)
        xn = float(xm)
        ym = float(height)
        yn = - height

        # normalized direction vector components
        sin = dY / length
        cos = dX / length

        x = xm * cos - ym * sin + startPoints[0]
        ym = xm * sin + ym * cos + startPoints[1]
        xm = x
        x = xn * cos - yn * sin + startPoints[0]
        yn = xn * sin + yn * cos + startPoints[1]
        xn = x
        points = [(endPoints[0], endPoints[1]), (int(xm), int(ym)), (int(xn), int(yn))]
        # draw polygon
        pygame.draw.polygon(self.screen, white, points)

    def drawMenu(self):
        graph = self.graphAlgo.graph
        menu = pygame_menu.Menu('Options', 450, 300, theme=pygame_menu.themes.THEME_ORANGE)
        menu.add.button(f'Number of Vertices: {graph.v_size()}', None)
        menu.add.button(f'Number of Edges: {graph.e_size()}', None)
        menu.add.button('Add Edge', self.addEdge)
        menu.add.button('Exit', menu.disable)
        return menu

    def display(self):
        graphButton = Button(4, 4, 40, 40, 'Options ')
        done = False
        # Run until the user asks to quit
        while not done:
            subX = abs(self.maxX - self.minX)
            subY = abs(self.maxY - self.minY)
            self.posX = (self.screen.get_width() / subX * 0.85)
            self.posY = (self.screen.get_height() / subY * 0.85)
            self.screen.fill(black)
            for event in pygame.event.get():
                # if the user clicked the close button-> done
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if graphButton.onCube(pygame.mouse.get_pos()):
                        algoMenu = self.drawMenu()
                        algoMenu.mainloop(self.screen)
            # draw buttons, vertices and edges
            graphButton.drawButton(self.screen, white)
            self.drawEdges()
            self.drawVertex()
            # Flip the display
            pygame.display.flip()
        # Done
        pygame.quit()


class Button:
    def _init_(self, x, y, width, height, text=''):
        self.color = yellow
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def drawButton(self, screen, line=None):
        # draw button on the screen
        pygame.draw.rect(screen, yellow, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('david', 10)
            text = font.render(self.text, 1, black)
            subWidth = self.width / 2 - text.get_width() / 2
            subHeight = self.height / 2 - text.get_height() / 2
            screen.blit(text, (self.x + subWidth-3, self.y + subHeight))

    def onCube(self, pos):
        # Pos = mouse position on the screen
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False