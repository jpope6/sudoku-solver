import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


class Board:
    def __init__(self, game):
        self.game = game
        self.size = 630
        self.font = pg.font.SysFont("comicsans", 40)
        self.board_offset = (self.game.width - self.size) // 2
        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

    def draw(self):
        box_size = self.size // 9

        # draw sudoku boxes
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                x = j * box_size
                y = i * box_size
                dif = self.size // 9

                pg.draw.rect(
                    self.game.surface,
                    WHITE if self.board[i][j] == 0 else BLUE,
                    (x, y, box_size, box_size),
                )

                if self.board[i][j] != 0:
                    number = self.font.render(str(self.board[i][j]), True, BLACK)
                    text_rect = number.get_rect(
                        center=(x + box_size // 2, y + box_size // 2)
                    )
                    self.game.surface.blit(number, text_rect)

        # draw lines
        for i in range(len(self.board) + 1):
            dif = self.size // 9

            if i % 3 == 0:
                thick = 4
            else:
                thick = 1

            offset = 0

            if i == 9:
                offset = thick // 2

            pg.draw.line(
                self.game.surface,
                BLACK,
                (0, (i * dif) - offset),
                (self.size, (i * dif) - offset),
                thick,
            )
            pg.draw.line(
                self.game.surface,
                BLACK,
                ((i * dif) - offset, 0),
                ((i * dif) - offset, self.size),
                thick,
            )
