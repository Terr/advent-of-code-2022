"""
--- Day 6: Tuning Trouble ---

The preparations are finally complete; you and the Elves leave camp on foot and
begin to make your way toward the star fruit grove.

As you move through the dense undergrowth, one of the Elves gives you a
handheld device. He says that it has many fancy features, but the most
important one to set up right now is the communication system.

However, because he's heard you have significant experience dealing with
signal-based systems, he convinced the other Elves that it would be okay to
give you their one malfunctioning device - surely you'll have no problem fixing
it.

As if inspired by comedic timing, the device emits a few colorful sparks.

To be able to communicate with the Elves, the device needs to lock on to their
signal. The signal is a series of seemingly-random characters that the device
receives one at a time.

To fix the communication system, you need to add a subroutine to the device
that detects a start-of-packet marker in the datastream. In the protocol being
used by the Elves, the start of a packet is indicated by a sequence of four
characters that are all different.

The device will send your subroutine a datastream buffer (your puzzle input);
your subroutine needs to identify the first position where the four most
recently received characters were all different. Specifically, it needs to
report the number of characters from the beginning of the buffer to the end of
the first such four-character marker.

For example, suppose you receive the following datastream buffer:

    mjqjpqmgbljsphdztnvjfqwrcgsmlb

After the first three characters (mjq) have been received, there haven't been
enough characters received yet to find the marker. The first time a marker
could occur is after the fourth character is received, making the most recent
four characters mjqj. Because j is repeated, this isn't a marker.

The first time a marker appears is after the seventh character arrives. Once it
does, the last four characters received are jpqm, which are all different. In
this case, your subroutine should report the value 7, because the first
start-of-packet marker is complete after 7 characters have been processed.

Here are a few more examples:

    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

How many characters need to be processed before the first start-of-packet
marker is detected?
"""

START_MARKER_LEN = 4

# data = open("../puzzle-input/day6-example-input.txt").read().strip()
data = open("../puzzle-input/day6-input.txt").read().strip()

cursor_pos = 0
while cursor_pos <= len(data) - START_MARKER_LEN:
    found_start = True

    for n in range(0, START_MARKER_LEN - 1):
        character = data[cursor_pos + n]
        updated_cursor_pos = False

        for i in range(1, START_MARKER_LEN - n):
            other_character = data[cursor_pos + n + i]

            if other_character == character:
                # Duplicate character found so the current `character` does not
                # mark the beginning of a start-of-packet. Keep searching!
                cursor_pos += 1
                found_start = False
                updated_cursor_pos = True
                break

        if updated_cursor_pos:
            break

    if found_start:
        print(data[cursor_pos : cursor_pos + START_MARKER_LEN])
        print(cursor_pos, "+", START_MARKER_LEN, "=", cursor_pos + START_MARKER_LEN)
        break