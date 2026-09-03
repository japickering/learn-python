"""
Solve the Tower of Hanoi Algorithm
Return the sequence of board states for a Tower of Hanoi solution.

Disks are represented by integers, with the largest disk at the start of
each rod's list. The returned string contains the initial state and one
state after every move, separated by newlines.
"""


def hanoi_solver(number_of_disks):
    if not isinstance(number_of_disks, int) or isinstance(number_of_disks, bool):
        raise TypeError("number_of_disks must be a positive integer")

    if number_of_disks < 1:
        raise ValueError("number_of_disks must be a positive integer")

    rods = [list(range(number_of_disks, 0, -1)), [], []]
    states = []

    def record_state():
        states.append(" ".join(str(rod) for rod in rods))

    def move(disks, source, auxiliary, target):
        if disks == 0:
            return

        move(disks - 1, source, target, auxiliary)
        rods[target].append(rods[source].pop())
        record_state()
        move(disks - 1, auxiliary, source, target)

    record_state()
    move(number_of_disks, 0, 1, 2)

    return "\n".join(states)
