"""
--- Day 24: Blizzard Basin ---

With everything replanted for next year (and with elephants and monkeys to tend
the grove), you and the Elves leave for the extraction point.

Partway up the mountain that shields the grove is a flat, open area that serves
as the extraction point. It's a bit of a climb, but nothing the expedition
can't handle.

At least, that would normally be true; now that the mountain is covered in
snow, things have become more difficult than the Elves are used to.

As the expedition reaches a valley that must be traversed to reach the
extraction site, you find that strong, turbulent winds are pushing small
blizzards of snow and sharp ice around the valley. It's a good thing everyone
packed warm clothes! To make it across safely, you'll need to find a way to
avoid them.

Fortunately, it's easy to see all of this from the entrance to the valley, so
you make a map of the valley and the blizzards (your puzzle input). For
example:

#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#

The walls of the valley are drawn as #; everything else is ground. Clear ground
- where there is currently no blizzard - is drawn as .. Otherwise, blizzards
are drawn with an arrow indicating their direction of motion: up (^), down (v),
left (<), or right (>).

The above map includes two blizzards, one moving right (>) and one moving down
(v). In one minute, each blizzard moves one position in the direction it is
pointing:

#.#####
#.....#
#.>...#
#.....#
#.....#
#...v.#
#####.#

Due to conservation of blizzard energy, as a blizzard reaches the wall of the
valley, a new blizzard forms on the opposite side of the valley moving in the
same direction. After another minute, the bottom downward-moving blizzard has
been replaced with a new downward-moving blizzard at the top of the valley
instead:

#.#####
#...v.#
#..>..#
#.....#
#.....#
#.....#
#####.#

Because blizzards are made of tiny snowflakes, they pass right through each
other. After another minute, both blizzards temporarily occupy the same
position, marked 2:

#.#####
#.....#
#...2.#
#.....#
#.....#
#.....#
#####.#

After another minute, the situation resolves itself, giving each blizzard back
its personal space:

#.#####
#.....#
#....>#
#...v.#
#.....#
#.....#
#####.#

Finally, after yet another minute, the rightward-facing blizzard on the right
is replaced with a new one on the left facing the same direction:

#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#

This process repeats at least as long as you are observing it, but probably
forever.

Here is a more complex example:

#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#

Your expedition begins in the only non-wall position in the top row and needs
to reach the only non-wall position in the bottom row. On each minute, you can
move up, down, left, or right, or you can wait in place. You and the blizzards
act simultaneously, and you cannot share a position with a blizzard.

In the above example, the fastest way to reach your goal requires 18 steps.
Drawing the position of the expedition as E, one way to achieve this is:

Initial state:
#E######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#

Minute 1, move down:
#.######
#E>3.<.#
#<..<<.#
#>2.22.#
#>v..^<#
######.#

Minute 2, move down:
#.######
#.2>2..#
#E^22^<#
#.>2.^>#
#.>..<.#
######.#

Minute 3, wait:
#.######
#<^<22.#
#E2<.2.#
#><2>..#
#..><..#
######.#

Minute 4, move up:
#.######
#E<..22#
#<<.<..#
#<2.>>.#
#.^22^.#
######.#

Minute 5, move right:
#.######
#2Ev.<>#
#<.<..<#
#.^>^22#
#.2..2.#
######.#

Minute 6, move right:
#.######
#>2E<.<#
#.2v^2<#
#>..>2>#
#<....>#
######.#

Minute 7, move down:
#.######
#.22^2.#
#<vE<2.#
#>>v<>.#
#>....<#
######.#

Minute 8, move left:
#.######
#.<>2^.#
#.E<<.<#
#.22..>#
#.2v^2.#
######.#

Minute 9, move up:
#.######
#<E2>>.#
#.<<.<.#
#>2>2^.#
#.v><^.#
######.#

Minute 10, move right:
#.######
#.2E.>2#
#<2v2^.#
#<>.>2.#
#..<>..#
######.#

Minute 11, wait:
#.######
#2^E^2>#
#<v<.^<#
#..2.>2#
#.<..>.#
######.#

Minute 12, move down:
#.######
#>>.<^<#
#.<E.<<#
#>v.><>#
#<^v^^>#
######.#

Minute 13, move down:
#.######
#.>3.<.#
#<..<<.#
#>2E22.#
#>v..^<#
######.#

Minute 14, move right:
#.######
#.2>2..#
#.^22^<#
#.>2E^>#
#.>..<.#
######.#

Minute 15, move right:
#.######
#<^<22.#
#.2<.2.#
#><2>E.#
#..><..#
######.#

Minute 16, move right:
#.######
#.<..22#
#<<.<..#
#<2.>>E#
#.^22^.#
######.#

Minute 17, move down:
#.######
#2.v.<>#
#<.<..<#
#.^>^22#
#.2..2E#
######.#

Minute 18, move down:
#.######
#>2.<.<#
#.2v^2<#
#>..>2>#
#<....>#
######E#

What is the fewest number of minutes required to avoid the blizzards and reach
the goal?

--- Part Two ---

As the expedition reaches the far side of the valley, one of the Elves looks
especially dismayed:

He forgot his snacks at the entrance to the valley!

Since you're so good at dodging blizzards, the Elves humbly request that you go
back for his snacks. From the same initial conditions, how quickly can you make
it from the start to the goal, then back to the start, then back to the goal?

In the above example, the first trip to the goal takes 18 minutes, the trip
back to the start takes 23 minutes, and the trip back to the goal again takes
13 minutes, for a total time of 54 minutes.

What is the fewest number of minutes required to reach the goal, go back to the
start, then reach the goal again?
"""

from collections import defaultdict, namedtuple
from heapq import heappush, heappop


Point = namedtuple("Point", ["x", "y"])
Size = namedtuple("Size", ["width", "height"])
Blizzard = namedtuple("Blizzard", ["position", "direction"])
Step = namedtuple("Step", ["position", "minute", "map_variation_idx"])


class Symbol:
    UP = "^"
    LEFT = "<"
    RIGHT = ">"
    DOWN = "v"
    EMPTY = "."
    WALL = "#"
    START = "S"
    EXIT = "E"
    PATH = "+"


class Direction:
    UP = Point(0, -1)
    RIGHT = Point(1, 0)
    DOWN = Point(0, 1)
    LEFT = Point(-1, 0)


class Map:
    """A map of the basin, with all blizzards and where they are located at a
    given minute.
    """

    def __init__(
        self, size: Size, entrance: Point, exit: Point, blizzards: list[Blizzard]
    ) -> None:
        self.size = size
        self.entrance = entrance
        self.exit = exit
        self.blizzards = blizzards

        self._cache_blizzard_positions()

    def _cache_blizzard_positions(self):
        """Builds a set of positions (`Point`) that contain at least one
        blizzard, speeds up checks of if a certain Coordinate is occupied from
        O(N) to O(1).
        """
        self.blizzard_positions = set([b.position for b in self.blizzards])

    def is_accessible(self, position: Point) -> bool:
        """Is the given position free to go to, or is it occupied by either a
        wall or a blizzard?
        """

        # Don't go out of bounds
        if not -1 < position.x < self.size.width:
            return False

        if not -1 < position.y < self.size.height:
            return False

        # It's unclear from the puzzle description if the entrance or exit tile
        # could become blocked by a blizzard, but because the example inputs
        # and real puzzle input don't have blizzards that can blow into those
        # positions we can assume they are always free.
        if position == self.entrance or position == self.exit:
            return True

        if self.is_wall(position):
            return False

        if position in self.blizzard_positions:
            return False

        return True

    def is_wall(self, position: Point) -> bool:
        # Walls to the left and right of the basin
        if position.x == 0 or position.x == self.size.width - 1:
            return True

        # Walls at the top and bottom of the basin
        if position.y == 0 or position.y == self.size.height - 1:
            return True

        return False


def parse_map(lines: list[str]) -> Map:
    map_size = Size(len(lines[0].strip()), len(lines))
    entrance = Point(lines[0].index("."), 0)
    exit = Point(lines[-1].index("."), map_size.height - 1)

    blizzards = []
    for y, line in enumerate(lines):
        for x, symbol in enumerate(line.strip()):
            match symbol:
                case Symbol.UP:
                    direction = Direction.UP

                case Symbol.RIGHT:
                    direction = Direction.RIGHT

                case Symbol.DOWN:
                    direction = Direction.DOWN

                case Symbol.LEFT:
                    direction = Direction.LEFT

                case _:
                    continue

            blizzards.append(Blizzard(Point(x, y), direction))

    return Map(map_size, entrance, exit, blizzards)


def create_map_variations(map: Map) -> list[Map]:
    """
    Builds a list of all possible maps, with regards to the positions of the
    blizzards.

    Since the blizzards simply wrap around when hitting a wall, there are a
    finite number of places they can be in. At some point it will simply become
    a cycle.
    """
    map_variations = [map]

    map_variation = move_blizzards(map)
    while map_variation.blizzards != map_variations[0].blizzards:
        map_variations.append(map_variation)
        map_variation = move_blizzards(map_variation)

    return map_variations


def move_blizzards(map: Map) -> Map:
    moved_blizzards = []
    for blizzard in map.blizzards:
        new_blizzard_pos = Point(
            blizzard.position.x + blizzard.direction.x,
            blizzard.position.y + blizzard.direction.y,
        )

        if map.is_wall(new_blizzard_pos):
            # Wrap the blizzard to the other side of the basin
            match blizzard.direction:
                case Direction.UP:
                    new_blizzard_pos = Point(new_blizzard_pos.x, map.size.height - 2)

                case Direction.RIGHT:
                    new_blizzard_pos = Point(1, new_blizzard_pos.y)

                case Direction.DOWN:
                    new_blizzard_pos = Point(new_blizzard_pos.x, 1)

                case Direction.LEFT:
                    new_blizzard_pos = Point(map.size.width - 2, new_blizzard_pos.y)

        moved_blizzards.append(Blizzard(new_blizzard_pos, blizzard.direction))

    return Map(map.size, map.entrance, map.exit, moved_blizzards)


def find_path(map_variations: list[Map], start_map_variation_idx=0):
    num_map_variations = len(map_variations)
    current_map_variation_idx = start_map_variation_idx
    map = map_variations[start_map_variation_idx]

    queue = []
    heappush(queue, (0, map.entrance, 0, start_map_variation_idx))

    cost_so_far = []
    for _ in range(num_map_variations):
        cost_so_far.append(defaultdict(lambda: 999_999_999))

    came_from = []
    for _ in range(num_map_variations):
        came_from.append(defaultdict(lambda: None))

    while queue:
        (
            cost_to_reach_exit,
            current_position,
            minute,
            current_map_variation_idx,
        ) = heappop(queue)

        if current_position == map.exit:
            cost_so_far[current_map_variation_idx][map.exit] = cost_to_reach_exit
            break

        # Because all movement (elf and blizzards) happen at the same minute,
        # look at how the map will look like in the next minute
        current_map_variation = map_variations[current_map_variation_idx]

        # next_cost = cost_so_far[map_variation_idx][current_position] + 1
        next_cost = minute + 1
        next_minute = minute + 1
        next_map_variation_idx = (current_map_variation_idx + 1) % num_map_variations

        # Consider movement options
        next_possible_positions = next_moves(current_map_variation, current_position)

        for next_position in next_possible_positions:
            if (
                next_position not in cost_so_far[current_map_variation_idx]
                or cost_so_far[current_map_variation_idx][next_position] > next_cost
            ):
                cost_so_far[current_map_variation_idx][next_position] = next_cost
                came_from[current_map_variation_idx][next_position] = current_position

                next_priority = next_cost + manhattan_distance(next_position, map.exit)
                heappush(
                    queue,
                    (next_priority, next_position, next_minute, next_map_variation_idx),
                )

    if map.exit not in cost_so_far[current_map_variation_idx]:
        raise Exception("Could not find a route")

    time_passed = cost_so_far[current_map_variation_idx][map.exit] - 1

    # This route is not complete: it doesn't show any backtracking done by the elves.
    route = [map.exit]
    while route[-1] != map.entrance:
        current_map_variation_idx = (current_map_variation_idx - 1) % num_map_variations
        route.append(came_from[current_map_variation_idx][route[-1]])
    route.reverse()

    return route, time_passed


def next_moves(map: Map, from_: Point) -> list[Point]:
    """Build a list of positions that can be visited from position `from_`,
    discarding those that would move you into a wall, a blizzard or would go
    out-of-bounds of the map.
    """
    next_points = []

    # Delta coordinates for the directions up, right, down, left, and for waiting here.
    for delta_x, delta_y in [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]:
        next_x = from_.x + delta_x
        next_y = from_.y + delta_y
        next_point = Point(next_x, next_y)

        if not map.is_accessible(next_point):
            continue

        next_points.append(Point(next_x, next_y))

    return next_points


def manhattan_distance(from_: Point, to_: Point) -> int:
    return abs(from_[0] - to_[0]) + abs(from_[1] - to_[1])


def print_route(map, route):
    for y in range(map.size.height):
        for x in range(map.size.width):
            point = Point(x, y)
            if point == route[0]:
                # Start of the route
                print(Symbol.START, end="")
            elif point == route[-1]:
                # End of the route
                print(Symbol.EXIT, end="")
            elif point in route:
                print(Symbol.PATH, end="")
            else:
                print(Symbol.EMPTY, end="")

        # Newline
        print()


# map_data = open("../puzzle-input/day24-simple-example-input.txt").readlines()
# map_data = open("../puzzle-input/day24-complex-example-input.txt").readlines()
map_data = open("../puzzle-input/day24-input.txt").readlines()

map = parse_map(map_data)

map_variations = create_map_variations(map)
num_map_variations = len(map_variations)
print("There are", num_map_variations, "variations of the map")

total_time_passed = 0
time_passed = 0
for i in range(3):
    start_map_variation_idx = total_time_passed % num_map_variations

    if i % 2 == 1:
        # Now, move back to the start with the map variation set to how it was at the end of the first route
        # Swap the entrance and exit positions
        (
            map_variations[start_map_variation_idx].entrance,
            map_variations[start_map_variation_idx].exit,
        ) = (
            map_variations[start_map_variation_idx].exit,
            map_variations[start_map_variation_idx].entrance,
        )

    route, time_passed = find_path(map_variations, start_map_variation_idx)
    print_route(map, route)
    print(time_passed)

    if i % 2 == 1:
        # Swap the entrance and exit positions back in case the third route
        # also begins on this map variation
        (
            map_variations[start_map_variation_idx].entrance,
            map_variations[start_map_variation_idx].exit,
        ) = (
            map_variations[start_map_variation_idx].exit,
            map_variations[start_map_variation_idx].entrance,
        )

    total_time_passed += time_passed

print(total_time_passed)
