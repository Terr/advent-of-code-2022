"""
--- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted
carefully in a grid. The Elves explain that a previous expedition planted these
trees as a reforestation effort. Now, they're curious if this would be a good
location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house
hidden. To do this, you need to count the number of trees that are visible from
outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height
of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0
is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid
are shorter than it. Only consider trees in the same row or column; that is,
only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are
already on the edge, there are no trees to block the view. In this example,
that only leaves the interior nine trees to consider:

* The top-left 5 is visible from the left and top. (It isn't visible from the
  right or bottom since other trees of height 5 are in the way.)
* The top-middle 5 is visible from the top and right.
* The top-right 1 is not visible from any direction; for it to be visible,
  there would need to only be trees of height 0 between it and an edge.
* The left-middle 5 is visible, but only from the right.
* The center 3 is not visible from any direction; for it to be visible, there
  would need to be only trees of at most height 2 between it and an edge.
* The right-middle 3 is visible from the right.
* In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a
total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?

"""

from collections import namedtuple


Grid = namedtuple("Grid", ["dimension", "fields"])


def parse_grid(data: list[str]) -> Grid:
    data = list(map(lambda s: s.strip(), data))
    # Verify that the grid is indeed a square
    assert len(data[0]) == len(data)

    fields = "".join([line.strip() for line in data])

    return Grid(dimension=len(data), fields=fields)


def is_tree_visible(grid: Grid, column: int, row: int) -> bool:
    """
    To determine if the tree at the given column and row in the grid is
    visible, we have to look from all four sides of the grid. We can stop once
    we found one direction from which its visible.
    """

    row_index_start = row * grid.dimension
    row_index_end = row_index_start + (grid.dimension - 1)

    tree_index = row_index_start + column

    column_index_start = column
    column_index_end = (grid.dimension - 1) * grid.dimension + column

    # Format: (start index, stop index, step size)
    directions = [
        # From left to right
        (row_index_start, tree_index, +1),
        # From right to left
        (row_index_end, tree_index, -1),
        # From top to bottom
        (column_index_start, tree_index, grid.dimension),
        # From bottom to top
        (column_index_end, tree_index, -grid.dimension),
    ]

    tree_height = int(grid.fields[tree_index])
    for index_from, index_to, step_size in directions:
        found_taller_tree = False

        for index in range(index_from, index_to, step_size):
            if int(grid.fields[index]) >= tree_height:
                found_taller_tree = True
                break

        if not found_taller_tree:
            return True

    # The tree isn't visible from any of the directions
    return False


# grid = parse_grid(open("../puzzle-input/day8-example-input.txt").readlines())
grid = parse_grid(open("../puzzle-input/day8-input.txt").readlines())

num_visible = 0
for x in range(grid.dimension):
    for y in range(grid.dimension):
        if is_tree_visible(grid, x, y):
            num_visible += 1

print(num_visible)
