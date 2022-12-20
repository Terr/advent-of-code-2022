"""
--- Day 20: Grove Positioning System ---

It's finally time to meet back up with the Elves. When you try to contact them,
however, you get no reply. Perhaps you're out of range?

You know they're headed to the grove where the star fruit grows, so if you can
figure out where that is, you should be able to meet back up with them.

Fortunately, your handheld device has a file (your puzzle input) that contains
the grove's coordinates! Unfortunately, the file is encrypted - just in case
the device were to fall into the wrong hands.

Maybe you can decrypt it?

When you were still back at the camp, you overheard some Elves talking about
coordinate file encryption. The main operation involved in decrypting the file
is called mixing.

The encrypted file is a list of numbers. To mix the file, move each number
forward or backward in the file a number of positions equal to the value of the
number being moved. The list is circular, so moving a number off one end of the
list wraps back around to the other end as if the ends were connected.

For example, to move the 1 in a sequence like 4, 5, 6, 1, 7, 8, 9, the 1 moves
one position forward: 4, 5, 6, 7, 1, 8, 9. To move the -2 in a sequence like 4,
-2, 5, 6, 7, 8, 9, the -2 moves two positions backward, wrapping around: 4, 5,
6, 7, 8, -2, 9.

The numbers should be moved in the order they originally appear in the
encrypted file. Numbers moving around during the mixing process do not change
the order in which the numbers are moved.

Consider this encrypted file:

1
2
-3
3
-2
0
4

Mixing this file proceeds as follows:

Initial arrangement:
1, 2, -3, 3, -2, 0, 4

1 moves between 2 and -3:
2, 1, -3, 3, -2, 0, 4

2 moves between -3 and 3:
1, -3, 2, 3, -2, 0, 4

-3 moves between -2 and 0:
1, 2, 3, -2, -3, 0, 4

3 moves between 0 and 4:
1, 2, -2, -3, 0, 3, 4

-2 moves between 4 and 1:
1, 2, -3, 0, 3, 4, -2

0 does not move:
1, 2, -3, 0, 3, 4, -2

4 moves between -3 and 0:
1, 2, -3, 4, 0, 3, -2

Then, the grove coordinates can be found by looking at the 1000th, 2000th, and
3000th numbers after the value 0, wrapping around the list as necessary. In the
above example, the 1000th number after 0 is 4, the 2000th is -3, and the 3000th
is 2; adding these together produces 3.

Mix your encrypted file exactly once. What is the sum of the three numbers that
form the grove coordinates?
"""

from collections import deque
from copy import copy
from itertools import count


# encrypted_coordinates = list(map(int, open("../puzzle-input/day20-example-input.txt").readlines()))
encrypted_coordinates = list(
    map(int, open("../puzzle-input/day20-input.txt").readlines())
)

num_encrypted_coordinates = len(encrypted_coordinates)
shift_values = copy(encrypted_coordinates)
mixed_coordinates = deque(list(zip(count(), encrypted_coordinates)))

for original_index, shift_by in enumerate(shift_values):
    if shift_by == 0:
        continue

    entry = (original_index, shift_by)

    mixed_position = mixed_coordinates.index(entry)
    new_index = (mixed_position + shift_by) % (num_encrypted_coordinates - 1)
    if new_index == 0:
        new_index = num_encrypted_coordinates - 1

    mixed_coordinates.remove(entry)
    mixed_coordinates.rotate(-new_index)
    mixed_coordinates.appendleft(entry)
    mixed_coordinates.rotate(new_index)

    if num_encrypted_coordinates == 7:
        numbers = [n[1] for n in mixed_coordinates]
        print(numbers)


numbers = [n[1] for n in mixed_coordinates]
zero_index = numbers.index(0)
num_1k = numbers[(zero_index + 1000) % num_encrypted_coordinates]
num_2k = numbers[(zero_index + 2000) % num_encrypted_coordinates]
num_3k = numbers[(zero_index + 3000) % num_encrypted_coordinates]

print(num_1k + num_2k + num_3k)
