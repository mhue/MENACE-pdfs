from itertools import permutations
from menace import Board

def get_positions_first_player():
    positions = [[Board()], [], [], []]

    for o1, x1 in permutations(range(9), 2):
        board = Board()
        board[o1] = 1
        board[x1] = 2
        if board.is_max() and not board.in_set(positions[1]):
            positions[1].append(board)

    for o1, x1, o2, x2 in permutations(range(9), 4):
        board = Board()
        board[o1] = 1
        board[x1] = 2
        board[o2] = 1
        board[x2] = 2
        if board.is_max() and not board.in_set(positions[2]):
            positions[2].append(board)

    for o1, x1, o2, x2, o3, x3 in permutations(range(9), 6):
        board = Board()
        board[o1] = 1
        board[x1] = 2
        board[o2] = 1
        board[x2] = 2
        board[o3] = 1
        board[x3] = 2
        if board.has_winner():
            continue
        if board.is_max() and not board.in_set(positions[3]):
            positions[3].append(board)

    assert len(positions[0]) == 1
    assert len(positions[1]) == 12
    assert sum([len(p) for p in positions]) == 304
    return positions

def get_positions_second_player():
    positions = [[], [], [], []]

    for o1 in range(9):
        board = Board()
        board[o1] = 1
        if board.is_max() and not board.in_set(positions[0]):
            positions[0].append(board)

    for o1, x1, o2 in permutations(range(9), 3):
        board = Board()
        board[o1] = 1
        board[x1] = 2
        board[o2] = 1
        if board.is_max() and not board.in_set(positions[1]):
            positions[1].append(board)

    for o1, x1, o2, x2, o3 in permutations(range(9), 5):
        board = Board()
        board[o1] = 1
        board[x1] = 2
        board[o2] = 1
        board[x2] = 2
        board[o3] = 1
        if board.has_winner():
            continue
        if board.is_max() and not board.in_set(positions[2]):
            positions[2].append(board)

    for o1, x1, o2, x2, o3, x3, o4 in permutations(range(9), 7):
        board = Board()
        board[o1] = 1
        board[x1] = 2
        board[o2] = 1
        board[x2] = 2
        board[o3] = 1
        board[x3] = 2
        board[o4] = 1
        if board.has_winner():
            continue
        if board.is_max() and not board.in_set(positions[3]):
            positions[3].append(board)

    assert sum([len(p) for p in positions]) == 289
    assert len(positions[0]) == 3
    assert len(positions[1]) == 38
    return positions 