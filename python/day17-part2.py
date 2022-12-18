"""
--- Day 17: Pyroclastic Flow ---

Your handheld device has located an alternative exit from the cave for you and
the elephants. The ground is rumbling almost continuously now, but the strange
valves bought you some time. It's definitely getting warmer in here, though.

The tunnels eventually open into a very tall, narrow chamber. Large,
oddly-shaped rocks are falling into the chamber from above, presumably due to
all the rumbling. If you can't work out where the rocks will fall next, you
might be crushed!

The five types of rocks have the following peculiar shapes, where # is rock and
. is empty space:

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

The rocks fall in the order shown above: first the - shape, then the + shape,
and so on. Once the end of the list is reached, the same order repeats: the -
shape falls first, sixth, 11th, 16th, etc.

The rocks don't spin, but they do get pushed around by jets of hot gas coming
out of the walls themselves. A quick scan reveals the effect the jets of hot
gas will have on the rocks as they fall (your puzzle input).

For example, suppose this was the jet pattern in your cave:

>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>

In jet patterns, < means a push to the left, while > means a push to the right.
The pattern above means that the jets will push a falling rock right, then
right, then right, then left, then left, then right, and so on. If the end of
the list is reached, it repeats.

The tall, vertical chamber is exactly seven units wide. Each rock appears so
that its left edge is two units away from the left wall and its bottom edge is
three units above the highest rock in the room (or the floor, if there isn't
one).

After a rock appears, it alternates between being pushed by a jet of hot gas
one unit (in the direction indicated by the next symbol in the jet pattern) and
then falling one unit down. If any movement would cause any part of the rock to
move into the walls, floor, or a stopped rock, the movement instead does not
occur. If a downward movement would have caused a falling rock to move into the
floor or an already-fallen rock, the falling rock stops where it is (having
landed on something) and a new rock immediately begins falling.

Drawing falling rocks with @ and stopped rocks with #, the jet pattern in the
example above manifests as follows:

The first rock begins falling:
|..@@@@.|
|.......|
|.......|
|.......|
+-------+

Jet of gas pushes rock right:
|...@@@@|
|.......|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
+-------+

Jet of gas pushes rock left:
|..@@@@.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|..####.|
+-------+

A new rock begins falling:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|...@...|
|..@@@..|
|...@...|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|..####.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

A new rock begins falling:
|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

The moment each of the next few rocks begins falling, you would see this:

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|..#....|
|..#....|
|####...|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|..#....|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|.....#.|
|.....#.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|....##.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|##..##.|
|######.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

To prove to the elephants your simulation is accurate, they want to know how
tall the tower will get after 2022 rocks have stopped (but before the 2023rd
rock begins falling). In this example, the tower of rocks will be 3068 units
tall.

How many units tall will the tower of rocks be after 2022 rocks have stopped
falling?

--- Part Two ---

The elephants are not impressed by your simulation. They demand to know how tall the tower will be after 1000000000000 rocks have stopped! Only then will they feel confident enough to proceed through the cave.

In the example above, the tower would be 1514285714288 units tall!

How tall will the tower be after 1000000000000 rocks have stopped?
"""

import sys

from itertools import cycle, tee, count


PIECES = [
    # Horizontal "straight tetromino" (https://en.wikipedia.org/wiki/Tetromino)
    [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        ["#", "#", "#", "#"],
    ],
    # Plus sign
    [
        [".", ".", ".", "."],
        [".", "#", ".", "."],
        ["#", "#", "#", "."],
        [".", "#", ".", "."],
    ],
    # Corner piece
    [
        [".", ".", ".", "."],
        [".", ".", "#", "."],
        [".", ".", "#", "."],
        ["#", "#", "#", "."],
    ],
    # Vertical 'straight tetromino'
    [
        ["#", ".", ".", "."],
        ["#", ".", ".", "."],
        ["#", ".", ".", "."],
        ["#", ".", ".", "."],
    ],
    # Square
    [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        ["#", "#", ".", "."],
        ["#", "#", ".", "."],
    ],
]

CHAMBER_WIDTH = 7
SYMBOL_ROCK = "#"
SYMBOL_EMPTY = "."


class Chamber:
    def __init__(self) -> None:
        # Floor
        self.rows = [[SYMBOL_ROCK for _ in range(CHAMBER_WIDTH + 2)]]

    def tower_height(self) -> int:
        return len(self.rows) - 1

    def add_level(self):
        self.rows.append(
            [s for s in SYMBOL_ROCK + (CHAMBER_WIDTH * SYMBOL_EMPTY) + SYMBOL_ROCK]
        )

    def get(self, x: int, y: int) -> str:
        if y >= len(self.rows):
            if x == 0 or x == (CHAMBER_WIDTH + 2) - 1:
                return SYMBOL_ROCK

            return SYMBOL_EMPTY:

        return self.rows[y][x]

    def mark_blocked(self, x: int, y: int):
        for _ in range(y - self.tower_height()):
            self.add_level()

        self.rows[y][x] = SYMBOL_ROCK

    def __str__(self):
        output = []
        for row in reversed(self.rows):
            output.append("".join(row))

        return "\n".join(output)


def delta_x_for_symbol(symbol: str):
    match symbol:
        case "<":
            return -1

        case ">":
            return 1

        case _:
            raise Exception("Unknown symbol")


# jet_pattern = cycle(zip(count(), open("../puzzle-input/day17-example-input.txt").read().strip()))
jet_pattern = cycle(
    zip(count(), open("../puzzle-input/day17-input.txt").read().strip())
)

chamber = Chamber()
iter_pieces = cycle(zip(count(), PIECES))

# Because both the jet patterns (puzzle input) and pieces cycle, there will be
# a point at which there's a repeating pattern of them. This dictionary is used
# to keep track of the jet/piece combinations that have been seen.
#
# When a duplicate combination is detected, a cycle, we can calculate how much
# different there is in the height of the tower since then and extrapolate how
# high it will be after many, many more cycles (up to 1 trillion pieces)
seen_jet_piece_combinations = {}

NUM_PIECES = 1_000_000_000_000
for piece_count in range(NUM_PIECES):
    piece_index, piece = next(iter_pieces)

    # Piece positions are seen from their bottom-left corner, 0-indexed
    piece_x = 3
    piece_y = chamber.tower_height() + 4

    piece_put_at_rest = False
    while not piece_put_at_rest:
        jet_index, jet_direction = next(jet_pattern)
        delta_x = delta_x_for_symbol(jet_direction)

        can_move = True
        for row_y, row in enumerate(reversed(piece)):
            for row_x, symbol in enumerate(row):
                if symbol == SYMBOL_EMPTY:
                    continue

                if (
                    chamber.get(piece_x + row_x + delta_x, piece_y + row_y)
                    == SYMBOL_ROCK
                ):
                    can_move = False
                    break

        if can_move:
            piece_x += delta_x

        # Going from the bottom row of the piece, check if it has dropped on any
        # block or floor below
        is_blocked = False
        for symbol_y, piece_row in enumerate(reversed(piece)):
            for symbol_x, symbol in enumerate(piece_row):
                if symbol == SYMBOL_EMPTY:
                    continue

                x = piece_x + symbol_x
                y = piece_y + symbol_y

                if chamber.get(x, y - 1) == SYMBOL_ROCK:
                    is_blocked = True
                    break

            if is_blocked:
                break

        if not is_blocked:
            # Piece is not stopped by collision so let it fall down one row
            piece_y -= 1
            continue

        for symbol_y, piece_row in enumerate(reversed(piece)):
            for symbol_x, symbol in enumerate(piece_row):
                # Put all symbols of the piece to rest in the chamber

                if symbol == SYMBOL_EMPTY:
                    continue

                x = piece_x + symbol_x
                y = piece_y + symbol_y

                chamber.mark_blocked(x, y)
                piece_put_at_rest = True

        jet_piece_id = (jet_index, piece_index)
        if jet_piece_id in seen_jet_piece_combinations:
            prev_block_count, prev_tower_height = seen_jet_piece_combinations[
                jet_piece_id
            ]
            period = piece_count - prev_block_count
            if piece_count % period == NUM_PIECES % period:
                print(
                    f"Cycle of period {period} detected",
                    f"(in iterations {prev_block_count-period}-{prev_block_count}",
                    f"and {prev_block_count}-{piece_count})",
                )
                cycle_height = chamber.tower_height() - prev_tower_height
                pieces_remaining = NUM_PIECES - piece_count
                cycles_remaining = (pieces_remaining // period) + 1
                print(prev_tower_height + (cycle_height * cycles_remaining) - 1)

                sys.exit(0)
        else:
            seen_jet_piece_combinations[jet_piece_id] = (
                piece_count,
                chamber.tower_height(),
            )

chamber.tower_height()
