from positions import get_positions_first_player
from menace import COLOR_NAMES
import os

positions = get_positions_first_player()
cell_counts = [0] * 9
for boards in positions:
    for board in boards:
        for move in board.best_moves_for_o():
            cell_counts[move] += 1

rows = [[6, 7, 8], [3, 4, 5], [0, 1, 2]]

os.makedirs("output", exist_ok=True)

# Determine the max width for color names and counts in each column
color_widths = []
count_widths = []
for col in range(3):
    max_color = 0
    max_count = 0
    for row in rows:
        i = row[col]
        color = COLOR_NAMES[i]
        count = str(cell_counts[i])
        if len(color) > max_color:
            max_color = len(color)
        if len(count) > max_count:
            max_count = len(count)
    color_widths.append(max_color)
    count_widths.append(max_count)

with open("output/bead_counts.txt", "w") as f:
    for row in rows:
        line = ' | '.join(
            f'{COLOR_NAMES[i].ljust(color_widths[j])}: {str(cell_counts[i]).rjust(count_widths[j])}'
            for j, i in enumerate(row)
        )
        f.write(line + "\n") 