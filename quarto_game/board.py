import cpp_bots.cpp_adapter as cppA
from .piece import Piece


class Board:
    # creates board filled with empty pieces
    def __init__(self):
        self._board = [[Piece(None) for tile in range(4)] for row in range(4)]

    def has_empty_tiles(self):
        for row in self._board:
            for tile in row:
                if tile.is_idle():
                    return True
        return False

    # user inputs row and col values in [1-4] format
    def is_avaliable(self, row, col):
        return self._board[row - 1][col - 1].is_idle()

    def place(self, piece, row, col):
        self._board[row - 1][col - 1] = piece

    # returns True if achieved Quarto, False otherwise
    def is_quarto(self):
        out = cppA.execute_cpp("cpp_bots/bin/is_quarto", self.format())
        if out == "1":
            return True
        else:
            return False

    # returns board in string format as one line for cpp
    def format(self):
        hex_string = ""
        for row in self._board:
            for piece in row:
                if piece.decimal() == -1:
                    hex_string += 'p'
                else:
                    hex_string += hex(piece.decimal())[2:].upper()

        return hex_string

    def __str__(self):
        readable_board = "#|11111|22222|33333|44444|\n"
        readable_board += "#|-----|-----|-----|-----|\n"

        for m in range(4):
            readable_row = f"{m + 1}|"
            for n in range(4):
                piece = self._board[m][n]
                if piece.is_idle():
                    readable_row += "     |"
                else:
                    piece_symbolic = piece.symbolic()
                    readable_row += f" {piece_symbolic[0]} {piece_symbolic[1]} |"
            readable_row += "\n"
            readable_row += f"{m + 1}|"
            for n in range(4):
                piece = self._board[m][n]
                if piece.is_idle():
                    readable_row += "     |"
                else:
                    piece_symbolic = piece.symbolic()
                    readable_row += f" {piece_symbolic[2]} {piece_symbolic[3]} |"
            readable_row += "\n"
            readable_row += "#|-----|-----|-----|-----|\n"
            readable_board += readable_row

        return readable_board
