from positions import (
    get_positions_first_player,
    get_positions_second_player,
)
from colors import COLOR_NAMES_FIRST, COLOR_NAMES_SECOND
import os


def compute_cell_counts(positions, best_moves_getter):
    counts = [0] * 9
    for boards in positions:
        for board in boards:
            for move in best_moves_getter(board):
                counts[move] += 1
    return counts


def format_section(title, color_names, counts):
    rows = [[6, 7, 8], [3, 4, 5], [0, 1, 2]]

    # Determine the max width for color names and counts in each column
    color_widths = []
    count_widths = []
    for col in range(3):
        max_color = 0
        max_count = 0
        for row in rows:
            i = row[col]
            color = color_names[i]
            count = str(counts[i])
            if len(color) > max_color:
                max_color = len(color)
            if len(count) > max_count:
                max_count = len(count)
        color_widths.append(max_color)
        count_widths.append(max_count)

    lines = [title]
    for row in rows:
        line = " | ".join(
            f"{color_names[i].ljust(color_widths[j])}: "
            f"{str(counts[i]).rjust(count_widths[j])}"
            for j, i in enumerate(row)
        )
        lines.append(line)
    return "\n".join(lines)


def main():
    os.makedirs("output", exist_ok=True)

    # FIRST player (o to move)
    positions_first = get_positions_first_player()
    counts_first = compute_cell_counts(positions_first,
                                       lambda b: b.best_moves_for_o())
    section_first = format_section("FIRST", COLOR_NAMES_FIRST, counts_first)

    # SECOND player (x to move)
    positions_second = get_positions_second_player()
    counts_second = compute_cell_counts(positions_second,
                                        lambda b: b.best_moves_for_x())
    section_second = format_section("SECOND", COLOR_NAMES_SECOND,
                                    counts_second)

    with open("output/bead_counts.txt", "w") as f:
        f.write(section_first + "\n\n" + section_second + "\n")


if __name__ == "__main__":
    main()
