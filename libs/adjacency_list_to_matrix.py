"""
Build an Adjacency List to Matrix Converter

Convert a graph's adjacency list into an adjacency matrix.
Nodes are represented by consecutive integer keys from ``0`` to
``len(adjacency_list) - 1``. Each value contains the nodes reachable from that key.
"""


def adjacency_list_to_matrix(adjacency_list):
    size = len(adjacency_list)
    adjacency_matrix = [[0] * size for _ in range(size)]

    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            adjacency_matrix[node][neighbor] = 1

    for row in adjacency_matrix:
        print(row)

    return adjacency_matrix
