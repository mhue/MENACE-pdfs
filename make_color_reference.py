from colors import COLOR_NAMES

preamb = r"""\documentclass{article}
\usepackage{tikz}
\usepackage[a4paper,margin=1.5cm]{geometry}
\begin{document}
\begin{center}
\begin{tikzpicture}[x=1mm, y=1mm]
"""
postamb = r"""\end{tikzpicture}
\end{center}
\end{document}
"""

# Grid parameters for nearly full A4 width (about 180mm)
cell_size = 56  # mm (3*56=168mm grid, plus margin)
margin = 10     # mm
num_cells = 3

grid_size = cell_size * num_cells

color_latex = preamb
# Draw grid lines (2 horizontal, 2 vertical) with thick lines
for i in range(1, num_cells):
    # Horizontal lines
    y = margin + i * cell_size
    color_latex += f'  \\draw[gray, line width=2mm] ({margin}mm,{y}mm) -- ({margin+grid_size}mm,{y}mm);\n'
    # Vertical lines
    x = margin + i * cell_size
    color_latex += f'  \\draw[gray, line width=2mm] ({x}mm,{margin}mm) -- ({x}mm,{margin+grid_size}mm);\n'
# Draw colored circles
positions = [
    (0, 0), (1, 0), (2, 0),
    (0, 1), (1, 1), (2, 1),
    (0, 2), (1, 2), (2, 2)
]
for i, color in enumerate(COLOR_NAMES):
    x, y = positions[i]
    cx = margin + x * cell_size + cell_size // 2
    cy = margin + y * cell_size + cell_size // 2
    color_latex += f'  \\fill[{color}] ({cx}mm, {cy}mm) circle (18mm);'
    color_latex += f'  \\draw[black, line width=1.5mm] ({cx}mm, {cy}mm) circle (18mm);'
color_latex += postamb

with open('output/colors_reference.tex', 'w') as f:
    f.write(color_latex)

import os
os.system('pdflatex -output-directory output output/colors_reference.tex') 