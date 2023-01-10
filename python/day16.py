"""
--- Day 16: Proboscidea Volcanium ---

The sensors have led you to the origin of the distress signal: yet another
handheld device, just like the one the Elves gave you. However, you don't see
any Elves around; instead, the device is surrounded by elephants! They must
have gotten lost in these tunnels, and one of the elephants apparently figured
out how to turn on the distress signal.

The ground rumbles again, much stronger this time. What kind of cave is this,
exactly? You scan the cave with your handheld device; it reports mostly igneous
rock, some ash, pockets of pressurized gas, magma... this isn't just a cave,
it's a volcano!

You need to get the elephants out of here, quickly. Your device estimates that
you have 30 minutes before the volcano erupts, so you don't have time to go
back out the way you came in.

You scan the cave for other options and discover a network of pipes and
pressure-release valves. You aren't sure how such a system got into a volcano,
but you don't have time to complain; your device produces a report (your puzzle
input) of each valve's flow rate if it were opened (in pressure per minute) and
the tunnels you could use to move between the valves.

There's even a valve in the room you and the elephants are currently standing
in labeled AA. You estimate it will take you one minute to open a single valve
and one minute to follow any tunnel from one valve to another. What is the most
pressure you could release?

For example, suppose you had the following scan output:

Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II

All of the valves begin closed. You start at valve AA, but it must be damaged
or jammed or something: its flow rate is 0, so there's no point in opening it.
However, you could spend one minute moving to valve BB and another minute
opening it; doing so would release pressure during the remaining 28 minutes at
a flow rate of 13, a total eventual pressure release of 28 * 13 = 364. Then,
you could spend your third minute moving to valve CC and your fourth minute
opening it, providing an additional 26 minutes of eventual pressure release at
a flow rate of 2, or 52 total pressure released by valve CC.

Making your way through the tunnels like this, you could probably open many or
all of the valves by the time 30 minutes have elapsed. However, you need to
release as much pressure as possible, so you'll need to be methodical. Instead,
consider this approach:

== Minute 1 ==
No valves are open.
You move to valve DD.

== Minute 2 ==
No valves are open.
You open valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You move to valve CC.

== Minute 4 ==
Valve DD is open, releasing 20 pressure.
You move to valve BB.

== Minute 5 ==
Valve DD is open, releasing 20 pressure.
You open valve BB.

== Minute 6 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve AA.

== Minute 7 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve II.

== Minute 8 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve JJ.

== Minute 9 ==
Valves BB and DD are open, releasing 33 pressure.
You open valve JJ.

== Minute 10 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve II.

== Minute 11 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve AA.

== Minute 12 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve DD.

== Minute 13 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve EE.

== Minute 14 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve FF.

== Minute 15 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve GG.

== Minute 16 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve HH.

== Minute 17 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You open valve HH.

== Minute 18 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve GG.

== Minute 19 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve FF.

== Minute 20 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve EE.

== Minute 21 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve EE.

== Minute 22 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve DD.

== Minute 23 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve CC.

== Minute 24 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You open valve CC.

== Minute 25 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 27 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 28 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 29 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 30 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

This approach lets you release the most pressure possible in 30 minutes with
this valve layout, 1651.

Work out the steps to release the most pressure in 30 minutes. What is the most
pressure you can release?
"""

from collections import defaultdict, deque, namedtuple
from copy import copy


MAX_VALUE = 2**31 - 1

TIME_LIMIT = 30

Graph = dict[str, "Node"]
Matrix = dict[str, dict[str, int]]
State = namedtuple(
    "State",
    [
        "current_node",
        "closed_valves",
        "time_passed",
        "pressure_release_rate",
        "total_pressure_released",
    ],
)


class Node:
    def __init__(self, name: str, flow_rate: int, edges: list[str]):
        self.name = name
        self.flow_rate = flow_rate
        self.edges = edges

    def __str__(self) -> str:
        return self.name


def parse_tunnel_layout(lines: list[str]) -> dict[str, Node]:
    # Format: [valve name]: flow rate
    graph = {}

    for line in lines:
        parts = line.split()

        valve = parts[1]
        flow_rate = int(parts[4].split("=")[1][:-1])
        edges = [edge[:2] for edge in parts[9:]]

        graph[valve] = Node(valve, flow_rate, edges)

    return graph


def find_max_releasable_pressure(graph: Graph) -> int:
    distance_matrix = floyd_warshal(graph)

    closed_valves = set([valve for valve in graph if graph[valve].flow_rate > 0])

    queue = deque([State("AA", closed_valves, 0, 0, 0)])
    highest_pressure_released = 0
    while queue:
        step = queue.popleft()
        current_node = step.current_node

        # If we would stop here and let time run out, how much pressed will there be
        # released at the time limit?
        idle_pressure_released = step.total_pressure_released + (
            (TIME_LIMIT - step.time_passed) * step.pressure_release_rate
        )
        highest_pressure_released = max(
            highest_pressure_released, idle_pressure_released
        )

        for destination_node in step.closed_valves:
            # For each unopened valve that offer some flow rate, simulate us going
            # there and opening that valve. While we're underway to that
            # destination valve the pressure released slowly ticks up.

            route_length = distance_matrix[current_node][destination_node]

            # The time it takes us to get to the valve, plus 1 minute to open it
            next_time_passed = step.time_passed + route_length + 1
            if next_time_passed >= TIME_LIMIT:
                # Time's up, we can't make it to the destination node in time.
                continue

            # Open the valve
            next_closed_valves = copy(step.closed_valves)
            next_closed_valves.remove(destination_node)

            next_release_rate = (
                step.pressure_release_rate + graph[destination_node].flow_rate
            )
            next_total_released = step.total_pressure_released + (
                step.pressure_release_rate * (route_length + 1)
            )

            next_step = State(
                destination_node,
                next_closed_valves,
                next_time_passed,
                next_release_rate,
                next_total_released,
            )
            queue.appendleft(next_step)

    return highest_pressure_released


def floyd_warshal(graph: dict[str, Node]) -> Matrix:
    matrix: Matrix = defaultdict(lambda: defaultdict(lambda: MAX_VALUE))

    # Create adjacency matrix
    for name, node in graph.items():
        matrix[name][name] = 0
        for edge in node.edges:
            # Every edge in this graph has a length of 1
            matrix[name][edge] = 1

    # Do the Floyd-Warshal
    for k in graph:
        for i in graph:
            for j in graph:
                through_k = matrix[i][k] + matrix[k][j]
                if through_k < matrix[i][j]:
                    matrix[i][j] = through_k

    return matrix


# tunnel_layout = open("../puzzle-input/day16-example-input.txt").readlines()
tunnel_layout = open("../puzzle-input/day16-input.txt").readlines()

graph = parse_tunnel_layout(tunnel_layout)

print(find_max_releasable_pressure(graph))


# def dijkstra(graph: dict[str, Node], start_node: str):
#     edge_length = 1
#
#     in_tree = set()
#     parents = {start_node: None}
#
#     distances = defaultdict(lambda: MAXINT)
#     distances[start_node] = 0
#
#     current_node = start_node
#     while current_node not in in_tree:
#         in_tree.add(current_node)
#
#         for to_node in graph[current_node].edges:
#             # if distances[current_node] + edge_length < distances[to_node] and to_node not in in_tree:
#             if distances[current_node] + edge_length < distances[to_node]:
#                 distances[to_node] = distances[current_node] + edge_length
#                 parents[to_node] = current_node
#
#         shortest_distance = MAXINT
#         for node in graph:
#             if node not in in_tree and distances[node] < shortest_distance:
#                 shortest_distance = distances[node]
#                 current_node = node
#
#     # Proof that all nodes were visited
#     assert len(in_tree) == len(graph)
#     assert len(parents) == len(graph)
#
#     return distances, parents


# def inverse_prim(graph: dict[str, Node], start_node: str):
#     """
#     Prim's algorithm but instead of looking for the lowest weight, look for
#     the paths that lead to nodes that release the most pressure.
#     """
#
#     benefits = defaultdict(lambda: -1)
#     benefits[start_node] = 0
#
#     parents = {start_node: None}
#
#     in_tree = set()
#     current_node = start_node
#     while current_node not in in_tree:
#         in_tree.add(current_node)
#
#         for to_node in graph[current_node].edges:
#             if graph[to_node].flow_rate > benefits[to_node] and to_node not in in_tree:
#                 benefits[to_node] = graph[to_node].flow_rate
#                 parents[to_node] = current_node
#
#         highest_benefit = -1
#         for node in graph:
#             if node not in in_tree and benefits[node] > highest_benefit:
#                 highest_benefit = benefits[node]
#                 current_node = node
#
#     # Proof that all nodes were visited
#     assert len(in_tree) == len(graph)
#     assert len(parents) == len(graph)
#
#     return benefits, parents
