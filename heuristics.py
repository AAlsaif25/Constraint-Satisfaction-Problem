from utils import number_of_conflicts

"""
Most Constrained Variable (MRV) heuristic

returns the variable with the fewest possible values remaining
Most_Constrained_Variable

"""


def most_constrained_variable(assignment, sudoku):

    unassigned = []

    # for each of the cells
    for cell in sudoku.cells:

        # if the cell is not in the assignment
        if cell not in assignment:

            # add it
            unassigned.append(cell)

    # the criterion here is the length of the possibilities (MRV)
    def criterion(cell): return len(sudoku.possibilities[cell])

    # we return the variable with the fewest possible values remaining
    return min(unassigned, key=criterion)


"""
Least Constraining Value (LCV) heuristic


"""


def Least_Constraining_Value(sudoku, cell):

    # since we are looking for the least constraining value
    # contained in [1, 2, 3, ..., 8, 9], smallest case possible is length of 1
    if len(sudoku.possibilities[cell]) == 1:
        return sudoku.possibilities[cell]

    # we want to sort based on the number of conflicts
    def criterion(value): return number_of_conflicts(sudoku, cell, value)
    return sorted(sudoku.possibilities[cell], key=criterion)
