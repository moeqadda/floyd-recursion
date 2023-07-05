import sys
import itertools

NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
MAX_LENGTH = len(graph[0])


# Recursive function to calculate the shortest path between nodes
def shortest_path(start, end, intermediate, distance):
    """
    Implementation of Floyd's algorithm using recursion.
    Calculates the shortest path between 'start' and 'end' nodes
    considering different intermediate nodes.
    """
    if intermediate < 0:
        return distance[start][end]

    # Return the minimum distance between two paths:
    # - The path without the current intermediate node.
    # - The path with the current intermediate node
    return min(
        shortest_path(start, end, intermediate - 1, distance),
        shortest_path(start, intermediate, intermediate - 1, distance) +
        shortest_path(intermediate, end, intermediate - 1, distance)
    )


def floyd(distance):
    """
    Implementation of Floyd's algorithm using recursion.
    Calculates the shortest paths between all pairs of nodes in the graph.
    """
    for start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        distance[start_node][end_node] = shortest_path(
            start_node, end_node, MAX_LENGTH - 1, distance
        )

    # Return the updated distance matrix
    return distance


if __name__ == '__main__':
    # Call the 'floyd' function and print the resulting distance matrix
    print(floyd(graph))
