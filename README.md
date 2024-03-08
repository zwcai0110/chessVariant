A class named **ChessVar** for playing an abstract board game that is a variant of chess. 

The starting position for the game is the normal starting position for standard chess.

As in standard chess, white moves first. **The winner is the first player to capture all of an opponent's pieces of one type**, for example capturing all of the opponent's knights (of which there are two) would win the game, or all of the opponent's pawns (of which there are eight), or all of the opponent's kings (of which there is only one), etc. The king isn't a special piece in this game - there is no check or checkmate. Pieces move and capture the same as in standard chess, except that there is no castling, en passant, or pawn promotion. As in standard chess, each pawn should be able to move two spaces forward on its first move (but not on subsequent moves).

Locations on the board will be specified using "algebraic notation", with columns labeled a-h and rows labeled 1-8.

* An **init method** that initializes any data members
* A method called **get_game_state** that just returns 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'.
* A method called **make_move** that takes two parameters - strings that represent the square moved from and the square moved to.  For example, make_move('b3', 'c4').  If the square being moved from does not contain a piece belonging to the player whose turn it is, or if the indicated move is not legal, or if the game has already been won, then it should **just return False**.  Otherwise it should make the indicated move, remove any captured piece, update the game state if necessary, update whose turn it is, and return True.

