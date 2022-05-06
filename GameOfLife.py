import random

from matplotlib import pyplot
import time

# init values
dimX = 100
dimY = 100
incremental = False  # set to true to use the incremental code


# init board
def genRand():
    xs = []
    ys = []

    for n in range(dimX * dimY // 2):
        xs.append(random.randint(0, dimX - 1))
        ys.append(random.randint(0, dimY - 1))

    # print(tuple(zip(xs, ys)))
    return tuple(zip(xs, ys))


# some presets, uncomment the one you want to use or make your own
# the points are stored in an array of tuples, each point represents a living cell, all others start as dead

# default
# initial = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

# glider - moves across the grid until it hits a wall
# initial = [(0, 0), (2, 0), (1, 1), (2, 1), (1, 2)]

# random generation
initial = genRand()

# fill grid with 0s
universal = [[0 for x in range(dimX)] for y in range(dimY)]
updated = [[0 for x in range(dimX)] for y in range(dimY)]

# update the grid with the initial live settings
for p in initial:
    # print(p)
    universal[p[1]][p[0]] = 1

# display the grid
pyplot.imshow(universal)
pyplot.ion()
pyplot.show()
pyplot.pause(0.5)


# main algorithm
def survive(universe, update):
    for y in range(dimY):
        for x in range(dimX):
            count = 0

            if incremental:
                if y > 0 and x > 0:
                    if universe[y - 1][x - 1]:
                        count += 1

                if x > 0:
                    if universe[y][x - 1]:
                        count += 1

                if y < dimY - 1 and x > 0:
                    if universe[y + 1][x - 1]:
                        count += 1

                if y < dimY - 1:
                    if universe[y + 1][x]:
                        count += 1

                if x < dimX - 1 and y < dimY - 1:

                    if universe[y + 1][x + 1]:
                        count += 1

                if x < dimX - 1:
                    if universe[y][x + 1]:
                        count += 1

                if y > 0 and x < dimX - 1:
                    if universe[y - 1][x + 1]:
                        count += 1

                if y > 0:
                    if universe[y - 1][x]:
                        count += 1

                if count < 2 or count > 3:
                    universe[y][x] = 0
                elif count == 3 and not universe[y][x]:
                    universe[y][x] = 1
            else:
                if y > 0 and x > 0:
                    if universe[y - 1][x - 1]:
                        count += 1

                if x > 0:
                    if universe[y][x - 1]:
                        count += 1

                if y < dimY - 1 and x > 0:
                    if universe[y + 1][x - 1]:
                        count += 1

                if y < dimY - 1:
                    if universe[y + 1][x]:
                        count += 1

                if x < dimX - 1 and y < dimY - 1:

                    if universe[y + 1][x + 1]:
                        count += 1

                if x < dimX - 1:
                    if universe[y][x + 1]:
                        count += 1

                if y > 0 and x < dimX - 1:
                    if universe[y - 1][x + 1]:
                        count += 1

                if y > 0:
                    if universe[y - 1][x]:
                        count += 1

                if count < 2 or count > 3:
                    update[y][x] = 0
                elif count == 3 and not universe[y][x]:
                    update[y][x] = 1
                elif count == 2 or (count == 3 and universe[y][x]):
                    update[y][x] = universe[y][x]

    if not incremental:
        universe = update
        update = [[0 for x in range(dimX)] for y in range(dimY)]

    return universe, update

# while loop and execution time tracking
def life(universe, update):
    total = 0
    c = 0
    while 1:
        start = time.time()
        universe, update = survive(universe, update)
        end = time.time()
        t = (end - start) * 1000
        if t == 0 and c > 0:
            t = total / c
        total += t
        c += 1

        print("Execution time: ", t)
        print("Average: ", total / c)

        pyplot.cla()
        pyplot.imshow(universe)
        pyplot.show()
        pyplot.pause(0.1)


life(universal, updated)
