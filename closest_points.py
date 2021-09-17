"""
Given a list of points (Euclidean coordinates) in plane, we are searching for two point
whose distance (Euclidean distance) is the smallest among all pairs of points.
Again we use the divide and conquer strategy to solve this problem.
Inspired by (one dimensional case) the closest points on straight line, which is immediately solvable
by sorting them with respect to their distance from a point (say origin), we first sort the points w.r.t x-coordinate.
We skip the sorting part of the algorithm and simply use python built-in function sorted().
"""


def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def closest_pairs(points_list):
    # Base case
    if len(points_list) == 2:
        return points_list[0], points_list[1]
    elif len(points_list) == 3:
        a = dist(points_list[0], points_list[1])
        b = dist(points_list[1], points_list[2])
        c = dist(points_list[2], points_list[0])
        if a <= b and a <= c:
            return points_list[0], points_list[1]
        elif b <= a and b <= c:
            return points_list[1], points_list[2]
        else:
            return points_list[2], points_list[0]

    # sorting w.r.t x-coordinate
    sorted_list = sorted(points_list, key=lambda point: point[0])
    # DIVIDE: dividing the list in two parts
    mid_len = int(len(sorted_list) / 2)
    X = sorted_list[:mid_len]
    Y = sorted_list[mid_len:]
    # CONQUER: finding the closest pairs in X and Y separately
    (p1, p2) = closest_pairs(X)
    (q1, q2) = closest_pairs(Y)
    d = None
    d_X = dist(p1, p2)
    d_Y = dist(q1, q2)
    if d_X <= d_Y:
        closest = (p1, p2)
        d = d_X
    else:
        closest = (q1, q2)
        d = d_Y

    # finding split closest pairs
    x0 = X[-1][0]
    strip = [p in sorted_list, p[0]<=x0+d and p[0]>=x0-d]

    return closest
