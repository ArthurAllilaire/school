# Get the
from numpy import inf


def addBP(bp, grid):
    """
    grid - numpy array of 0's representing non-blocked positions
    bp - list of tuples, which are coordinates where the position is blocked
    Modifies the grid passed in, don't need it any more
    """

    for coord in bp:
        grid[coord[1], coord[0]] = 1


def calc_weight(checked, fp):
    """
    A binded function so that only I only need to pass in the np, easier to deal with in the calc_weight.
    checked {(x,y): int}- dictionary of already calculated weights
    fp - finishing point
    """
    def weight_func(np):
        """
        np - (x,y) the position of the weight to be calculated
        """
        nonlocal checked, fp
        try:
            return checked[np]

        except KeyError:
            # Calculate the distance between the two points
            weight = ((fp[0] - np[0])**2 + (fp[1]-np[1])**2)**0.5

            # Add it to checked (global)
            checked[np] = weight

            return weight

    return weight_func


def surrounding(cp, grid, calc_weight):
    """ 
    cp = (x, y)
    grid: all the squares that have already been tried
    calced_weights: {(x,y): int} - any already calculated weights
    calc_weight: The function used to calculate the weight assigned to each variable, already bound with previous calculated weights and the fp - returns a float of the weight

    For every valid square in the periphery get the weight for that square

    """

    # Check every single square
    weights = {}
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            np = (cp[0]+x, cp[1]+y)
            # Having negative numbers is allowed in arrays, just gets them from the back, so have to set up checks instead of try and except
            # grid.shape = (num rows, num cols)
            # ignore all coords outside the grid or blocked coords or the coord we are currently on
            if np[0] < 0 or np[1] < 0 or np[0] > grid.shape[0]-1 or np[1] > grid.shape[1]-1 or grid[np] == 1 or np == cp:
                continue

            # Calculate the weight
            # Else calculate the weight and add it to the dict
            weights[np] = calc_weight(np)

            # Will need to add it to the overall dict of calculated weights.

    return weights


def get_best_weight(sur_weights):
    """
    Takes in a dict of weights, returning the best position. Currently worked out as the lowest weight.
    """

    best = ((0, 0), float(inf))

    for pos, weight in sur_weights.items():
        if weight < best[1]:
            best = (pos, weight)

    return best[0]
