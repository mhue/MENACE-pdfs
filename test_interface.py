#!/usr/bin/env python3
"""
Test script to verify that the MENACE interface works with known positions.
"""

from generate_position_data import (generate_first_player_mappings,
                                    generate_second_player_mappings)


def test_known_positions():
    """Test some known positions to verify interface will work correctly."""

    # Load the generated data by importing the Python data directly
    # This is more reliable than parsing the JavaScript
    first_player_mappings = generate_first_player_mappings()
    second_player_mappings = generate_second_player_mappings()

    print("Testing MENACE Interface Position Mappings")
    print("=" * 50)

    # Test 1: Empty board (machine plays first)
    empty_board = '.........'
    if empty_board in first_player_mappings:
        print(f"✓ Empty board (machine first): {empty_board} -> "
              f"Box {first_player_mappings[empty_board]}")
    else:
        print("✗ Empty board not found in first player mappings")

    # Test 2: Single O move (machine plays second)
    single_o = '........o'
    if single_o in second_player_mappings:
        print(f"✓ Single O move: {single_o} -> "
              f"Box {second_player_mappings[single_o]}")
    else:
        print("✗ Single O move not found in second player mappings")

    # Test 3: Check a few random positions from each set
    print("\nFirst Player Mappings Sample (Machine plays O):")
    for i, (pos, box) in enumerate(list(first_player_mappings.items())[:5]):
        print(f"  {pos} -> Box {box}")

    print("\nSecond Player Mappings Sample (Machine plays X):")
    for i, (pos, box) in enumerate(list(second_player_mappings.items())[:5]):
        print(f"  {pos} -> Box {box}")

    print("\nTotal positions:")
    print(f"  First player (machine O): {len(first_player_mappings)}")
    print(f"  Second player (machine X): {len(second_player_mappings)}")

    # Test 4: Verify some positions make sense
    print("\nPosition Analysis:")

    # Count positions by number of moves
    first_by_moves = {}
    second_by_moves = {}

    for pos in first_player_mappings:
        move_count = pos.count('o') + pos.count('x')
        first_by_moves[move_count] = first_by_moves.get(move_count, 0) + 1

    for pos in second_player_mappings:
        move_count = pos.count('o') + pos.count('x')
        second_by_moves[move_count] = second_by_moves.get(move_count, 0) + 1

    print("First player positions by move count:")
    for moves in sorted(first_by_moves.keys()):
        print(f"  {moves} moves: {first_by_moves[moves]} positions")

    print("Second player positions by move count:")
    for moves in sorted(second_by_moves.keys()):
        print(f"  {moves} moves: {second_by_moves[moves]} positions")


if __name__ == "__main__":
    test_known_positions()
