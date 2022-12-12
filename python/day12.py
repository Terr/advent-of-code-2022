"""
--- Day 12: Hill Climbing Algorithm ---

You try contacting the Elves using your handheld device, but the river you're
following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input).
The heightmap shows the local area from above broken into a grid; the elevation
of each square of the grid is given by a single lowercase letter, where a is
the lowest elevation, b is the next-lowest, and so on up to the highest
elevation, z.

Also included on the heightmap are marks for your current position (S) and the
location that should get the best signal (E). Your current position (S) has
elevation a, and the location that should get the best signal (E) has elevation
z.

You'd like to reach E, but to save energy, you should do it in as few steps as
possible. During each step, you can move exactly one square up, down, left, or
right. To avoid needing to get out your climbing gear, the elevation of the
destination square can be at most one higher than the elevation of your current
square; that is, if your current elevation is m, you could step to elevation n,
but not to elevation o. (This also means that the elevation of the destination
square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could
start by moving down or right, but eventually you'll need to head toward the e
at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square
moving up (^), down (v), left (<), or right (>). The location that should get
the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the
location that should get the best signal?
"""

from collections import namedtuple
from heapq import heappush, heappop


Coordinate = namedtuple("Coordinate", ["x", "y"])


class Map:
    def __init__(self, squares, width, height, start_position, end_position):
        self.squares: list[int] = squares
        self.width: int = width
        self.height: int = height
        self.start_position: Coordinate = start_position
        self.end_position: Coordinate = end_position

    def height_at(self, coordinate: Coordinate) -> int:
        if not self.is_in_bounds(coordinate):
            return 255

        square_index = coordinate.y * self.width + coordinate.x

        return self.squares[square_index]

    def adjacent_squares(self, coordinate: Coordinate) -> list[Coordinate]:
        adjacent_squares = []

        for delta_x in [-1, 1]:
            adjacent_coordinate = Coordinate(coordinate.x + delta_x, coordinate.y)

            if self.is_in_bounds(adjacent_coordinate):
                adjacent_squares.append(adjacent_coordinate)

        for delta_y in [-1, 1]:
            adjacent_coordinate = Coordinate(coordinate.x, coordinate.y + delta_y)

            if self.is_in_bounds(adjacent_coordinate):
                adjacent_squares.append(adjacent_coordinate)

        return adjacent_squares

    def is_in_bounds(self, coordinate: Coordinate) -> bool:
        if coordinate.x < 0 or coordinate.y < 0:
            return False

        if coordinate.x >= self.width or coordinate.y >= self.height:
            return False

        return True


def search_path(map: Map) -> list[Coordinate]:
    queue = []
    heappush(queue, (0, map.start_position))

    came_from = {}
    cost_so_far = {}

    came_from[map.start_position] = None
    cost_so_far[map.start_position] = 0

    while queue:
        _, current = heappop(queue)
        current_height = map.height_at(current)

        if current == map.end_position:
            break

        for next_square in map.adjacent_squares(current):
            new_cost = cost_so_far[current] + 1

            next_height = map.height_at(next_square)
            if next_height - current_height > 1:
                # We can only go up 1 level of height
                continue

            if next_square not in cost_so_far or new_cost < cost_so_far[next_square]:
                cost_so_far[next_square] = new_cost

                priority = new_cost + manhattan_distance(next_square, map.end_position)
                heappush(queue, (priority, next_square))
                came_from[next_square] = current

    if map.end_position not in came_from:
        raise Exception("Did not find a route to the end position")

    route = [map.end_position]
    while route[-1] != map.start_position:
        previous_step = came_from[route[-1]]
        route.append(previous_step)
    route.reverse()

    return route


def manhattan_distance(from_: Coordinate, to_: Coordinate) -> int:
    return abs(from_[0] - to_[0]) + abs(from_[1] - to_[1])


def parse_map(lines: list[str]) -> Map:
    squares = []
    map_width = len(lines[0].strip())
    map_height = len(lines)
    start_position = None
    end_position = None

    for y, row in enumerate(lines):
        row = row.strip()

        for x, column in enumerate(row):
            if column == "S":
                start_position = Coordinate(x, y)
                column = "a"
            elif column == "E":
                end_position = Coordinate(x, y)
                column = "z"

            square_height = ord(column) - ord("a")
            squares.append(square_height)

    assert start_position is not None
    assert end_position is not None

    return Map(squares, map_width, map_height, start_position, end_position)


# puzzle_input = open("../puzzle-input/day12-example-input.txt").readlines()
puzzle_input = open("../puzzle-input/day12-input.txt").readlines()

map = parse_map(puzzle_input)

print(len(search_path(map)) - 1)
