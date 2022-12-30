"""
--- Day 23: Unstable Diffusion ---

You enter a large crater of gray dirt where the grove is supposed to be. All
around you, plants you imagine were expected to be full of fruit are instead
withered and broken. A large group of Elves has formed in the middle of the
grove.

"...but this volcano has been dormant for months. Without ash, the fruit can't
grow!"

You look up to see a massive, snow-capped mountain towering above you.

"It's not like there are other active volcanoes here; we've looked everywhere."

"But our scanners show active magma flows; clearly it's going somewhere."

They finally notice you at the edge of the grove, your pack almost overflowing
from the random star fruit you've been collecting. Behind you, elephants and
monkeys explore the grove, looking concerned. Then, the Elves recognize the ash
cloud slowly spreading above your recent detour.

"Why do you--" "How is--" "Did you just--"

Before any of them can form a complete question, another Elf speaks up: "Okay,
new plan. We have almost enough fruit already, and ash from the plume should
spread here eventually. If we quickly plant new seedlings now, we can still
make it to the extraction point. Spread out!"

The Elves each reach into their pack and pull out a tiny plant. The plants rely
on important nutrients from the ash, so they can't be planted too close
together.

There isn't enough time to let the Elves figure out where to plant the
seedlings themselves; you quickly scan the grove (your puzzle input) and note
their positions.

For example:

....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..

The scan shows Elves # and empty ground .; outside your scan, more empty ground
extends a long way in every direction. The scan is oriented so that north is
up; orthogonal directions are written N (north), S (south), W (west), and E
(east), while diagonal directions are written NE, NW, SE, SW.

The Elves follow a time-consuming process to figure out where they should each
go; you can speed up this process considerably. The process consists of some
number of rounds during which Elves alternate between considering where to move
and actually moving.

During the first half of each round, each Elf considers the eight positions
adjacent to themself. If no other Elves are in one of those eight positions,
the Elf does not do anything during this round. Otherwise, the Elf looks in
each of four directions in the following order and proposes moving one step in
the first valid direction:

    If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
    If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
    If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
    If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.

After each Elf has had a chance to propose a move, the second half of the round
can begin. Simultaneously, each Elf moves to their proposed destination tile if
they were the only Elf to propose moving to that position. If two or more Elves
propose moving to the same position, none of those Elves move.

Finally, at the end of the round, the first direction the Elves considered is
moved to the end of the list of directions. For example, during the second
round, the Elves would try proposing a move to the south first, then west, then
east, then north. On the third round, the Elves would first consider west, then
east, then north, then south.

As a smaller example, consider just these five Elves:

.....
..##.
..#..
.....
..##.
.....

The northernmost two Elves and southernmost two Elves all propose moving north,
while the middle Elf cannot move north and proposes moving south. The middle
Elf proposes the same destination as the southwest Elf, so neither of them
move, but the other three do:

..##.
.....
..#..
...#.
..#..
.....

Next, the northernmost two Elves and the southernmost Elf all propose moving
south. Of the remaining middle two Elves, the west one cannot move south and
proposes moving west, while the east one cannot move south or west and proposes
moving east. All five Elves succeed in moving to their proposed positions:

.....
..##.
.#...
....#
.....
..#..

Finally, the southernmost two Elves choose not to move at all. Of the remaining
three Elves, the west one proposes moving west, the east one proposes moving
east, and the middle one proposes moving north; all three succeed in moving:

..#..
....#
#....
....#
.....
..#..

At this point, no Elves need to move, and so the process ends.

The larger example above proceeds as follows:

== Initial State ==
..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............

== End of Round 1 ==
..............
.......#......
.....#...#....
...#..#.#.....
.......#..#...
....#.#.##....
..#..#.#......
..#.#.#.##....
..............
....#..#......
..............
..............

== End of Round 2 ==
..............
.......#......
....#.....#...
...#..#.#.....
.......#...#..
...#..#.#.....
.#...#.#.#....
..............
..#.#.#.##....
....#..#......
..............
..............

== End of Round 3 ==
..............
.......#......
.....#....#...
..#..#...#....
.......#...#..
...#..#.#.....
.#..#.....#...
.......##.....
..##.#....#...
...#..........
.......#......
..............

== End of Round 4 ==
..............
.......#......
......#....#..
..#...##......
...#.....#.#..
.........#....
.#...###..#...
..#......#....
....##....#...
....#.........
.......#......
..............

== End of Round 5 ==
.......#......
..............
..#..#.....#..
.........#....
......##...#..
.#.#.####.....
...........#..
....##..#.....
..#...........
..........#...
....#..#......
..............

After a few more rounds...

== End of Round 10 ==
.......#......
...........#..
..#.#..#......
......#.......
...#.....#..#.
.#......##....
.....##.......
..#........#..
....#.#..#....
..............
....#..#..#...
..............

To make sure they're on the right track, the Elves like to check after round 10
that they're making good progress toward covering enough ground. To do this,
count the number of empty ground tiles contained by the smallest rectangle that
contains every Elf. (The edges of the rectangle should be aligned to the
N/S/E/W directions; the Elves do not have the patience to calculate arbitrary
rectangles.) In the above example, that rectangle is:

......#.....
..........#.
.#.#..#.....
.....#......
..#.....#..#
#......##...
....##......
.#........#.
...#.#..#...
............
...#..#..#..

In this region, the number of empty ground tiles is 110.

Simulate the Elves' process and find the smallest rectangle that contains the
Elves after 10 rounds. How many empty ground tiles does that rectangle contain?

--- Part Two ---

It seems you're on the right track. Finish simulating the process and figure
out where the Elves need to go. How many rounds did you save them?

In the example above, the first round where no Elf moved was round 20:

.......#......
....#......#..
..#.....#.....
......#.......
...#....#.#..#
#.............
....#.....#...
..#.....#.....
....#.#....#..
.........#....
....#......#..
.......#......

Figure out where the Elves need to go. What is the number of the first round
where no Elf moves?
"""

from collections import namedtuple
from enum import Enum


NUM_ROUNDS = 10

Coordinates = namedtuple("Coordinates", ["x", "y"])


class Direction(Enum):
    """The values are the vector/delta you can add to another `Coordinates` to
    move in that direction.
    """

    North = Coordinates(0, -1)
    East = Coordinates(1, 0)
    South = Coordinates(0, 1)
    West = Coordinates(-1, 0)


def parse_grove(lines: list[str]) -> set[Coordinates]:
    elves = set()

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char != "#":
                continue

            elves.add(Coordinates(x, y))

    return elves


# In order of which direction the elves will consider first
scan_directions = [
    Direction.North,
    Direction.South,
    Direction.West,
    Direction.East,
]

# grove = open("../puzzle-input/day23-example-input.txt").readlines()
grove = open("../puzzle-input/day23-input.txt").readlines()

elves = parse_grove(grove)

for round_number in range(1, 1_000_000):
    new_elf_positions: dict[Coordinates, Coordinates] = {}
    stationary_elves = set()

    for elf in elves:
        # First, check if all the adjacent positions next to this elf are free
        # at the moment
        alone = True
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue

                if Coordinates(elf.x + x, elf.y + y) in elves:
                    alone = False
                    break

            if not alone:
                break

        if alone:
            stationary_elves.add(elf)
            continue

        for direction in scan_directions:
            found_empty_spot = True

            for delta in [-1, 0, 1]:
                match direction:
                    case Direction.North:
                        coordinates_to_check = Coordinates(elf.x + delta, elf.y - 1)

                    case Direction.East:
                        coordinates_to_check = Coordinates(elf.x + 1, elf.y + delta)

                    case Direction.South:
                        coordinates_to_check = Coordinates(elf.x + delta, elf.y + 1)

                    case Direction.West:
                        coordinates_to_check = Coordinates(elf.x - 1, elf.y + delta)

                if coordinates_to_check in elves:
                    found_empty_spot = False
                    break

            if not found_empty_spot:
                continue

            new_position = Coordinates(
                elf.x + direction.value.x, elf.y + direction.value.y
            )

            if new_position in new_elf_positions:
                # Two elves want to move to the same spot, cancel both their
                # movements
                stationary_elves.add(new_elf_positions[new_position])
                stationary_elves.add(elf)
                del new_elf_positions[new_position]
            else:
                new_elf_positions[new_position] = elf

            break
        else:
            # Didn't find any empty spot to move to
            stationary_elves.add(elf)

    # Build a new list of elves with their (possibly updated) positions
    num_elves = len(elves)
    elves = set(new_elf_positions.keys())
    elves.update(stationary_elves)
    # Head count. Did we lose any elves?
    assert len(elves) == num_elves

    # Did anyone move?
    if not new_elf_positions:
        break

    # Rotate scan directions
    scan_directions = scan_directions[1:] + scan_directions[:1]

print(round_number)
