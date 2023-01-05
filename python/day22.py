"""
--- Day 22: Monkey Map ---

The monkeys take you on a surprisingly easy trail through the jungle. They're
even going in roughly the right direction according to your handheld device's
Grove Positioning System.

As you walk, the monkeys explain that the grove is protected by a force field.
To pass through the force field, you have to enter a password; doing so
involves tracing a specific path on a strangely-shaped board.

At least, you're pretty sure that's what you have to do; the elephants aren't
exactly fluent in monkey.

The monkeys give you notes that they took when they last saw the password
entered (your puzzle input).

For example:

        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5

The first half of the monkeys' notes is a map of the board. It is comprised of
a set of open tiles (on which you can move, drawn .) and solid walls (tiles
which you cannot enter, drawn #).

The second half is a description of the path you must follow. It consists of
alternating numbers and letters:

* A number indicates the number of tiles to move in the direction you are
  facing. If you run into a wall, you stop moving forward and continue with the
  next instruction.
* A letter indicates whether to turn 90 degrees clockwise (R) or
  counterclockwise (L). Turning happens in-place; it does not change your current
  tile.

So, a path like 10R5 means "go forward 10 tiles, then turn clockwise 90
degrees, then go forward 5 tiles".

You begin the path in the leftmost open tile of the top row of tiles.
Initially, you are facing to the right (from the perspective of how the map is
drawn).

If a movement instruction would take you off of the map, you wrap around to the
other side of the board. In other words, if your next tile is off of the board,
you should instead look in the direction opposite of your current facing as far
as you can until you find the opposite edge of the board, then reappear there.

For example, if you are at A and facing to the right, the tile in front of you
is marked B; if you are at C and facing down, the tile in front of you is
marked D:

        ...#
        .#..
        #...
        ....
...#.D.....#
........#...
B.#....#...A
.....C....#.
        ...#....
        .....#..
        .#......
        ......#.

It is possible for the next tile (after wrapping around) to be a wall; this
still counts as there being a wall in front of you, and so movement stops
before you actually wrap to the other side of the board.

By drawing the last facing you had with an arrow on each tile you visit, the
full path taken by the above example looks like this:

        >>v#
        .#v.
        #.v.
        ..v.
...#...v..v#
>>>v...>#.>>
..#v...#....
...>>>>v..#.
        ...#....
        .....#..
        .#......
        ......#.

To finish providing the password to this strange input device, you need to
determine numbers for your final row, column, and facing as your final position
appears from the perspective of the original map. Rows start from 1 at the top
and count downward; columns start from 1 at the left and count rightward.
(In the above example, row 1, column 1 refers to the empty space with no tile
on it in the top-left corner.) Facing is 0 for right (>), 1 for down (v), 2 for
left (<), and 3 for up (^). The final password is the sum of 1000 times the
row, 4 times the column, and the facing.

In the above example, the final row is 6, the final column is 8, and the final
facing is 0. So, the final password is 1000 * 6 + 4 * 8 + 0: 6032.

Follow the path given in the monkeys' notes. What is the final password?
"""

from collections import defaultdict, namedtuple
from enum import Enum
from itertools import product


Coordinates = namedtuple("Coordinates", ["x", "y"])


class Direction(Enum):
    RIGHT = 90
    DOWN = 180
    LEFT = 270
    UP = 0

    def turn_left(self) -> "Direction":
        return Direction((self.value - 90) % 360)

    def turn_right(self) -> "Direction":
        return Direction((self.value + 90) % 360)


class Map:
    def __init__(self) -> None:
        self.rows = []


class CellType(Enum):
    Wall = 0
    Open = 1


class MapCell:
    def __init__(self, coordinates: Coordinates, type_: CellType):
        self.coordinates = coordinates
        self.type = type_
        self.neighbours = defaultdict(None)

    def set_neighbour(self, direction, cell: "MapCell"):
        if self.neighbours[direction] is not None:
            raise Exception("Should not be setting a neighbour twice")

        self.neighbours[direction] = cell

    def __str__(self):
        return "#" if self.type is CellType.Wall else "."


def parse_steps(description: str) -> list[str | int]:
    description = description.strip()
    cursor = 0
    steps = []

    while cursor < len(description):
        next_turn_position = [
            description.find("L", cursor),
            description.find("R", cursor),
        ]
        if max(next_turn_position) == -1:
            # We've reached the end of the description, only one more move
            # instruction remains
            next_turn_position = len(description)
        else:
            next_turn_position = min(filter(lambda n: n > 0, next_turn_position))

        if next_turn_position > cursor:
            move_instruction = description[cursor:next_turn_position]
            steps.append(int(move_instruction))
            cursor += len(move_instruction)
        else:
            cursor = next_turn_position
            steps.append(description[cursor])
            cursor += 1

    return steps


def parse_map(lines: list[str]) -> Map:
    map = Map()

    for y, line in enumerate(lines):
        if not line.strip():
            continue

        row = []
        row_index = 0

        for x, symbol in enumerate(line.rstrip()):
            match symbol:
                case " ":
                    # Void
                    continue

                case ".":
                    # Open tile
                    cell = MapCell(Coordinates(x, y), CellType.Open)
                    row.append(cell)

                case "#":
                    # Wall
                    cell = MapCell(Coordinates(x, y), CellType.Wall)
                    row.append(cell)

                case other:
                    raise Exception("Unknown symbol encountered", other)

            # Set left and right neighbours
            if row_index > 0:
                cell.neighbours[Direction.LEFT] = row[row_index - 1]
                row[row_index - 1].neighbours[Direction.RIGHT] = cell

            row_index += 1

        # Wrap the right end of the row to the start of it, and vice versa
        row[-1].neighbours[Direction.RIGHT] = row[0]
        row[0].neighbours[Direction.LEFT] = row[-1]

        map.rows.append(row)

    # Set upper and lower neighbours
    previous_row = None
    for y, row in enumerate(map.rows):
        if y == 0:
            previous_row = row
            continue

        # Check all X/column combinations of the current and previous row to
        # see if any of them are positioned next to eachother
        for prev_x, x in product(range(len(previous_row)), range(len(row))):
            if previous_row[prev_x].coordinates.x == row[x].coordinates.x:
                previous_row[prev_x].neighbours[Direction.DOWN] = row[x]
                row[x].neighbours[Direction.UP] = previous_row[prev_x]

        previous_row = row

    # Let the start and end of columns wrap to eachother
    column_start = {}
    column_end = {}
    for y, row in enumerate(map.rows):
        for cell in row:
            if column_start.get(cell.coordinates.x, None) is None:
                column_start[cell.coordinates.x] = cell

            column_end[cell.coordinates.x] = cell

    for start, end in zip(column_start.values(), column_end.values()):
        start.neighbours[Direction.UP] = end
        end.neighbours[Direction.DOWN] = start

    return map


# puzzle_input = open("../puzzle-input/day22-example-input.txt").readlines()
puzzle_input = open("../puzzle-input/day22-input.txt").readlines()

steps = parse_steps(puzzle_input[-1])
map = parse_map(puzzle_input[:-1])

assert map.rows[0][0].type is not CellType.Wall
current_cell = map.rows[0][0]
current_direction = Direction.RIGHT

for step in steps:
    if type(step) is int:
        # Take X steps in the current direction (or until we hit a wall)
        for _ in range(step):
            if current_cell.neighbours[current_direction].type is CellType.Wall:
                break

            current_cell = current_cell.neighbours[current_direction]
    elif step == "R":
        current_direction = current_direction.turn_right()
    elif step == "L":
        current_direction = current_direction.turn_left()
    else:
        raise Exception("Unknown instruction")

direction_value = (
    3 if current_direction is Direction.UP else (current_direction.value // 90) - 1
)
password = (
    1000 * (current_cell.coordinates.y + 1)
    + 4 * (current_cell.coordinates.x + 1)
    + direction_value
)
print(password)
