"""
--- Day 18: Boiling Boulders ---

You and the elephants finally reach fresh air. You've emerged near the base of
a large volcano that seems to be actively erupting! Fortunately, the lava seems
to be flowing away from you and toward the ocean.

Bits of lava are still being ejected toward you, so you're sheltering in the
cavern exit a little longer. Outside the cave, you can see the lava landing in
a pond and hear it loudly hissing as it solidifies.

Depending on the specific compounds in the lava and speed at which it cools, it
might be forming obsidian! The cooling rate should be based on the surface area
of the lava droplets, so you take a quick scan of a droplet as it flies past
you (your puzzle input).

Because of how quickly the lava is moving, the scan isn't very good; its
resolution is quite low and, as a result, it approximates the shape of the lava
droplet with 1x1x1 cubes on a 3D grid, each given as its x,y,z position.

To approximate the surface area, count the number of sides of each cube that
are not immediately connected to another cube. So, if your scan were only two
adjacent cubes like 1,1,1 and 2,1,1, each cube would have a single side covered
and five sides exposed, a total surface area of 10 sides.

Here's a larger example:

2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5

In the above example, after counting up all the sides that aren't connected to
another cube, the total surface area is 64.

What is the surface area of your scanned lava droplet?

--- Part Two ---

Something seems off about your calculation. The cooling rate depends on
exterior surface area, but your calculation also included the surface area of
air pockets trapped in the lava droplet.

Instead, consider only cube sides that could be reached by the water and steam
as the lava droplet tumbles into the pond. The steam will expand to reach as
much as possible, completely displacing any air on the outside of the lava
droplet but never expanding diagonally.

In the larger example above, exactly one cube of air is trapped within the lava
droplet (at 2,2,5), so the exterior surface area of the lava droplet is 58.

What is the exterior surface area of your scanned lava droplet?
"""

from collections import deque, namedtuple
from heapq import heappush, heappop


Coordinate = namedtuple("Coordinate", ["x", "y", "z"])

ADJACENT_COORDINATES = [
    (0, -1, 0),
    (0, +1, 0),
    (-1, 0, 0),
    (+1, 0, 0),
    (0, 0, -1),
    (0, 0, +1),
]

AREA_SIZE = 22


def is_reachable_astar(cubes, from_: Coordinate, to_: Coordinate) -> bool:
    queue = []
    heappush(queue, (0, from_))

    cost_so_far = {from_: 0}

    while queue:
        _, current = heappop(queue)

        if (
            (current.x == -1 or current.x == AREA_SIZE)
            or (current.y == -1 or current.y == AREA_SIZE)
            or (current.z == -1 or current.z == AREA_SIZE)
        ):
            return True

        for next_x, next_y, next_z in ADJACENT_COORDINATES:
            neighbor_cell = Coordinate(
                current.x + next_x, current.y + next_y, current.z + next_z
            )
            if not (
                -1 <= neighbor_cell.x <= AREA_SIZE
                and -1 <= neighbor_cell.y <= AREA_SIZE
                and -1 <= neighbor_cell.z <= AREA_SIZE
            ):
                # Don't go out of bounds
                continue

            if neighbor_cell in cubes:
                # This cell is filled with a lava cube
                continue

            new_cost = cost_so_far[current] + 1

            if (
                neighbor_cell not in cost_so_far
                or new_cost < cost_so_far[neighbor_cell]
            ):
                cost_so_far[neighbor_cell] = new_cost

                priority = new_cost + manhattan_distance(neighbor_cell, to_)
                heappush(queue, (priority, neighbor_cell))

    return False


def manhattan_distance(from_: Coordinate, to_: Coordinate) -> int:
    return abs(from_.x - to_.x) + abs(from_.y - to_.y) + abs(from_.z - from_.z)


def is_reachable_bfs(cubes, from_: Coordinate) -> bool:
    visited = {from_}
    queue = deque([from_])

    while queue:
        current = queue.popleft()

        if (
            (current.x == -1 or current.x == AREA_SIZE)
            or (current.y == -1 or current.y == AREA_SIZE)
            or (current.z == -1 or current.z == AREA_SIZE)
        ):
            return True

        for next_x, next_y, next_z in ADJACENT_COORDINATES:
            edge_node = Coordinate(
                current.x + next_x, current.y + next_y, current.z + next_z
            )

            if not (
                -1 <= edge_node.x <= AREA_SIZE
                and -1 <= edge_node.y <= AREA_SIZE
                and -1 <= edge_node.z <= AREA_SIZE
            ):
                # Don't go out of bounds
                continue

            if edge_node in cubes:
                # This cell is filled with a lava cube
                continue

            if edge_node not in visited:
                queue.append(edge_node)
                visited.add(edge_node)

    return False


def is_reachable_dfs(cubes, from_: Coordinate) -> bool:
    visited = {from_}
    queue = [from_]

    while queue:
        current = queue.pop()

        # If we can reach a border of the area it means we reached outside air
        if (
            (current.x == -1 or current.x == AREA_SIZE)
            or (current.y == -1 or current.y == AREA_SIZE)
            or (current.z == -1 or current.z == AREA_SIZE)
        ):
            return True

        for next_x, next_y, next_z in ADJACENT_COORDINATES:
            edge_node = Coordinate(
                current.x + next_x, current.y + next_y, current.z + next_z
            )

            if not (
                -1 <= edge_node.x <= AREA_SIZE
                and -1 <= edge_node.y <= AREA_SIZE
                and -1 <= edge_node.z <= AREA_SIZE
            ):
                # Don't go out of bounds
                continue

            if edge_node in cubes:
                # This cell is filled with a lava cube
                continue

            if edge_node not in visited:
                queue.append(edge_node)
                visited.add(edge_node)

    return False


# scan_data = open("../puzzle-input/day18-example-input.txt").readlines()
scan_data = open("../puzzle-input/day18-input.txt").readlines()

cubes = set()

for line in scan_data:
    x, y, z = map(int, line.strip().split(","))
    cubes.add(Coordinate(x, y, z))

exterior_surfaces_exposed = 0
for cube in cubes:
    for x, y, z in ADJACENT_COORDINATES:
        test_coordinate = Coordinate(cube[0] + x, cube[1] + y, cube[2] + z)

        # Create a coordinate of what is certainly 'outside air' and likely to be
        # close (Manhattan distance-wise) to the cube under test
        goal = Coordinate(-1, cube.y, cube.z)

        # if test_coordinate not in cubes and is_reachable_astar(cubes, test_coordinate, goal):
        # if test_coordinate not in cubes and is_reachable_bfs(cubes, test_coordinate):
        if test_coordinate not in cubes and is_reachable_dfs(cubes, test_coordinate):
            exterior_surfaces_exposed += 1

print(exterior_surfaces_exposed)
