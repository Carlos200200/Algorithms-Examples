###########################
# Sudoku Solver
# Codewars 3kyu
###########################


import itertools

def sudoku(Puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    global puzzle
    puzzle = Puzzle
    
    Solved = False
    while not Solved:
        Solved = True
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    Solved = False
                    CheckSolved(i,j)
    return puzzle

def CheckSolved(i,j):
        
    global puzzle
    Candidates = list(range(1,10))
    
    #Check Line and Column
    for k in range(9):
        if puzzle[i][k] in Candidates: Candidates.remove(puzzle[i][k])
        if puzzle[k][j] in Candidates: Candidates.remove(puzzle[k][j])
        
    #Ver1-------
    #Check Square    
    #StartI = (i//3)*3 
    #StartJ = (j//3)*3
    #for p,q in itertools.product(range(3), range(3)):
    #    if puzzle[StartI+p][StartJ+q] in Candidates: Candidates.remove(puzzle[StartI+p][StartJ+q])

    #Ver2-------
    #Check Square
    StartI = (i//3)*3  # Start of Sudoku square zone
    StartJ = (j//3)*3
    for p,q in itertools.product(range(StartI, StartI+3), range(StartJ, StartJ+3)):
        if puzzle[p][q] in Candidates: Candidates.remove(puzzle[p][q])
        
    if len(Candidates) == 1:
        puzzle[i][j] = Candidates[0]
        
    return puzzle


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
sudoku(puzzle)
    
