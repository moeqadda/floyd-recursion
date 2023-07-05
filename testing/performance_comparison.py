#!/usr/bin/env python3

import sys
import time

import imperative_floyd
import recursive_floyd


def compare_performance():
    
    NO_PATH = sys.maxsize
    graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0],
    ]

    started_at = time.time()
    for _ in range(2**12):
        recursive_floyd.floyd(graph)
    elapsed_recursive = time.time() - started_at

    started_at = time.time()
    for _ in range(2**12):
        imperative_floyd.floyd(graph)
    elapsed_imperative = time.time() - started_at

    return (elapsed_recursive, elapsed_imperative)


if __name__ == '__main__':
    elapsed_recursive, elapsed_imperative = compare_performance()
    print('recursive: {}s'.format(round(elapsed_recursive, 2)))
    print('imperative: {}s'.format(round(elapsed_imperative, 2)))
