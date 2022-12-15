"""
--- Day 14: Regolith Reservoir ---

The distress signal leads you to a giant waterfall! Actually, hang on - the
signal seems like it's coming from the waterfall itself, and that doesn't make
any sense. However, you do notice a little path that leads behind the
waterfall.

Correction: the distress signal leads you behind a giant waterfall! There seems
to be a large cave system here, and the signal definitely leads further inside.

As you begin to make your way deeper underground, you feel the ground rumble
for a moment. Sand begins pouring into the cave! If you don't quickly figure
out where the sand is going, you could quickly become trapped!

Fortunately, your familiarity with analyzing the path of falling material will
come in handy here. You scan a two-dimensional vertical slice of the cave above
you (your puzzle input) and discover that it is mostly air with structures made
of rock.

Your scan traces the path of each solid rock structure and reports the x,y
coordinates that form the shape of the path, where x represents distance to the
right and y represents distance down. Each path appears as a single line of
text in your scan. After the first point of each path, each point indicates the
end of a straight horizontal or vertical line to be drawn from the previous
point. For example:

498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9

This scan means that there are two paths of rock; the first path consists of
two straight lines, and the second path consists of three straight lines.
(Specifically, the first path consists of a line of rock from 498,4 through
498,6 and another line of rock from 498,6 through 496,6.)

The sand is pouring into the cave from point 500,0.

Drawing rock as #, air as ., and the source of the sand as +, this becomes:


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.

Sand is produced one unit at a time, and the next unit of sand is not produced
until the previous unit of sand comes to rest. A unit of sand is large enough
to fill one tile of air in your scan.

A unit of sand always falls down one step if possible. If the tile immediately
below is blocked (by rock or sand), the unit of sand attempts to instead move
diagonally one step down and to the left. If that tile is blocked, the unit of
sand attempts to instead move diagonally one step down and to the right. Sand
keeps moving as long as it is able to do so, at each step trying to move down,
then down-left, then down-right. If all three possible destinations are
blocked, the unit of sand comes to rest and no longer moves, at which point the
next unit of sand is created back at the source.

So, drawing sand that has come to rest as o, the first unit of sand simply
falls straight down and then stops:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......o.#.
#########.

The second unit of sand then falls straight down, lands on the first one, and
then comes to rest to its left:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
.....oo.#.
#########.

After a total of five units of sand have come to rest, they form this pattern:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
....oooo#.
#########.

After a total of 22 units of sand:

......+...
..........
......o...
.....ooo..
....#ooo##
....#ooo#.
..###ooo#.
....oooo#.
...ooooo#.
#########.

Finally, only two more units of sand can possibly come to rest:

......+...
..........
......o...
.....ooo..
....#ooo##
...o#ooo#.
..###ooo#.
....oooo#.
.o.ooooo#.
#########.

Once all 24 units of sand shown above have come to rest, all further sand flows
out the bottom, falling into the endless void. Just for fun, the path any new
sand takes before falling forever is shown here with ~:

.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........

Using your scan, simulate the falling sand. How many units of sand come to rest
before sand starts flowing into the abyss below?

--- Part Two ---

You realize you misread the scan. There isn't an endless void at the bottom of
the scan - there's floor, and you're standing on it!

You don't have time to scan the floor, so assume the floor is an infinite
horizontal line with a y coordinate equal to two plus the highest y coordinate
of any point in your scan.

In the example above, the highest y coordinate of any point is 9, and so the
floor is at y=11. (This is as if your scan contained one extra rock path like
-infinity,11 -> infinity,11.) With the added floor, the example above now looks
like this:

        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
<-- etc #################### etc -->

To find somewhere safe to stand, you'll need to simulate falling sand until a
unit of sand comes to rest at 500,0, blocking the source entirely and stopping
the flow of sand into the cave. In the example above, the situation finally
looks like this after 93 units of sand come to rest:

............o............
...........ooo...........
..........ooooo..........
.........ooooooo.........
........oo#ooo##o........
.......ooo#ooo#ooo.......
......oo###ooo#oooo......
.....oooo.oooo#ooooo.....
....oooooooooo#oooooo....
...ooo#########ooooooo...
..ooooo.......ooooooooo..
#########################

Using your scan, simulate the falling sand until the source of the sand becomes
blocked. How many units of sand come to rest?
"""

from collections import namedtuple
from enum import Enum


class Tile(Enum):
    Air = 0
    Rock = 1
    Sand = 2


Coordinate = namedtuple("Coordinate", ["x", "y"])


class Cave:
    def __init__(self, horizontal_size, vertical_size) -> None:
        # From, to
        self.horizontal_size = horizontal_size
        # From, to
        self.vertical_size = vertical_size

        # {Coordinate: Tile}
        self.tiles = {}

    def set_tile(self, coordinate: Coordinate, tile: Tile):
        if tile is Tile.Air:
            del self.tiles[coordinate]
            return

        self.tiles[coordinate] = tile

    def tile_at(self, coordinate: Coordinate) -> Tile:
        if coordinate.y == self.vertical_size[1]:
            # Coordinate is pointing at the floor of the cave
            return Tile.Rock

        return self.tiles.get(coordinate, Tile.Air)


def parse_cave_structure(lines: list[str]) -> Cave:
    rock_coordinates = set()
    min_x, max_x = 2**31, 500
    min_y, max_y = 0, 0

    for line in lines:
        coordinates = []
        parts = map(lambda t: t.strip(), line.split("->"))
        for part in parts:
            x, y = part.split(",")
            coordinate = Coordinate(int(x), int(y))

            min_x = min(min_x, coordinate.x)
            max_x = max(max_x, coordinate.x)
            min_y = min(min_y, coordinate.y)
            max_y = max(max_y, coordinate.y)

            coordinates.append(coordinate)

        for i in range(1, len(coordinates)):
            if coordinates[i - 1].y == coordinates[i].y:
                # Create a horizontal line of rock
                from_x = min(coordinates[i - 1].x, coordinates[i].x)
                to_x = max(coordinates[i - 1].x, coordinates[i].x)
                for x in range(from_x, to_x + 1):
                    rock_coordinates.add(Coordinate(x, coordinates[i].y))
            else:
                # Create a vertical line of rock
                from_y = min(coordinates[i - 1].y, coordinates[i].y)
                to_y = max(coordinates[i - 1].y, coordinates[i].y)
                for y in range(from_y, to_y + 1):
                    rock_coordinates.add(Coordinate(coordinates[i].x, y))

    # '+ 2' because there's a floor two steps below the lowest piece of rock
    max_y += 2

    cave = Cave((min_x, max_x), (min_y, max_y))
    for coordinate in rock_coordinates:
        cave.set_tile(coordinate, Tile.Rock)

    return cave


# puzzle_input = open("../puzzle-input/day14-example-input.txt").readlines()
puzzle_input = open("../puzzle-input/day14-input.txt").readlines()

cave = parse_cave_structure(puzzle_input)

source_position = Coordinate(500, 0)
next_position = Coordinate(source_position.x, source_position.y - 1)
num_sand_at_rest = 0

while True:
    sand = next_position
    next_position = Coordinate(sand.x, sand.y + 1)

    if cave.tile_at(next_position) is Tile.Air:
        continue

    # Try falling diagonally to the left
    next_position = Coordinate(sand.x - 1, sand.y + 1)
    if cave.tile_at(next_position) is Tile.Air:
        continue

    # Try falling diagonally to the right
    next_position = Coordinate(sand.x + 1, sand.y + 1)
    if cave.tile_at(next_position) is Tile.Air:
        continue

    # Sand can't go anywhere so put it at rest here
    cave.set_tile(sand, Tile.Sand)
    num_sand_at_rest += 1
    next_position = Coordinate(source_position.x, source_position.y - 1)

    # Sand can't go anywhere but is still at the source position, meaning
    # the source of the sand is blocked and won't be depositing any more
    # sand
    if sand == source_position:
        break

print(num_sand_at_rest)
