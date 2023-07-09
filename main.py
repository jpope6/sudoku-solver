import pygame as pg
import sys
from board import Board

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Game:
    def __init__(self):
        pg.init()
        self.width = 700
        self.height = 700
        self.screen = pg.display.set_mode((self.width, self.height))
        self.board = Board(self)
        self.surface = pg.Surface((self.board.size, self.board.size))

    def play(self):
        while True:
            self.surface.fill(WHITE)
            self.board.draw()
            self.screen.fill((50, 50, 50))
            self.screen.blit(
                self.surface, (self.board.board_offset, self.board.board_offset)
            )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            pg.display.update()


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
