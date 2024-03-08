# Author: Zhiwei Cai
# GitHub username: zwcai0110
# Date: 11/17/2023
# Description: portfolio project that plays a chess game with slight variations

class Piece:
    '''
    parent class that represents different pieces
    '''

    def __init__(self, color, name):
        self._color = color
        self._name = name
        self._num = None

    def get_color(self):
        '''
        gets the color of the piece
        :return: color of the piece
        '''
        return self._color

    def get_name(self):
        '''
        gets the name of the piece
        :return: name of the piece
        '''
        return self._name

    def get_num(self):
        '''
        gets the number of this type/color of piece left on the board
        :return: number of the piece
        '''
        return self._num

    def update_num(self, num):
        '''
        updates the number of this type/color of piece left on the board
        :return: nothing
        '''
        self._num = num


class King(Piece):
    '''
    represents king
    '''

    def __init__(self, color, name):
        super().__init__(color, name)
        self._num = 1

    def check_legal(self, start, end, board):
        '''
        checks whether a move is legal
        :param start: start position
        :param end: end position
        :param board: current board info
        :return: whether the move is legal
        '''
        # first, convert algebraic notation to indices
        s_col, s_row = ord(start[0]) - 97, abs(int(start[1]) - 8)
        e_col, e_row = ord(end[0]) - 97, abs(int(end[1]) - 8)

        # check whether 'start' and 'end' are out of bound
        if s_col < 0 or s_row < 0 or e_col < 0 or e_row < 0:
            return False
        if s_col > 7 or s_row > 7 or e_col > 7 or e_row > 7:
            return False

        # if the endpoint is occupied
        if board[e_row][e_col].get_color() != '':
            # check if it's occupied by a piece of the same color
            if board[e_row][e_col].get_color() == board[s_row][s_col].get_color():
                # if so, return false
                return False

        # check if the move is only 1 square and within 8 legal directions
        if (e_col, e_row) == (s_col + 1, s_row + 1) or (e_col, e_row) == (s_col - 1, s_row - 1) or \
                (e_col, e_row) == (s_col + 1, s_row - 1) or (e_col, e_row) == (s_col - 1, s_row + 1) or \
                (e_col, e_row) == (s_col + 1, s_row) or (e_col, e_row) == (s_col, s_row + 1) or \
                (e_col, e_row) == (s_col - 1, s_row) or (e_col, e_row) == (s_col, s_row - 1):
            # if legal, return true
            return True
        # otherwise, return false
        return False


class Queen(Piece):
    '''
    represents queen
    '''

    def __init__(self, color, name):
        super().__init__(color, name)
        self._num = 1

    def check_legal(self, start, end, board):
        '''
        checks whether a move is legal
        :param start: start position
        :param end: end position
        :param board: current board info
        :return: whether the move is legal
        '''
        # first, convert algebraic notation to indices
        s_col, s_row = ord(start[0]) - 97, abs(int(start[1]) - 8)
        e_col, e_row = ord(end[0]) - 97, abs(int(end[1]) - 8)

        # store the color of the piece making the move
        s_color = board[s_row][s_col].get_color()
        # check whether 'start' and 'end' are out of bound
        if s_col < 0 or s_row < 0 or e_col < 0 or e_row < 0:
            return False
        if s_col > 7 or s_row > 7 or e_col > 7 or e_row > 7:
            return False
        # check when moving diagonally, whether the change in x is the same as the change in y
        if s_row != e_row and s_col != e_col and abs(s_row - e_row) != abs(s_col - e_col):
            # if not moving truly 1:1 diagonally, return false
            return False

        # check the case that the endpoint is already occupied
        if board[e_row][e_col] != '':
            # check if the piece is of the same color
            if board[e_row][e_col].get_color() == s_color:
                # if so, return false
                return False

        # scenario when queen is moving straight down
        if s_col == e_col and s_row < e_row:
            # keep moving down 1 square at a time to check if there's any piece in the way
            while s_row < e_row - 1:
                s_row += 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving straight up
        if s_col == e_col and s_row > e_row:
            # keep moving up 1 square at a time to check if there's any piece in the way
            while s_row > e_row + 1:
                s_row -= 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving straight right
        if s_row == e_row and s_col < e_col:
            # keep moving right 1 square at a time to check if there's any piece in the way
            while s_col < e_col - 1:
                s_col += 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving straight left
        if s_row == e_row and s_col > e_col:
            # keep moving left 1 square at a time to check if there's any piece in the way
            while s_col > e_col + 1:
                s_col -= 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving diagonally, down and to the left
        if s_row < e_row and s_col > e_col:
            # keep moving 1 square at a time to check if there's any piece in the way
            while s_row < e_row - 1 and s_col > e_col + 1:
                s_row += 1
                s_col -= 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving diagonally, down and to the right
        if s_row < e_row and s_col < e_col:
            # keep moving 1 square at a time to check if there's any piece in the way
            while s_row < e_row - 1 and s_col < e_col - 1:
                s_row += 1
                s_col += 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving diagonally, up and to the left
        if s_row > e_row and s_col > e_col:
            # keep moving 1 square at a time to check if there's any piece in the way
            while s_row > e_row + 1 and s_col > e_col + 1:
                s_row -= 1
                s_col -= 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving diagonally, up and to the right
        if s_row > e_row and s_col < e_col:
            # keep moving 1 square at a time to check if there's any piece in the way
            while s_row > e_row + 1 and s_col < e_col - 1:
                s_row -= 1
                s_col += 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False
        # if nothing goes wrong, return true
        return True


class Pawn(Piece):
    '''
    represents pawn
    '''

    def __init__(self, color, name):
        super().__init__(color, name)
        self._num = 8

    def check_legal(self, start, end, board):
        '''
        checks whether a move is legal
        :param start: start position
        :param end: end position
        :param board: current board info
        :return: whether the move is legal
        '''
        # first, convert algebraic notation to indices
        s_col, s_row = ord(start[0]) - 97, abs(int(start[1]) - 8)
        e_col, e_row = ord(end[0]) - 97, abs(int(end[1]) - 8)
        # store the color of the piece making the move
        s_color = board[s_row][s_col].get_color()
        # check whether 'start' and 'end' are out of bound
        if s_col < 0 or s_row < 0 or e_col < 0 or e_row < 0:
            return False
        if s_col > 7 or s_row > 7 or e_col > 7 or e_row > 7:
            return False

        # check the case that the endpoint is already occupied
        if board[e_row][e_col] != '':
            # check if the piece is of the same color
            if board[e_row][e_col].get_color() == s_color:
                # if so, return false
                return False

            # otherwise, if the piece in the endpoint is not ours, we are capturing an opponent's piece
            # when the piece we are moving is black
            if board[s_row][s_col].get_color() == 'black':
                # check if moving 1 square diagonally down and either to the left or right
                if (e_col, e_row) != (s_col + 1, s_row + 1) and (e_col, e_row) != (s_col - 1, s_row + 1):
                    # if not, return false
                    return False

            # when the piece we are moving is white
            if board[s_row][s_col].get_color() == 'white':
                # check if moving 1 square diagonally up and either to the left or right
                if (e_col, e_row) != (s_col + 1, s_row - 1) and (e_col, e_row) != (s_col - 1, s_row - 1):
                    # if not, return false
                    return False

        # if we are simply moving and not capturing
        if board[e_row][e_col] == '':
            # check if we are only moving up and down and not diagonally
            if s_col != e_col:
                # if moving side to side, return false
                return False

            # scenario where we are moving a black piece
            if board[s_row][s_col].get_color() == 'black':
                # case where this is the first move
                if s_row == 1:
                    # then check if moving no more than 2 squares, or if there's not another piece blocking
                    if e_row > s_row + 2 or board[s_row + 1][s_col] != '':
                        # return false otherwise
                        return False
                # case where this is not the first move
                else:
                    # check if only moving 1 square
                    if e_row != s_row + 1:
                        # if not, return false
                        return False

            # scenario where we are moving a white piece
            if board[s_row][s_col].get_color() == 'white':
                # case where this is the first move
                if s_row == 6:
                    # then check if moving more than 2 squares, or if there's not another piece blocking
                    if e_row < s_row - 2 or board[s_row - 1][s_col] != '':
                        # return false otherwise
                        return False
                # case where this is not the first move
                else:
                    # check if only moving 1 square
                    if e_row != s_row - 1:
                        # if not, return false
                        return False
        # if nothing goes wrong, return true
        return True


class Rook(Piece):
    '''
    represents rook
    '''

    def __init__(self, color, name):
        super().__init__(color, name)
        self._num = 2

    def check_legal(self, start, end, board):
        '''
        checks whether a move is legal
        :param start: start position
        :param end: end position
        :param board: current board info
        :return: whether the move is legal
        '''
        # first, convert algebraic notation to indices
        s_col, s_row = ord(start[0]) - 97, abs(int(start[1]) - 8)
        e_col, e_row = ord(end[0]) - 97, abs(int(end[1]) - 8)
        # store the color of the piece making the move
        s_color = board[s_row][s_col].get_color()
        # check whether 'start' and 'end' are out of bound
        if s_col < 0 or s_row < 0 or e_col < 0 or e_row < 0:
            return False
        if s_col > 7 or s_row > 7 or e_col > 7 or e_row > 7:
            return False

        # check if moving diagonally, which is illegal for rook
        if s_col != e_col and s_row != e_row:
            # if so, return false
            return False

        # check the case that the endpoint is already occupied
        if board[e_row][e_col] != '':
            # check if the piece is of the same color
            if board[e_row][e_col].get_color() == s_color:
                # if so, return false
                return False

        # scenario when queen is moving straight down
        if s_col == e_col and s_row < e_row:
            # keep moving 1 square at a time to check if there's any piece in the way
            while s_row < e_row - 1:
                s_row += 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving straight up
        if s_col == e_col and s_row > e_row:
            # keep moving 1 square at a time to check if there's any piece in the way
            while s_row > e_row + 1:
                s_row -= 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving straight right
        if s_row == e_row and s_col < e_col:
            # keep moving 1 square at a time to check if there's any piece in the way
            while s_col < e_col - 1:
                s_col += 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving straight left
        if s_row == e_row and s_col > e_col:
            # keep moving 1 square at a time to check if there's any piece in the way
            while s_col > e_col + 1:
                s_col -= 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False
        # if nothing goes wrong, return true
        return True


class Bishop(Piece):
    '''
    represents bishop
    '''

    def __init__(self, color, name):
        super().__init__(color, name)
        self._num = 2

    def check_legal(self, start, end, board):
        '''
        checks whether a move is legal
        :param start: start position
        :param end: end position
        :param board: current board info
        :return: whether the move is legal
        '''
        # first, convert algebraic notation to indices
        s_col, s_row = ord(start[0]) - 97, abs(int(start[1]) - 8)
        e_col, e_row = ord(end[0]) - 97, abs(int(end[1]) - 8)
        # store the color of the piece making the move
        s_color = board[s_row][s_col].get_color()
        # check whether 'start' and 'end' are out of bound
        if s_col < 0 or s_row < 0 or e_col < 0 or e_row < 0:
            return False
        if s_col > 7 or s_row > 7 or e_col > 7 or e_row > 7:
            return False
        # check whether moving purely diagonally, since bishop cannot move any other way
        if s_col == e_col or s_row == e_row or abs(s_row - e_row) != abs(s_col - e_col):
            # if not moving diagonally or change in x and y not equal, return false
            return False

        # check the case that the endpoint is already occupied
        if board[e_row][e_col] != '':
            # check if the piece is of the same color
            if board[e_row][e_col].get_color() == s_color:
                # if so, return false
                return False

        # scenario when queen is moving diagonally, down and to the left
        if s_row < e_row and s_col > e_col:
            # keep moving 1 square at a time to check if there's any piece in the way
            while s_row < e_row - 1 and s_col > e_col + 1:
                s_row += 1
                s_col -= 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving diagonally, down and to the right
        if s_row < e_row and s_col < e_col:
            # keep moving 1 square at a time to check if there's any piece in the way
            while s_row < e_row - 1 and s_col < e_col - 1:
                s_row += 1
                s_col += 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving diagonally, up and to the left
        if s_row > e_row and s_col > e_col:
            # keep moving 1 square at a time to check if there's any piece in the way
            while s_row > e_row + 1 and s_col > e_col + 1:
                s_row -= 1
                s_col -= 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False

        # scenario when queen is moving diagonally, up and to the right
        if s_row > e_row and s_col < e_col:
            # keep moving 1 square at a time to check if there's any piece in the way
            while s_row > e_row + 1 and s_col < e_col - 1:
                s_row -= 1
                s_col += 1
                # if there's a piece blocking the path, return false
                if board[s_row][s_col] != '':
                    return False
        # if nothing goes wrong, return true
        return True


class Knight(Piece):
    '''
    represents knight
    '''

    def __init__(self, color, name):
        super().__init__(color, name)
        self._num = 2

    def check_legal(self, start, end, board):
        '''
        checks whether a move is legal
        :param start: start position
        :param end: end position
        :param board: current board info
        :return: whether the move is legal
        '''
        # first, convert algebraic notation to indices
        s_col, s_row = ord(start[0]) - 97, abs(int(start[1]) - 8)
        e_col, e_row = ord(end[0]) - 97, abs(int(end[1]) - 8)
        # store the color of the piece making the move
        s_color = board[s_row][s_col].get_color()
        # check whether 'start' and 'end' are out of bound
        if s_col < 0 or s_row < 0 or e_col < 0 or e_row < 0:
            return False
        if s_col > 7 or s_row > 7 or e_col > 7 or e_row > 7:
            return False

        # check the case that the endpoint is already occupied
        if board[e_row][e_col] != '':
            # check if the piece is of the same color
            if board[e_row][e_col].get_color() == s_color:
                # if so, return false
                return False

        # check if the move is only 1 square and within 8 legal directions
        if (e_col, e_row) == (s_col + 2, s_row + 1) or (e_col, e_row) == (s_col - 2, s_row - 1) or \
                (e_col, e_row) == (s_col + 2, s_row - 1) or (e_col, e_row) == (s_col - 2, s_row + 1) or \
                (e_col, e_row) == (s_col + 1, s_row - 2) or (e_col, e_row) == (s_col + 1, s_row + 2) or \
                (e_col, e_row) == (s_col - 1, s_row - 2) or (e_col, e_row) == (s_col - 1, s_row + 2):
            return True
        # otherwise, return false
        return False


class ChessVar:
    '''
    main class that represents the game
    '''

    def __init__(self):
        self._R = Rook('black', 'R')
        self._N = Knight('black', 'N')
        self._B = Bishop('black', 'B')
        self._Q = Queen('black', 'Q')
        self._K = King('black', 'K')
        self._P = Pawn('black', 'P')

        self._r = Rook('white', 'r')
        self._n = Knight('white', 'n')
        self._b = Bishop('white', 'b')
        self._q = Queen('white', 'q')
        self._k = King('white', 'k')
        self._p = Pawn('white', 'p')

        self._turn = 0
        self._state = 'UNFINISHED'

        self._board = [
            [self._R, self._N, self._B, self._Q, self._K, self._B, self._N, self._R],
            [self._P] * 8,
            [''] * 8,
            [''] * 8,
            [''] * 8,
            [''] * 8,
            [self._p] * 8,
            [self._r, self._n, self._b, self._q, self._k, self._b, self._n, self._r]
        ]

    def print_board(self):
        '''
        prints the current board configuration
        :return: nothing
        '''
        # initialize the column labels
        col_labels = '   a  b  c  d  e  f  g  h  '
        print(col_labels)  # print the labels for the first line
        for i, row in enumerate(self._board):
            row_num = str(8 - i)  # get current row number
            row_string = ' '.join([' ' + (piece.get_name() if piece != '' else '.') for piece in row])
            print(f"{row_num} {row_string} {row_num}")  # formatting
        print(col_labels)  # print the labels for the last line

    def get_game_state(self):
        '''
        gets the current game state
        :return: current game state
        '''
        return self._state

    def make_move(self, start, end):
        '''
        moves the piece in "start" to "end"; relies on get_color() from the Piece class to determine the color of
        the pieces, both to determine who's turn it is and whowon the game; relies on check_legal() from all classes
        representing different type of pieces to determine if the proposed move is valid; depends on get_num() and
        update_num() from the Piece class to keep track of the number of pieces left on the board.
        :param start: the square we are starting with
        :param end: the square we are moving the piece into
        :return: false if the move is invalid, true if otherwise
        '''
        # first, convert algebraic notation to indices
        s_col, s_row = ord(start[0]) - 97, abs(int(start[1]) - 8)
        e_col, e_row = ord(end[0]) - 97, abs(int(end[1]) - 8)
        # get info for the square we are starting with and moving into
        s = self._board[s_row][s_col]
        e = self._board[e_row][e_col]

        # get current board
        board = self._board

        # check whose turn it is. Use remainder to alternate between black and white, then increment by 1 at the end
        if self._turn % 2 == 0:
            turn = 'white'
        else:
            turn = 'black'

        # check if it's not the current color's turn to move or if the game has finished
        if s == '' or s.get_color() != turn or self._state != 'UNFINISHED':
            # if so, return false
            print('false')
            return False

        # check whether the move is legal for the type of piece we are moving
        if_valid = s.check_legal(start, end, self._board)
        # return false if the move is not legal
        if if_valid is False:
            print('false')
            return False

        # otherwise, the move is legal, and we move the piece from start to end
        board[s_row][s_col] = ''
        board[e_row][e_col] = s

        # in case of capturing
        if e != '':
            e.update_num(e.get_num() - 1)
            if e.get_num() == 0:
                if s.get_color() == 'white':
                    self._state = 'WHITE_WON'
                else:
                    self._state = 'BLACK_WON'
        # update the turn counter to alternate between black and white each turn
        self._turn += 1

        # if nothing goes wrong, return true
        return True

