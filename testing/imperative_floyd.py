import sys
import itertools

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])


def floyd(distance):
    """
    A simple implementation of Floyd's algorithm.
    """
    for intermediate in range(MAX_LENGTH):
        for start_node in range(MAX_LENGTH):
            for end_node in range(MAX_LENGTH):
                # Assume that if start_node and end_node are the same
                # then the distance would be zero
                if start_node == end_node:
                    distance[start_node][end_node] = 0
                    continue

                # return all possible paths and find the minimum
                distance[start_node][end_node] = min(distance[start_node][end_node],
                                                     distance[start_node][intermediate] +
                                                     distance[intermediate][end_node])

    # Any value that has sys.maxsize has no path
    print(distance)

floyd(graph)
