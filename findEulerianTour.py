# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    print graph[1][0]
    checked = []
    tour = []
    prevItem = graph[0]
    tour.append(graph[0][0])
    tour.append(graph[0][1])
    for item in graph:
        ix = item[0]
        iy = item[1]
        prevIx = prevItem[0]
        prevIy = prevItem[1]
        if item == prevItem:
            continue
        if ix not in tour:
            tour.append(ix)
        if iy not in tour:
            tour.append(iy)
    return tour

print find_eulerian_tour([(1, 2), (2, 3), (3, 1)])
print find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])
