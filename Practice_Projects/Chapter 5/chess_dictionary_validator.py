# Chess Dictionary Validator Page 127 Chapter 5
def isValidChessBoard(board):
    # Initialize counts for white and black kings
    white_kings = 0
    black_kings = 0

    # Initialize counts for total pieces for each player
    white_pieces = 0
    black_pieces = 0

    # Initialize counts for pawns for each player
    white_pawns = 0
    black_pawns = 0

    # Define valid chess board coordinates
    valid_coordinates = set('12345678')  # Rows
    valid_coordinates.update('abcdefgh')  # Columns

    # Define valid chess piece names
    valid_pieces = {'wpawn', 'bpawn', 'wknight', 'bknight', 'wbishop', 'bbishop', 'wrook', 'brook', 'wqueen', 'bqueen', 'wking', 'bking'}

    for position, piece in board.items():
        # Check if the piece name is valid
        if piece not in valid_pieces:
            return False

        # Check if the position is valid
        if position[0] not in valid_coordinates or position[1] not in valid_coordinates:
            return False

        # Count the number of kings for each player
        if piece == 'wking':
            white_kings += 1
        elif piece == 'bking':
            black_kings += 1

        # Count the total number of pieces for each player
        if piece.startswith('w'):
            white_pieces += 1
        elif piece.startswith('b'):
            black_pieces += 1

        # Count the number of pawns for each player
        if piece == 'wpawn':
            white_pawns += 1
        elif piece == 'bpawn':
            black_pawns += 1

    # Check if there is exactly one white king and one black king
    if white_kings != 1 or black_kings != 1:
        return False

    # Check if the total number of pieces for each player is at most 16
    if white_pieces > 16 or black_pieces > 16:
        return False

    # Check if the total number of pawns for each player is at most 8
    if white_pawns > 8 or black_pawns > 8:
        return False

    return True

# Example usage:
chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(chess_board))  # Should return True

# Valid board: Exactly one white king and one black king, all pieces on valid spaces, and valid piece names.
board1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
# Output should be True
print(isValidChessBoard(board1))

# Invalid board: Two white kings.
board2 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '7f': 'wking'}
# Output should be False
print(isValidChessBoard(board2))

# Valid board: Maximum number of pieces (16) for each player, including pawns.
board3 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking',
          '8a': 'bpawn', '7b': 'bpawn', '2g': 'bpawn', '4d': 'bpawn', '5e': 'bpawn', '8f': 'bpawn',
          '1a': 'wpawn', '7c': 'wpawn', '3g': 'wpawn', '4e': 'wpawn', '5d': 'wpawn', '8h': 'wpawn'}
# Output should be True
print(isValidChessBoard(board3))

# Invalid board: A piece is on an invalid space ('9z').
board4 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '9z': 'wpawn'}
# Output should be False
print(isValidChessBoard(board4))
