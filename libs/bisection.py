"""
Find square roots using the bisection method
Return the square root of ``square_target`` using interval bisection.
The search interval is narrowed until its width is no greater than the requested tolerance, or until ``max_iterations`` has been reached.
"""


def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers")

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    low = square_target if square_target < 1 else 1
    high = 1 if square_target < 1 else square_target
    root = None

    for _ in range(max_iterations):
        mid = (low + high) / 2
        if high - low <= tolerance:
            root = mid
            break

        if mid**2 < square_target:
            low = mid
        else:
            high = mid

    if root is None:
        print(f"Failed to converge within {max_iterations} iterations")
        return None

    print(f"The square root of {square_target} is approximately {root}")
    return root
