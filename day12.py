from collections import Counter

class Cave:
    def __init__(self, name):
        self.name = name
        self.big = name.isupper()
        self.connections = set()

    def __hash__(self):
        return hash(self.name)

    def connect(self, other):
        self.connections.add(other)
        other.connections.add(self)

    def extend(self, visited):
        """Find all connections to new caves (rules of part 1)."""
        for nextcave in self.connections:
            if nextcave.big or nextcave not in visited:
                yield nextcave

    def extend2(self, visited):
        """Find all connections to new caves (rules of part 2)."""
        cave_counts = Counter([cave for cave in visited if not cave.big])
        for nextcave in self.connections:
            if nextcave.name == "start":
                # startcave can't be revisited
                continue
            elif nextcave.big:
                # big caves can always be visited
                yield nextcave
            elif nextcave not in cave_counts:
                # unvisited caves can always be visited
                yield nextcave
            elif not cave_counts or max(cave_counts.values()) == 1:
                # if it's already visited, it can only be revisited if there is
                # no other cave with >1 visit
                yield nextcave


# read input
caves = {} # {name:cave} mappings
with open("in12.txt") as connections:
    for path in connections:
        cave1, cave2 = path.strip().split("-")
        if cave1 in caves:
            cave1 = caves[cave1]
        else:
            caves[cave1] = Cave(cave1)
            cave1 = caves[cave1]

        if cave2 in caves:
            cave2 = caves[cave2]
        else:
            caves[cave2] = Cave(cave2)
            cave2 = caves[cave2]

        cave1.connect(cave2)

# part 1
subroutes = [[caves["start"]]]
complete_routes = []
while subroutes:
    route = subroutes.pop()
    for newcave in route[-1].extend(route):
        if newcave == caves["end"]:
            complete_routes.append(route)
            continue
        newroute = list(route) # copies the route
        newroute.append(newcave)
        subroutes.append(newroute)

print("part 1:", len(complete_routes))

# part 2
# this looks exactly like part 1, but with another `extend` method
subroutes = [[caves["start"]]]
complete_routes = []
while subroutes:
    route = subroutes.pop()
    for newcave in route[-1].extend2(route):
        if newcave == caves["end"]:
            complete_routes.append(route)
            continue
        newroute = list(route) # copies the route
        newroute.append(newcave)
        subroutes.append(newroute)

print("part 2:", len(complete_routes))