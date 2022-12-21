"""
--- Day 21: Monkey Math ---

The monkeys are back! You're worried they're going to try to steal your stuff
again, but it seems like they're just holding their ground and making various
monkey noises at you.

Eventually, one of the elephants realizes you don't speak monkey and comes over
to interpret. As it turns out, they overheard you talking about trying to find
the grove; they can show you a shortcut if you answer their riddle.

Each monkey is given a job: either to yell a specific number or to yell the
result of a math operation. All of the number-yelling monkeys know their number
from the start; however, the math operation monkeys need to wait for two other
monkeys to yell a number, and those two other monkeys might also be waiting on
other monkeys.

Your job is to work out the number the monkey named root will yell before the
monkeys figure it out themselves.

For example:

root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32

Each line contains the name of a monkey, a colon, and then the job of that
monkey:

* A lone number means the monkey's job is simply to yell that number.
* A job like aaaa + bbbb means the monkey waits for monkeys aaaa and bbbb to
  yell each of their numbers; the monkey then yells the sum of those two
  numbers.
* aaaa - bbbb means the monkey yells aaaa's number minus bbbb's number.
* Job aaaa * bbbb will yell aaaa's number multiplied by bbbb's number.
* Job aaaa / bbbb will yell aaaa's number divided by bbbb's number.

So, in the above example, monkey drzm has to wait for monkeys hmdt and zczc to
yell their numbers. Fortunately, both hmdt and zczc have jobs that involve
simply yelling a single number, so they do this immediately: 32 and 2. Monkey
drzm can then yell its number by finding 32 minus 2: 30.

Then, monkey sjmn has one of its numbers (30, from monkey drzm), and already
has its other number, 5, from dbpl. This allows it to yell its own number by
finding 30 multiplied by 5: 150.

This process continues until root yells a number: 152.

However, your actual situation involves considerably more monkeys. What number
will the monkey named root yell?

--- Part Two ---

Due to some kind of monkey-elephant-human mistranslation, you seem to have
misunderstood a few key details about the riddle.

First, you got the wrong job for the monkey named root; specifically, you got
the wrong math operation. The correct operation for monkey root should be =,
which means that it still listens for two numbers (from the same two monkeys as
before), but now checks that the two numbers match.

Second, you got the wrong monkey for the job starting with humn:. It isn't a
monkey - it's you. Actually, you got the job wrong, too: you need to figure out
what number you need to yell so that root's equality check passes. (The number
that appears after humn: in your input is now irrelevant.)

In the above example, the number you need to yell to pass root's equality test
is 301. (This causes root to get the same number, 150, from both of its
monkeys.)

What number do you yell to pass root's equality test?
"""


class Monkey:
    def __init__(
        self, *, resolved_value=None, dependencies=None, operation=None
    ) -> None:
        self.resolved_value = resolved_value
        self.dependencies = dependencies
        self.operation = operation

    def __repr__(self) -> str:
        return " ".join(
            map(str, [self.resolved_value, self.dependencies, self.operation])
        )


def parse_monkeys(lines: list[str]) -> dict[str, Monkey]:
    monkeys = {}
    for line in lines:
        parts = line.split()

        monkey_name = parts[0][:4]
        if len(parts) == 2:
            # This is a number monkey
            if monkey_name == "humn":
                monkey = Monkey(resolved_value=1j)
            else:
                monkey = Monkey(resolved_value=int(parts[1]))
        else:
            # This is a math operation monkey
            if monkey_name == "root":
                operation = "="
            else:
                operation = parts[2]
            monkey = Monkey(dependencies=(parts[1], parts[3]), operation=operation)

        monkeys[monkey_name] = monkey

    for monkey in monkeys.values():
        if monkey.resolved_value is not None:
            continue

        monkey.dependencies = (
            monkeys[monkey.dependencies[0]],
            monkeys[monkey.dependencies[1]],
        )

    return monkeys


def resolve_value(monkey: Monkey) -> int | complex:
    if monkey.resolved_value is not None:
        return monkey.resolved_value

    dependency_1 = monkey.dependencies[0]
    dependency_2 = monkey.dependencies[1]

    value_1 = resolve_value(dependency_1)
    value_2 = resolve_value(dependency_2)

    match monkey.operation:
        case "+":
            monkey.resolved_value = value_1 + value_2

        case "-":
            monkey.resolved_value = value_1 - value_2

        case "*":
            monkey.resolved_value = value_1 * value_2

        case "/":
            monkey.resolved_value = value_1 / value_2

        case "=":
            # This only applies to the root monkey
            assert value_1 == value_2
            monkey.resolved_value = value_1

    assert monkey.resolved_value is not None
    return monkey.resolved_value


# monkey_data = open("../puzzle-input/day21-example-input.txt").readlines()
monkey_data = open("../puzzle-input/day21-input.txt").readlines()

monkeys = parse_monkeys(monkey_data)
root = monkeys["root"]
dependency_1 = root.dependencies[0]
dependency_2 = root.dependencies[1]

res1 = resolve_value(dependency_1)
res2 = resolve_value(dependency_2)

# Apparently this works because of complex number magic
solution = int((res1.real - res2.real) / (res2.imag - res1.imag))

# Reset the monkey data so any calculated (i.e. cache) values are erased
monkeys = parse_monkeys(monkey_data)
monkeys["humn"].resolved_value = solution

# It should pass the assertion for equality now
root = monkeys["root"]
resolve_value(root)

print(solution)
