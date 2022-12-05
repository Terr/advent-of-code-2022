"""
--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded from
the ships. Supplies are stored in stacks of marked crates, but because the
needed supplies are buried under many other crates, the crates need to be
rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To
ensure none of the crates get crushed or fall over, the crane operator will
rearrange them in a series of carefully-planned steps. After the crates are
rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate
procedure, but they forgot to ask her which crate will end up where, and they
want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the
rearrangement procedure (your puzzle input). For example:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates:
crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates;
from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a
single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a
quantity of crates is moved from one stack to a different stack. In the first
step of the above rearrangement procedure, one crate is moved from stack 2 to
stack 1, resulting in this configuration:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

In the second step, three crates are moved from stack 1 to stack 3. Crates are
moved one at a time, so the first crate to be moved (D) ends up below the
second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are
moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in
this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3,
so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each
stack?
"""

from collections import namedtuple


Step = namedtuple("Step", ["num_crates", "from_", "to_"])

# Each stack in the diagram, empty or not (even at the end of a line), is 4
# characters wide
DIAGRAM_STACK_WIDTH = 4


def parse_crate_diagram(diagram_lines: list[str]) -> list[list[str]]:
    diagram_width = len(diagram_lines[0])
    num_stacks = diagram_width // DIAGRAM_STACK_WIDTH
    stacks = [[] for _ in range(num_stacks)]

    for line in diagram_lines:
        for stack_num, pos in enumerate(range(0, diagram_width, DIAGRAM_STACK_WIDTH)):
            stack = line[pos : pos + DIAGRAM_STACK_WIDTH]
            if stack[1].isalpha():
                stacks[stack_num].insert(0, stack[1])

    return stacks


def parse_rearrangement_procedure(procedure_lines: list[str]) -> list[Step]:
    procedure = []

    for line in procedure_lines:
        parts = line.split()
        procedure.append(
            Step(num_crates=int(parts[1]), from_=int(parts[3]), to_=int(parts[5]))
        )

    return procedure


# lines = open("../puzzle-input/day5-example-input.txt").readlines()
lines = open("../puzzle-input/day5-input.txt").readlines()

# Find the line that marks the end of the crate diagram
for line_num, line in enumerate(lines):
    if line.strip().startswith("1"):
        break

stacks = parse_crate_diagram(lines[:line_num])
# 2 lines are skipped: the stack numbers and an empty line
procedure = parse_rearrangement_procedure(lines[line_num + 2 :])

for step in procedure:
    for _ in range(step.num_crates):
        crate = stacks[step.from_ - 1].pop()
        stacks[step.to_ - 1].append(crate)

print("".join([stack.pop() for stack in stacks]))
