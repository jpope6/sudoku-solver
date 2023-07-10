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
        pg.display.set_caption("Sudoku Solver")
        self.clock = pg.time.Clock()

        # Change the difficulty to get different boards here
        self.board = Board(self, difficulty="easy")

        self.surface = pg.Surface((self.board.size, self.board.size))

    def draw(self):
        self.surface.fill(WHITE)
        self.board.draw()
        self.screen.fill((50, 50, 50))
        self.screen.blit(
            self.surface, (self.board.board_offset, self.board.board_offset)
        )

    def play(self):
        self.board.solve()

        while True:
            self.draw()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            pg.display.update()
            self.clock.tick(30)


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
