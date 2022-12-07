import AoC_tools.aoc_tools as aoc


class File(object):

    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory(object):

    def __init__(self, name, parent):
        self.name = name
        self.children = dict()
        self.parent = parent
        self.files = list()

    def add_child(self, dir):
        self.children[dir.name] = dir

    @property
    def size(self):
        size = 0
        for f in self.files:
            size += f.size
        for c in self.children.values():
            size += c.size
        return size

    @property
    def subdirs(self):
        subdirs = list(self.children.values())
        for c in self.children.values():
            subdirs.extend(c.subdirs)
        return subdirs

def walk(data):
    root = Directory("/", parent=None)
    current_dir = root
    for i in range(1, len(data)):
        line = data[i]
        if line.startswith("$ ls"):
            pass
        elif line.startswith("$ cd"):
            dirname = line.split()[2]
            if dirname == "..":
                # set parent as current
                current_dir = current_dir.parent
            else:
                newdir = Directory(dirname, parent=current_dir)
                current_dir.add_child(newdir)
                current_dir = newdir
        elif line.startswith("dir"):
            pass
        elif line[0].isdigit():
            filename = line.split()[1]
            size = int(line.split()[0])
            current_dir.files.append(File(filename, size))
    return root


data = aoc.read_input("input.txt", sep1 = "\n")
root = walk(data)

# part 1
total_size = 0
for d in root.subdirs:
    if d.size <= 100000:
        total_size += d.size

assert total_size == 1334506

# part 2
dirs = root.subdirs
dirs.append(root)
sizes = [d.size for d in dirs]
sizes.sort()
for s in sizes:
    if s >= 30000000 - (70000000 - root.size):
        result = s
        break

assert result == 7421137
