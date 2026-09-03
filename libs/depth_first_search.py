"""
Implement the Depth-First Search Algorithm

Return the nodes reachable from ``node`` in depth-first order.
``matrix[row][column] == 1`` indicates an edge from ``row`` to
``column``.  The stack and visited collection are local to each call so
repeated traversals do not share state.
"""


def dfs(matrix, node):
    stack = [node]
    visited = set()
    traversal = []

    while stack:
        current = stack.pop()
        if current in visited:
            continue

        visited.add(current)
        traversal.append(current)

        for neighbor, is_connected in enumerate(matrix[current]):
            if is_connected == 1 and neighbor not in visited:
                stack.append(neighbor)

    return traversal
