"""
--- Day 15: Beacon Exclusion Zone ---

You feel the ground rumble again as the distress signal leads you to a large
network of subterranean tunnels. You don't have time to search them all, but
you don't need to: your pack contains a set of deployable sensors that you
imagine were originally built to locate lost Elves.

The sensors aren't very powerful, but that's okay; your handheld device
indicates that you're close enough to the source of the distress signal to use
them. You pull the emergency sensor system out of your pack, hit the big button
on top, and the sensors zoom off down the tunnels.

Once a sensor finds a spot it thinks will give it a good reading, it attaches
itself to a hard surface and begins monitoring for the nearest signal source
beacon. Sensors and beacons always exist at integer coordinates. Each sensor
knows its own position and can determine the position of a beacon precisely;
however, sensors can only lock on to the one beacon closest to the sensor as
measured by the Manhattan distance. (There is never a tie where two beacons are
the same distance to a sensor.)

It doesn't take long for the sensors to report back their positions and closest
beacons (your puzzle input). For example:

Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3

So, consider the sensor at 2,18; the closest beacon to it is at -2,15. For the
sensor at 9,16, the closest beacon to it is at 10,16.

Drawing sensors as S and beacons as B, the above arrangement of sensors and
beacons looks like this:

               1    1    2    2
     0    5    0    5    0    5
 0 ....S.......................
 1 ......................S.....
 2 ...............S............
 3 ................SB..........
 4 ............................
 5 ............................
 6 ............................
 7 ..........S.......S.........
 8 ............................
 9 ............................
10 ....B.......................
11 ..S.........................
12 ............................
13 ............................
14 ..............S.......S.....
15 B...........................
16 ...........SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....

This isn't necessarily a comprehensive map of all beacons in the area, though.
Because each sensor only identifies its closest beacon, if a sensor detects a
beacon, you know there are no other beacons that close or closer to that
sensor. There could still be beacons that just happen to not be the closest
beacon to any sensor. Consider the sensor at 8,7:

               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....

This sensor's closest beacon is at 2,10, and so you know there are no beacons
that close or closer (in any positions marked #).

None of the detected beacons seem to be producing the distress signal, so
you'll need to work out where the distress beacon is by working out where it
isn't. For now, keep things simple by counting the positions where a beacon
cannot possibly be along just a single row.

So, suppose you have an arrangement of beacons and sensors like in the example
above and, just in the row where y=10, you'd like to count the number of
positions a beacon cannot possibly exist. The coverage from all sensors near
that row looks like this:

                 1    1    2    2
       0    5    0    5    0    5
 9 ...#########################...
10 ..####B######################..
11 .###S#############.###########.

In this example, in the row where y=10, there are 26 positions where a beacon
cannot be present.

Consult the report from the sensors you just deployed. In the row where
y=2000000, how many positions cannot contain a beacon?
"""

from collections import namedtuple


Coordinate = namedtuple("Coordinate", ["x", "y"])


def manhattan_distance(from_: Coordinate, to_: Coordinate) -> int:
    return abs(from_.x - to_.x) + abs(from_.y - to_.y)


def parse_sensor_list(
    lines: list[str],
) -> tuple[list[tuple[Coordinate, int]], list[Coordinate]]:
    """Parses the puzzle input and gives back two lists:

    * A list of Sensor coordinates and the Manhattan distance to their closest
      beacon.
    * A list of coordinates of the Beacons
    """
    # Format: [(Coordinate, manhattan_distance)]
    sensors = []
    beacons = []

    for line in lines:
        words = line.strip().split()

        # Create integer out of 'x=1,'
        sensor_x = int(words[2].split("=")[1][:-1])
        # Create integer out of 'y=2:'
        sensor_y = int(words[3].split("=")[1][:-1])
        sensor = Coordinate(sensor_x, sensor_y)

        # Create integer out of 'x=1,'
        beacon_x = int(words[8].split("=")[1][:-1])
        # Create integer out of 'y=2'
        beacon_y = int(words[9].split("=")[1])
        beacon = Coordinate(beacon_x, beacon_y)

        sensors.append((sensor, manhattan_distance(sensor, beacon)))
        beacons.append(beacon)

    return sensors, beacons


def find_gap(
    sensors: list[tuple[Coordinate, int]], row_y: int, coverage_range_limit: int
) -> None | int:
    coverage_range_x = range(0, coverage_range_limit + 1)

    intervals = []
    for sensor, distance in sensors:
        # Can the coverage of this sensor reach the row we're interested in at all?
        if not sensor.y - distance <= row_y <= sensor.y + distance:
            continue

        # Taking the steps from the sensor's Y position needed to get to the
        # monitored row into account, what X coordinates of that row are being
        # covered by the sensor?
        distance_needed = abs(sensor.y - row_y)
        coverage_left = abs(distance - distance_needed)
        from_x = max(coverage_range_x.start, -coverage_left + sensor.x)
        to_x = min(coverage_range_x.stop, coverage_left + sensor.x)

        intervals.append(range(from_x, to_x))

    # We sort the intervals so we can then compare them in order from left to right
    intervals.sort(key=lambda i: i.start)

    max_x = -1
    for interval in intervals:
        if interval.start > max_x + 1:
            # A gap was detected
            return max_x + 1

        max_x = max(max_x, interval.stop)


# sensor_list = open("../puzzle-input/day15-example-input.txt").readlines()
# coverage_range_limit = 20

sensor_list = open("../puzzle-input/day15-input.txt").readlines()
coverage_range_limit = 4_000_000

sensors, beacons = parse_sensor_list(sensor_list)

min_y = 0
max_y = coverage_range_limit
coverage_range_y = range(min_y, max_y + 1)

for row_to_monitor in coverage_range_y:
    if (gap_x := find_gap(sensors, row_to_monitor, coverage_range_limit)) is not None:
        tuning_frequency = 4_000_000 * gap_x + row_to_monitor
        print(tuning_frequency)
        break
