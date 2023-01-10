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

--- Part Two ---

You're worried that even with an optimal approach, the pressure released won't
be enough. What if you got one of the elephants to help you?

It would take you 4 minutes to teach an elephant how to open the right valves
in the right order, leaving you with only 26 minutes to actually execute your
plan. Would having two of you working together be better, even if it means
having less time? (Assume that you teach the elephant before opening any valves
yourself, giving you both the same full 26 minutes.)

In the example above, you could teach the elephant to help you as follows:

== Minute 1 ==
No valves are open.
You move to valve II.
The elephant moves to valve DD.

== Minute 2 ==
No valves are open.
You move to valve JJ.
The elephant opens valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You open valve JJ.
The elephant moves to valve EE.

== Minute 4 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve II.
The elephant moves to valve FF.

== Minute 5 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve AA.
The elephant moves to valve GG.

== Minute 6 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve BB.
The elephant moves to valve HH.

== Minute 7 ==
Valves DD and JJ are open, releasing 41 pressure.
You open valve BB.
The elephant opens valve HH.

== Minute 8 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve CC.
The elephant moves to valve GG.

== Minute 9 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve CC.
The elephant moves to valve FF.

== Minute 10 ==
Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
The elephant moves to valve EE.

== Minute 11 ==
Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
The elephant opens valve EE.

(At this point, all valves are open.)

== Minute 12 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

...

== Minute 20 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

...

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

With the elephant helping, after 26 minutes, the best you could do would
release a total of 1707 pressure.

With you and an elephant working together for 26 minutes, what is the most
pressure you could release?
"""

from collections import defaultdict, namedtuple
from copy import copy
from heapq import heappop, heappush


MAX_VALUE = 2**31 - 1

TIME_LIMIT = 26

Graph = dict[str, "Node"]
Matrix = dict[str, dict[str, int]]
State = namedtuple("State", ["agents", "closed_valves", "total_pressure_released"])
Agent = namedtuple("Agent", ["current_node", "time_passed", "pressure_release_rate"])


class Node:
    def __init__(self, name: str, flow_rate: int, edges: list[str]) -> None:
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


def find_max_releasable_pressure(graph: Graph, num_agents: int) -> int:
    distance_matrix = floyd_warshal(graph)

    closed_valves = set([valve for valve in graph if graph[valve].flow_rate > 0])
    initial_state = State(
        [Agent("AA", 0, 0) for _ in range(num_agents)], closed_valves, 0
    )
    queue = [(0, initial_state)]

    # Caches the best results (total pressure released + remaining release at
    # the current rate) that was achieved with a combination of opened valves.
    #
    # If a possible next step of an agent isn't providing a higher value with
    # the same combination of opened valves, it means it's lagging behind on a
    # better option.
    #
    # We can be sure it's a worse option because all agents start from the same
    # node and so it takes the same amount of time to open the same combination
    # of valves. So if a lower amount of released pressure is calculated for
    # the same set of opened valves, it means the agents opened them in a less
    # efficient order.
    #
    # In such cases stop following that branch by not executing the next step at all.
    #
    # This store is also used to determine the highest releasable pressure of all
    # options, which is the answer to the puzzle.
    best_results = defaultdict(int)

    while queue:
        _, state = heappop(queue)

        cache_key = frozenset(state.closed_valves)
        best_results[cache_key] = max(
            best_results[cache_key],
            state.total_pressure_released + pressure_release_remaining(state.agents),
        )

        # Make the next move with the agent that has the most time left
        current_agent = sorted(state.agents, key=lambda a: a.time_passed)[0]

        # For each unopened valve that offer some flow rate, simulate us going
        # there and opening that valve. While we're underway to that
        # destination valve the pressure released slowly ticks up.
        for destination_node in state.closed_valves:
            route_length = distance_matrix[current_agent.current_node][destination_node]

            # The time it takes us to get to the valve, plus 1 minute to open it
            next_time_passed = current_agent.time_passed + route_length + 1
            if next_time_passed >= TIME_LIMIT:
                # Time's up, we can't make it to the destination node in time,
                # so consider other options
                continue

            # Open the valve
            next_closed_valves = copy(state.closed_valves)
            next_closed_valves.remove(destination_node)

            next_total_released = state.total_pressure_released + (
                current_agent.pressure_release_rate * (route_length + 1)
            )
            next_release_rate = (
                current_agent.pressure_release_rate + graph[destination_node].flow_rate
            )

            agents = [agent for agent in state.agents if agent is not current_agent]
            agents.append(Agent(destination_node, next_time_passed, next_release_rate))

            # Should this branch stop and not open any more valves, how much
            # pressure will there be released?
            minimum_pressure_released = (
                next_total_released + pressure_release_remaining(agents)
            )
            if best_results[frozenset(next_closed_valves)] < minimum_pressure_released:
                next_step = State(agents, next_closed_valves, next_total_released)

                heappush(queue, (MAX_VALUE - minimum_pressure_released, next_step))

    return max(best_results.values())


def floyd_warshal(graph: Graph) -> Matrix:
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


def pressure_release_remaining(agents: list[Agent]) -> int:
    return sum(
        [
            (TIME_LIMIT - agent.time_passed) * agent.pressure_release_rate
            for agent in agents
        ]
    )


# tunnel_layout = open("../puzzle-input/day16-example-input.txt").readlines()
tunnel_layout = open("../puzzle-input/day16-input.txt").readlines()

graph = parse_tunnel_layout(tunnel_layout)

print(find_max_releasable_pressure(graph, num_agents=2))
