# MENACE Box Number Interface

This directory contains an interactive web interface to help determine MENACE box numbers for any tic-tac-toe configuration.

## Files

- `menace_box_interface.html` - The main interactive interface
- `menace_positions.js` - Position mappings data (auto-generated)
- `generate_position_data.py` - Script to generate position data
- `test_interface.py` - Test script to verify mappings
- `position_summary.txt` - Human-readable summary of positions

## How to Use

1. **Generate the position data** (if not already done):
   ```bash
   python3 generate_position_data.py
   ```

2. **Open the interface**:
   - Open `menace_box_interface.html` in your web browser
   - Or use: `open menace_box_interface.html`

3. **Using the interface**:
   - Choose whether the machine plays first (O) or second (X)
   - Click on the board to place moves alternately
   - Box numbers are shown only when it's the machine's turn
   - Use "Reset Board" to start over

## How It Works

The interface uses the same position generation logic as the main MENACE system:

- **Machine plays first**: Uses positions from `get_positions_first_player()`
- **Machine plays second**: Uses positions from `get_positions_second_player()`

Box numbers are calculated by:
1. Converting the board state to a string (`.` = empty, `o` = O, `x` = X)
2. Checking all 8 symmetries (rotations and reflections)
3. Looking up the canonical position in the pre-generated mappings

## Key Features

- **Real-time box lookup**: Shows box numbers as you play
- **Dual mode support**: Works for both first and second player scenarios
- **Symmetry handling**: Automatically finds the canonical representation
- **Visual feedback**: Clear indication of whose turn it is
- **Complete position coverage**: Includes all 2,201 first-player and 2,097 second-player positions

## Understanding Box Numbers

- Box numbers are only shown when it's the machine's turn to play
- Each unique game position (considering symmetries) has one box number
- The machine would use these boxes to store colored beads for learning
- Empty positions or human turns don't have box numbers

## Technical Details

The interface loads position mappings from `menace_positions.js`, which contains:
- 2,201 positions for machine-first scenarios
- 2,097 positions for machine-second scenarios
- All positions include their symmetric equivalents

The position strings use the format:
- Position 0 = top-left, Position 8 = bottom-right
- Reading order: left-to-right, top-to-bottom
- Example: `"o.x......"` = O at top-left, X at top-middle
