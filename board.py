import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# easy
# [
# [7, 9, 5, 2, 8, 0, 0, 0, 1],
# [0, 0, 0, 9, 5, 4, 0, 8, 7],
# [0, 0, 4, 3, 7, 0, 5, 0, 0],
# [0, 0, 0, 8, 9, 2, 0, 5, 0],
# [5, 1, 2, 0, 0, 0, 0, 0, 9],
# [3, 0, 0, 0, 0, 7, 4, 0, 0],
# [0, 0, 1, 0, 3, 8, 0, 2, 0],
# [6, 3, 0, 0, 0, 9, 7, 0, 0],
# [0, 4, 0, 0, 0, 5, 9, 3, 0],
# ]

# medium
# [0, 0, 0, 0, 0, 0, 0, 0, 1],
# [0, 0, 8, 0, 0, 0, 0, 0, 5],
# [9, 0, 0, 6, 0, 5, 3, 7, 0],
# [0, 0, 0, 0, 2, 6, 0, 4, 0],
# [5, 0, 0, 0, 0, 9, 0, 0, 0],
# [3, 0, 0, 0, 0, 0, 0, 0, 0],
# [7, 0, 5, 0, 0, 0, 2, 0, 0],
# [0, 0, 4, 8, 0, 0, 0, 0, 6],
# [0, 1, 9, 7, 0, 0, 0, 0, 0],


class Board:
    def __init__(self, game, difficulty="easy"):
        self.game = game
        self.size = 630
        self.font = pg.font.SysFont("comicsans", 40)
        self.board_offset = (self.game.width - self.size) // 2

        if difficulty == "easy":
            self.board = [
                [7, 9, 5, 2, 8, 0, 0, 0, 1],
                [0, 0, 0, 9, 5, 4, 0, 8, 7],
                [0, 0, 4, 3, 7, 0, 5, 0, 0],
                [0, 0, 0, 8, 9, 2, 0, 5, 0],
                [5, 1, 2, 0, 0, 0, 0, 0, 9],
                [3, 0, 0, 0, 0, 7, 4, 0, 0],
                [0, 0, 1, 0, 3, 8, 0, 2, 0],
                [6, 3, 0, 0, 0, 9, 7, 0, 0],
                [0, 4, 0, 0, 0, 5, 9, 3, 0],
            ]
            self.delay = 100
        elif difficulty == "medium":
            self.board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 8, 0, 0, 0, 0, 0, 5],
                [9, 0, 0, 6, 0, 5, 3, 7, 0],
                [0, 0, 0, 0, 2, 6, 0, 4, 0],
                [5, 0, 0, 0, 0, 9, 0, 0, 0],
                [3, 0, 0, 0, 0, 0, 0, 0, 0],
                [7, 0, 5, 0, 0, 0, 2, 0, 0],
                [0, 0, 4, 8, 0, 0, 0, 0, 6],
                [0, 1, 9, 7, 0, 0, 0, 0, 0],
            ]
            # with any delay, it takes a while to solve
            self.delay = 0

    # check if the number can be places in the row, col, or box
    def valid_number(self, row, col, num):
        for i in range(len(self.board)):
            if self.board[row][i] == num:
                return False

            if self.board[i][col] == num:
                return False

        box_row = row // 3
        box_col = col // 3

        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def solve(self):
        # loop through every row and col
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    # try every number from 1 to 9
                    for num in range(1, 10):
                        if self.valid_number(i, j, num):
                            # if the number is valid, place it in the board
                            self.board[i][j] = num

                            # draw the board
                            self.game.draw()
                            pg.display.update()
                            pg.time.delay(self.delay)

                            # recursively call solve
                            if self.solve():
                                return True

                            # if solve returns false, reset the number
                            self.board[i][j] = 0

                            # draw the board
                            self.game.draw()
                            pg.display.update()
                            pg.time.delay(self.delay)

                    return False

        return True

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
