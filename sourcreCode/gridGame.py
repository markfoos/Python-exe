#class based tile map games
import pygame as pg
import random
import sys
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        pass


    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player(self, 0, 0)
        for x in range(10, 20):
            Wall(self, x, 5)


    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def update(self):
        # NOTE: Game loop update
        self.all_sprites.update()

    def events(self):
        # Game loop - events
        for event in pg.event.get():
            #check for closing window
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def draw_grid(self):
        for x in range(0, width, tilesize):
            pg.draw.line(self.screen, lightgrey, (x, 0), (x, height))
        for y in range(0, height, tilesize):
            pg.draw.line(self.screen, lightgrey, (0, y), (width, y))

    def draw(self):
        #game loop - drawing
        self.screen.fill(black)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()


    def show_start_screen(self):
        # shows start screen
        pass

    def show_go_screen(self):
        # shows game over screen
        pass


g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
