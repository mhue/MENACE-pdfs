from make_pdfs import positions
from menace import COLOR_NAMES

cell_counts = [0] * 9
for boards in positions:
    for board in boards:
        for move in board.best_moves_for_o():
            cell_counts[move] += 1

rows = [[6, 7, 8], [3, 4, 5], [0, 1, 2]]

import os
os.makedirs("output", exist_ok=True)

# Determine the max width for each column (color name + count)
col_widths = []
for col in range(3):
    max_width = 0
    for row in rows:
        i = row[col]
        entry = f'{COLOR_NAMES[i]}: {cell_counts[i]}'
        if len(entry) > max_width:
            max_width = len(entry)
    col_widths.append(max_width)

with open("output/bead_counts.txt", "w") as f:
    for row in rows:
        line = ' | '.join(f'{COLOR_NAMES[i]}: {cell_counts[i]:<}'
                          .ljust(col_widths[j]) for j, i in enumerate(row))
        f.write(line + "\n") 