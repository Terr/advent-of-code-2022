"""
--- Day 7: No Space Left On Device ---

You can hear birds chirping and raindrops hitting leaves as the expedition
proceeds. Occasionally, you can even hear much louder sounds in the distance;
how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its
communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device

Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting
terminal output (your puzzle input). For example:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k

The filesystem consists of a tree of files (plain data) and directories (which
can contain other directories or files). The outermost directory is called /.
You can navigate around the filesystem, moving into or out of directories and
listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed,
very much like some modern computers:

* cd means change directory. This changes which directory is the current
  directory, but the specific result depends on the argument:
    * cd x moves in one level: it looks in the current directory for the
      directory named x and makes it the current directory.
    * cd .. moves out one level: it finds the directory that contains the
      current directory, then makes that directory the current directory.
    * cd / switches the current directory to the outermost directory, /.

* ls means list. It prints out all of the files and directories immediately
  contained by the current directory:
    * 123 abc means that the current directory contains a file named abc with
      size 123.
    * dir xyz means that the current directory contains a directory named xyz.

Given the commands and output in the example above, you can determine that the
filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)

Here, there are four directories: / (the outermost directory), a and d (which
are in /), and e (which is in a). These directories also contain files of
various sizes.

Since the disk is full, your first step should probably be to find directories
that are good candidates for deletion. To do this, you need to determine the
total size of each directory. The total size of a directory is the sum of the
sizes of the files it contains, directly or indirectly. (Directories themselves
do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

* The total size of directory e is 584 because it contains a single file i of
  size 584 and no other directories.
* The directory a has total size 94853 because it contains files f (size
  29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a
  contains e which contains i).
* Directory d has total size 24933642.
* As the outermost directory, / contains every file. Its total size is
  48381165, the sum of the size of every file.

To begin, find all of the directories with a total size of at most 100000, then
calculate the sum of their total sizes. In the example above, these directories
are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this
example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is the
sum of the total sizes of those directories?
"""

from collections import namedtuple
from functools import reduce


File = namedtuple("File", ["filename", "size"])


class Directory:
    # Note: it's necessary to put the Directory type in quotes here because it
    # hasn't been defined yet (we're in the middle of doing that). Python 3.11
    # fixes this.
    def __init__(self, parent: "Directory" = None):
        self.parent = parent
        self.dirs = {}
        self.files = []

    def add_dir(self, dirname: str):
        self.dirs[dirname] = Directory(parent=self)

    def get_dir_by_name(self, dirname: str) -> "Directory":
        if dirname not in self.dirs:
            raise Exception("No directory named %s" % dirname)

        return self.dirs[dirname]

    def go_directory_up(self) -> "Directory":
        if self.parent is None:
            raise Exception("Cannot go up, root of filesystem reached")

        return self.parent

    def add_file(self, file: File):
        self.files.append(file)

    def get_total_size(self) -> int:
        own_size = reduce(lambda total, file: total + file.size, self.files, 0)

        children_size = reduce(
            lambda total, dir: total + dir.get_total_size(), self.dirs.values(), 0
        )

        return own_size + children_size


def parse_terminal_output(lines: list[str]) -> Directory:
    """Builds a filesystem tree based on the given terminal output."""

    filesystem_root = Directory()
    current_directory = filesystem_root

    for line in lines:
        parts = line.split()

        if len(parts) < 2:
            raise Exception

        match parts:
            case ["$", "cd", "/"]:
                # Line describes a change directory command back to the root
                current_directory = filesystem_root

            case ["$", "cd", ".."]:
                # Line describes a command to go to the parent directory of the
                # current path
                current_directory = current_directory.go_directory_up()

            case ["$", "cd", dirname]:
                current_directory = current_directory.get_dir_by_name(dirname)

            case ["$", "ls"]:
                # Line describes a listing command
                # Nothing has to be done for this one
                pass

            case ["dir", dirname]:
                # Line describes a directory present in the current path
                current_directory.add_dir(dirname)

            case [size, filename] if parts[0].isnumeric():
                # Line describes a file
                current_directory.add_file(File(filename, int(size)))

            case other:
                raise Exception("Unidentified line: %s" % other)

    return filesystem_root


# terminal_output_lines = open("../puzzle-input/day7-example-input.txt").readlines()
terminal_output_lines = open("../puzzle-input/day7-input.txt").readlines()

filesystem_root = parse_terminal_output(terminal_output_lines)

directory_stack = [filesystem_root]
matching_dirs = []

while len(directory_stack):
    directory = directory_stack.pop()
    directory_stack.extend(directory.dirs.values())

    if directory.get_total_size() <= 100_000:
        matching_dirs.append(directory)

print(sum([d.get_total_size() for d in matching_dirs]))
