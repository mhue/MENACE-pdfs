import os
from latex import preamb, postamb
from positions import get_positions_second_player

positions = get_positions_second_player()

# Generate original PDFs
index = 1
for i, boards in enumerate(positions):
    latex = preamb
    for j, board in enumerate(boards):
        latex += board.as_latex(index=index)
        latex += "\n"
        if (j + 1) % 5 == 0:
            latex += "\n\\noindent"
        index += 1
    latex += postamb
    with open(f"output/second_boxes{i}.tex", "w") as f:
        f.write(latex)
    assert os.system(
        f"pdflatex -output-directory output output/second_boxes{i}.tex") == 0

# Generate PDFs with best moves highlighted
index = 1
for i, boards in enumerate(positions):
    latex = preamb
    for j, board in enumerate(boards):
        best_moves = board.best_moves_for_x()
        latex += board.as_latex(index=index, best_moves=best_moves)
        latex += "\n"
        if (j + 1) % 5 == 0:
            latex += "\n\\noindent"
        index += 1
    latex += postamb
    with open(f"output/second_boxes_best{i}.tex", "w") as f:
        f.write(latex)
    assert os.system(
        f"pdflatex -output-directory output output/second_boxes_best{i}.tex") == 0
