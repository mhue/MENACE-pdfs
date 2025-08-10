from positions import get_positions_first_player, get_positions_second_player
from colors import COLOR_NAMES_FIRST, COLOR_NAMES_SECOND

positions_first = get_positions_first_player()
positions_second = get_positions_second_player()

# Flatten positions into a single list, keeping track of 1-based indices
def flatten_positions(positions):
    boards = []
    for group in positions:
        boards.extend(group)
    return boards

boards_first = flatten_positions(positions_first)
boards_second = flatten_positions(positions_second)

def get_color_to_indices(boards, best_moves_func, palette):
    color_to_indices = {color: [] for color in palette}
    for idx, board in enumerate(boards, start=1):
        best_moves = best_moves_func(board)
        bead_colors = set(palette[i % len(palette)] for i in best_moves)
        for color in bead_colors:
            color_to_indices[color].append(idx)
    return color_to_indices

def matrix_lines(lst, columns=10):
    lines = []
    for i in range(0, len(lst), columns):
        lines.append(" ".join(f"{x:3}" for x in lst[i:i+columns]))
    return lines

# First player (as in make_pdfs.py)
color_to_indices_first = get_color_to_indices(boards_first, lambda b: b.best_moves_for_o(), COLOR_NAMES_FIRST)
with open("color_indices_first.txt", "w") as f:
    for color in COLOR_NAMES_FIRST:
        f.write(f"{color} ({len(color_to_indices_first[color])}):\n")
        for line in matrix_lines(color_to_indices_first[color], columns=10):
            f.write(line + "\n")
        f.write("\n")

# Second player (as in make_pdfs_second.py)
color_to_indices_second = get_color_to_indices(boards_second, lambda b: b.best_moves_for_x(), COLOR_NAMES_SECOND)
with open("color_indices_second.txt", "w") as f:
    for color in COLOR_NAMES_SECOND:
        f.write(f"{color} ({len(color_to_indices_second[color])}):\n")
        for line in matrix_lines(color_to_indices_second[color], columns=10):
            f.write(line + "\n")
        f.write("\n") 