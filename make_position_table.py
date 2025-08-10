from positions import get_positions_first_player
from menace import Board

positions = get_positions_first_player()

# The 8 symmetry rotations as in Board.permutations
rotations = [
    (0, 1, 2, 3, 4, 5, 6, 7, 8),
    (2, 5, 8, 1, 4, 7, 0, 3, 6),
    (8, 7, 6, 5, 4, 3, 2, 1, 0),
    (6, 3, 0, 7, 4, 1, 8, 5, 2),
    (2, 1, 0, 5, 4, 3, 8, 7, 6),
    (8, 5, 2, 7, 4, 1, 6, 3, 0),
    (6, 7, 8, 3, 4, 5, 0, 1, 2),
    (0, 3, 6, 1, 4, 7, 2, 5, 8)
]


def board_symmetries(board):
    syms = []
    for rot in rotations:
        b = Board()
        for i in range(9):
            b[i] = board[rot[i]]
        # Format as nine consecutive characters, using '.' for spaces
        syms.append(''.join([['.', 'o', 'x'][b[i]] for i in range(9)]))
    return syms

# Build mapping from every symmetry string to its index
sym_to_index = {}
index = 1
for boards in positions:
    for board in boards:
        syms = board_symmetries(board)
        for s in syms:
            sym_to_index[s] = index
        index += 1

with open('output/symmetry_to_index.txt', 'w') as f:
    for s, idx in sorted(sym_to_index.items()):
        f.write(f'"{s}",{idx}\n')

    # Check for the empty board
    empty_board_str = '.........'
    if empty_board_str in sym_to_index:
        f.write(f"Empty board is present with index {sym_to_index[empty_board_str]}\n")
    else:
        f.write("Empty board is NOT present in the mapping.\n") 