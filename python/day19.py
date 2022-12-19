"""
--- Day 19: Not Enough Minerals ---

Your scans show that the lava did indeed form obsidian!

The wind has changed direction enough to stop sending lava droplets toward you,
so you and the elephants exit the cave. As you do, you notice a collection of
geodes around the pond. Perhaps you could use the obsidian to create some
geode-cracking robots and break them open?

To collect the obsidian from the bottom of the pond, you'll need waterproof
obsidian-collecting robots. Fortunately, there is an abundant amount of clay
nearby that you can use to make them waterproof.

In order to harvest the clay, you'll need special-purpose clay-collecting
robots. To make any type of robot, you'll need ore, which is also plentiful but
in the opposite direction from the clay.

Collecting ore requires ore-collecting robots with big drills. Fortunately, you
have exactly one ore-collecting robot in your pack that you can use to
kickstart the whole operation.

Each robot can collect 1 of its resource type per minute. It also takes one
minute for the robot factory (also conveniently from your pack) to construct
any type of robot, although it consumes the necessary resources available when
construction begins.

The robot factory has many blueprints (your puzzle input) you can choose from,
but once you've configured it with a blueprint, you can't change it. You'll
need to work out which blueprint is best.

For example:

Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.

(Blueprints have been line-wrapped here for legibility. The robot factory's
actual assortment of blueprints are provided one blueprint per line.)

The elephants are starting to look hungry, so you shouldn't take too long; you
need to figure out which blueprint would maximize the number of opened geodes
after 24 minutes by figuring out which robots to build and when to build them.

Using blueprint 1 in the example above, the largest number of geodes you could
open in 24 minutes is 9. One way to achieve that is:

== Minute 1 ==
1 ore-collecting robot collects 1 ore; you now have 1 ore.

== Minute 2 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.

== Minute 3 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
The new clay-collecting robot is ready; you now have 1 of them.

== Minute 4 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
1 clay-collecting robot collects 1 clay; you now have 1 clay.

== Minute 5 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
1 clay-collecting robot collects 1 clay; you now have 2 clay.
The new clay-collecting robot is ready; you now have 2 of them.

== Minute 6 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
2 clay-collecting robots collect 2 clay; you now have 4 clay.

== Minute 7 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
2 clay-collecting robots collect 2 clay; you now have 6 clay.
The new clay-collecting robot is ready; you now have 3 of them.

== Minute 8 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
3 clay-collecting robots collect 3 clay; you now have 9 clay.

== Minute 9 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
3 clay-collecting robots collect 3 clay; you now have 12 clay.

== Minute 10 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
3 clay-collecting robots collect 3 clay; you now have 15 clay.

== Minute 11 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 2 ore.
3 clay-collecting robots collect 3 clay; you now have 4 clay.
The new obsidian-collecting robot is ready; you now have 1 of them.

== Minute 12 ==
Spend 2 ore to start building a clay-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
3 clay-collecting robots collect 3 clay; you now have 7 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
The new clay-collecting robot is ready; you now have 4 of them.

== Minute 13 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 11 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.

== Minute 14 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 15 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 3 obsidian.

== Minute 15 ==
Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
1 ore-collecting robot collects 1 ore; you now have 1 ore.
4 clay-collecting robots collect 4 clay; you now have 5 clay.
1 obsidian-collecting robot collects 1 obsidian; you now have 4 obsidian.
The new obsidian-collecting robot is ready; you now have 2 of them.

== Minute 16 ==
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 9 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.

== Minute 17 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 13 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.

== Minute 18 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
1 ore-collecting robot collects 1 ore; you now have 2 ore.
4 clay-collecting robots collect 4 clay; you now have 17 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 3 obsidian.
The new geode-cracking robot is ready; you now have 1 of them.

== Minute 19 ==
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 21 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 5 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 1 open geode.

== Minute 20 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
4 clay-collecting robots collect 4 clay; you now have 25 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 7 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.

== Minute 21 ==
Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
1 ore-collecting robot collects 1 ore; you now have 3 ore.
4 clay-collecting robots collect 4 clay; you now have 29 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 2 obsidian.
1 geode-cracking robot cracks 1 geode; you now have 3 open geodes.
The new geode-cracking robot is ready; you now have 2 of them.

== Minute 22 ==
1 ore-collecting robot collects 1 ore; you now have 4 ore.
4 clay-collecting robots collect 4 clay; you now have 33 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 5 open geodes.

== Minute 23 ==
1 ore-collecting robot collects 1 ore; you now have 5 ore.
4 clay-collecting robots collect 4 clay; you now have 37 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 7 open geodes.

== Minute 24 ==
1 ore-collecting robot collects 1 ore; you now have 6 ore.
4 clay-collecting robots collect 4 clay; you now have 41 clay.
2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
2 geode-cracking robots crack 2 geodes; you now have 9 open geodes.

However, by using blueprint 2 in the example above, you could do even better:
the largest number of geodes you could open in 24 minutes is 12.

Determine the quality level of each blueprint by multiplying that blueprint's
ID number with the largest number of geodes that can be opened in 24 minutes
using that blueprint. In this example, the first blueprint has ID 1 and can
open 9 geodes, so its quality level is 9. The second blueprint has ID 2 and can
open 12 geodes, so its quality level is 24. Finally, if you add up the quality
levels of all of the blueprints in the list, you get 33.

Determine the quality level of each blueprint using the largest number of
geodes it could produce in 24 minutes. What do you get if you add up the
quality level of all of the blueprints in your list?
"""

from collections import namedtuple, deque, OrderedDict, defaultdict
from copy import copy, deepcopy
from enum import Enum
from itertools import repeat, count


class Resource(Enum):
    Ore = 1
    Clay = 2
    Obsidian = 3
    Geode = 4


class Bot(Enum):
    Ore = 1
    Clay = 2
    Obsidian = 3
    Geode = 4


Cost = namedtuple("Cost", ["ore", "clay", "obsidian"])
Blueprint = dict[Bot, Cost]


class RobotFactory:
    def __init__(self, blueprint: Blueprint):
        self.blueprint = blueprint
        self.resources = OrderedDict(zip(list(Resource), repeat(0)))

    def deposit(self, resource: Resource, amount: int):
        self.resources[resource] += amount

    def can_build(self, bot: Bot) -> bool:
        cost = self.blueprint[bot]

        return (
            self.resources[Resource.Ore] >= cost.ore
            and self.resources[Resource.Clay] >= cost.clay
            and self.resources[Resource.Obsidian] >= cost.obsidian
        )

    def build(self, bot: Bot):
        if not self.can_build(bot):
            raise Exception("Not enough materials to build %s bot!", bot)

        cost = self.blueprint[bot]

        self.use(Resource.Ore, cost.ore)
        self.use(Resource.Clay, cost.clay)
        self.use(Resource.Obsidian, cost.obsidian)

    def use(self, resource: Resource, amount: int):
        if amount > self.resources[resource]:
            raise Exception("Insufficient materials!")

        self.resources[resource] -= amount


def parse_blueprints(lines: list[str]) -> list[Blueprint]:
    blueprints = []

    for line in lines:
        parts = line.split()
        blueprints.append(
            {
                Bot.Ore: Cost(int(parts[6]), 0, 0),
                Bot.Clay: Cost(int(parts[12]), 0, 0),
                Bot.Obsidian: Cost(int(parts[18]), int(parts[21]), 0),
                Bot.Geode: Cost(int(parts[27]), 0, int(parts[30])),
            }
        )

    return blueprints


def do_blueprint_run(blueprint: Blueprint) -> int:
    factory = RobotFactory(blueprint)
    bots = OrderedDict(
        [
            (Bot.Ore, 1),
            (Bot.Clay, 0),
            (Bot.Obsidian, 0),
            (Bot.Geode, 0),
        ]
    )

    # Since we can only construct 1 bot per minute, it's no use to produce more
    # of a resource than is needed by even the most expensive both. Find the
    # highest cost for each resource.
    max_ore = max([costs.ore for costs in factory.blueprint.values()])
    max_clay = max([costs.clay for costs in factory.blueprint.values()])
    max_obsidian = max([costs.obsidian for costs in factory.blueprint.values()])

    minutes_remaining = 24
    queue = deque([(factory, bots, minutes_remaining)])

    max_geodes_cracked = 0
    best_geode_count_at_time = defaultdict(int)

    seen = set()

    while queue:
        factory, bots, minutes_remaining = queue.pop()

        # Don't process paths we already ended up at before
        seen_key = (
            minutes_remaining,
            tuple(factory.resources.values()),
            tuple(bots.values()),
        )
        if seen_key in seen:
            continue
        seen.add(seen_key)

        if minutes_remaining == 0:
            max_geodes_cracked = max(
                max_geodes_cracked, factory.resources[Resource.Geode]
            )
            continue

        # Can this path still catch up the highest geode score so far, even
        # if it would build 1 Geode bot per minute from now on?
        if max_geodes_cracked > factory.resources[Resource.Geode] + (
            bots[Bot.Geode] * minutes_remaining
        ) + sum(range(minutes_remaining)):
            continue

        # Build additional bot, if possible
        buildable_bots = []

        # Always build a Geode bot if possible
        if factory.can_build(Bot.Geode):
            buildable_bots.append(Bot.Geode)
        else:
            # Build the following bots only if the current mining rate and
            # storage is not enough to build that bot every minute from now
            # on
            if factory.can_build(Bot.Obsidian) and not (
                bots[Bot.Obsidian] * minutes_remaining
                + factory.resources[Resource.Obsidian]
                >= minutes_remaining * max_obsidian
            ):
                buildable_bots.append(Bot.Obsidian)

            if factory.can_build(Bot.Clay) and not (
                bots[Bot.Clay] * minutes_remaining + factory.resources[Resource.Clay]
                >= minutes_remaining * max_clay
            ):
                buildable_bots.append(Bot.Clay)

            if factory.can_build(Bot.Ore) and not (
                bots[Bot.Ore] * minutes_remaining + factory.resources[Resource.Ore]
                >= minutes_remaining * max_ore
            ):
                buildable_bots.append(Bot.Ore)

        # Collect resources
        factory.deposit(Resource.Ore, bots[Bot.Ore])
        factory.deposit(Resource.Clay, bots[Bot.Clay])
        factory.deposit(Resource.Obsidian, bots[Bot.Obsidian])
        factory.deposit(Resource.Geode, bots[Bot.Geode])

        # Stop following this path if there have been others who collected
        # more geodes by now.
        #
        # I don't think this assumption always holds because couldn't an
        # army of Geode bots later on catch up? But this pruning method
        # seems to work well for our short runtime of 24 steps/minutes
        if (
            best_geode_count_at_time[minutes_remaining]
            > factory.resources[Resource.Geode]
        ):
            continue
        best_geode_count_at_time[minutes_remaining] = factory.resources[Resource.Geode]

        # One path that we can always take is not building any bot at this time
        queue.append((factory, bots, minutes_remaining - 1))

        # Each bot that can be built signifies a new route that we can take.
        for bot in buildable_bots:
            next_factory = deepcopy(factory)
            next_bots = copy(bots)

            next_factory.build(bot)
            next_bots[bot] += 1

            queue.append((next_factory, next_bots, minutes_remaining - 1))

    return max_geodes_cracked


# puzzle_input = open("../puzzle-input/day19-example-input.txt").readlines()
puzzle_input = open("../puzzle-input/day19-input.txt").readlines()

blueprints = zip(count(start=1), parse_blueprints(puzzle_input))

total_quality_score = 0
for id_, blueprint in blueprints:
    geodes_cracked = do_blueprint_run(blueprint)

    print(f"Blueprint {id_}: {geodes_cracked} geodes cracked")

    total_quality_score += geodes_cracked * id_

print(total_quality_score)
