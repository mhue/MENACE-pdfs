#!/usr/bin/env python3
"""
Generate JavaScript data file with MENACE position mappings for the web interface.
"""

import json
from positions import get_positions_first_player, get_positions_second_player
from menace import Board

# Board rotations for symmetry checking (same as in MENACE code)
rotations = [
    (0, 1, 2, 3, 4, 5, 6, 7, 8),  # identity
    (2, 5, 8, 1, 4, 7, 0, 3, 6),  # 90° clockwise
    (8, 7, 6, 5, 4, 3, 2, 1, 0),  # 180°
    (6, 3, 0, 7, 4, 1, 8, 5, 2),  # 270° clockwise
    (2, 1, 0, 5, 4, 3, 8, 7, 6),  # horizontal flip
    (8, 5, 2, 7, 4, 1, 6, 3, 0),  # vertical flip
    (6, 7, 8, 3, 4, 5, 0, 1, 2),  # diagonal flip 1
    (0, 3, 6, 1, 4, 7, 2, 5, 8)   # diagonal flip 2
]

def board_symmetries(board):
    """Generate all symmetries of a board state as strings."""
    syms = []
    for rot in rotations:
        b = Board()
        for i in range(9):
            b[i] = board[rot[i]]
        # Format as nine consecutive characters, using '.' for spaces
        syms.append(''.join(['.', 'o', 'x'][b[i]] for i in range(9)))
    return syms

def generate_first_player_mappings():
    """Generate position mappings for machine playing first (O)."""
    positions = get_positions_first_player()
    mappings = {}
    
    index = 1
    for boards in positions:
        for board in boards:
            syms = board_symmetries(board)
            for s in syms:
                mappings[s] = index
            index += 1
    
    return mappings

def generate_second_player_mappings():
    """Generate position mappings for machine playing second (X)."""
    positions = get_positions_second_player()
    mappings = {}
    
    index = 1
    for boards in positions:
        for board in boards:
            syms = board_symmetries(board)
            for s in syms:
                mappings[s] = index
            index += 1
    
    return mappings

def main():
    print("Generating MENACE position mappings...")
    
    # Generate mappings for both scenarios
    first_player_mappings = generate_first_player_mappings()
    second_player_mappings = generate_second_player_mappings()
    
    # Create JavaScript data
    js_content = f"""// MENACE Position Mappings
// Auto-generated from Python positions data

const MENACE_POSITIONS = {{
    first_player: {json.dumps(first_player_mappings, indent=2)},
    second_player: {json.dumps(second_player_mappings, indent=2)}
}};

// Export for use in HTML interface
if (typeof module !== 'undefined' && module.exports) {{
    module.exports = MENACE_POSITIONS;
}}
"""
    
    # Write to JavaScript file
    with open('menace_positions.js', 'w') as f:
        f.write(js_content)
    
    print(f"Generated mappings:")
    print(f"  First player (machine O): {len(first_player_mappings)} positions")
    print(f"  Second player (machine X): {len(second_player_mappings)} positions")
    print(f"Data written to: menace_positions.js")
    
    # Also create a simple text summary for verification
    with open('position_summary.txt', 'w') as f:
        f.write("MENACE Position Summary\n")
        f.write("======================\n\n")
        
        f.write("First Player (Machine plays O):\n")
        f.write(f"Total positions: {len(first_player_mappings)}\n")
        f.write("Sample positions:\n")
        for i, (pos, idx) in enumerate(sorted(first_player_mappings.items())[:10]):
            f.write(f"  {pos} -> Box {idx}\n")
        f.write("\n")
        
        f.write("Second Player (Machine plays X):\n")
        f.write(f"Total positions: {len(second_player_mappings)}\n")
        f.write("Sample positions:\n")
        for i, (pos, idx) in enumerate(sorted(second_player_mappings.items())[:10]):
            f.write(f"  {pos} -> Box {idx}\n")
    
    print("Summary written to: position_summary.txt")

if __name__ == "__main__":
    main()
