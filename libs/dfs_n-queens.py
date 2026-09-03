"""
Solve the N-Queens problem with depth-first search
Return every valid placement of ``n`` queens on an ``n`` by ``n`` board.
A solution is represented by a list whose index is the row and whose value is the zero-based column containing that row's queen.
"""


def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    placement = []
    columns = set()
    descending_diagonals = set()  # row - column
    ascending_diagonals = set()  # row + column

    def search(row):
        if row == n:
            solutions.append(placement.copy())
            return

        for column in range(n):
            if (
                column in columns
                or row - column in descending_diagonals
                or row + column in ascending_diagonals
            ):
                continue

            placement.append(column)
            columns.add(column)
            descending_diagonals.add(row - column)
            ascending_diagonals.add(row + column)

            search(row + 1)

            placement.pop()
            columns.remove(column)
            descending_diagonals.remove(row - column)
            ascending_diagonals.remove(row + column)

    search(0)
    return solutions
