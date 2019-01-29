from solver import SudokuBoard, InvalidSudokuException,UnsolvableSudokuException

def test_exceptions():
    try:
        s = SudokuBoard([[],[],[]])
    except Exception as e:
        assert type(e) == InvalidSudokuException

    try:
        s = SudokuBoard([[1,2,3,4,5,6,7,8,9],[1,2,3],[],[],[],[],[],[],[]])
    except Exception as e:
        assert type(e) == InvalidSudokuException

    try:
        SudokuBoard.subgridize([[],[]])
    except Exception as e:
        assert type(e) == ValueError

    try:
        SudokuBoard([[1,1,None,None,None,None,None,None,None],
                            [None,None,None,None,None,None,None,None,None],
                            [None,None,None,None,None,None,None,None,None],
                            [None,None,None,None,None,None,None,None,None],
                            [None,None,None,None,None,None,None,None,None],
                            [None,None,None,None,None,None,None,None,None],
                            [None,None,None,None,None,None,None,None,None],
                            [None,None,None,None,None,None,None,None,None],
                            [None,None,None,None,None,None,None,None,None]]
                            )
    except Exception as e:
        assert type(e) == InvalidSudokuException
        
    print("Passed exceptions test")

def test_simple_sudoku():
    global s
    assert SudokuBoard.subgridize([[1,1,1,2,2,2,3,3,3],
                       [1,1,1,2,2,2,3,3,3],
                       [1,1,1,2,2,2,3,3,3]]) == [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                 [2, 2, 2, 2, 2, 2, 2, 2, 2],
                                                 [3, 3, 3, 3, 3, 3, 3, 3, 3]]

    s = SudokuBoard([[8,   7,   6,     9,   None,None,  None,None,None],
                     [None,1,   None,  None,None,6,     None,None,None],
                     [None,4,   None,  3,   None,5,     8,   None,None],
                     
                     [4,   None,None,  None,None,None,  2,   1,   None],
                     [None,9,   None,  5,   None,None,  None,None,None],
                     [None,5,   None,  None,4,   None,  3,   None,   6],
                     
                     [None,2,   9,     None,None,None,  None,None,8   ],
                     [None,None,4,     6,   9,   None,  1,   7,   3   ],
                     [None,None,None,  None,None,1,     None,None,4   ]])
    
    assert s.subgrids == [[8, 7, 6, None, 1, None, None, 4, None],
                            [9, None, None, None, None, 6, 3, None, 5],
                            [None, None, None, None, None, None, 8, None, None],
                            [4, None, None, None, 9, None, None, 5, None],
                            [None, None, None, 5, None, None, None, 4, None],
                            [2, 1, None, None, None, None, 3, None, 6],
                            [None, 2, 9, None, None, 4, None, None, None],
                            [None, None, None, 6, 9, None, None, None, 1],
                            [None, None, 8, 1, 7, 3, None, None, 4]]

    assert s.cols == [[8, None, None, 4, None, None, None, None, None],
                        [7, 1, 4, None, 9, 5, 2, None, None],
                        [6, None, None, None, None, None, 9, 4, None],
                        [9, None, 3, None, 5, None, None, 6, None],
                        [None, None, None, None, None, 4, None, 9, None],
                        [None, 6, 5, None, None, None, None, None, 1],
                        [None, None, 8, 2, None, 3, None, 1, None],
                        [None, None, None, 1, None, None, None, 7, None],
                        [None, None, None, None, None, 6, 8, 3, 4]]

    assert s.possibilities() == {(0, 4): [1, 2],
                               (0, 5): [2, 4],
                               (0, 6): [4, 5],
                               (0, 7): [2, 3, 4, 5],
                               (0, 8): [1, 2, 5],
                               (1, 0): [2, 3, 5, 9],
                               (1, 2): [2, 3, 5],
                               (1, 3): [2, 4, 7, 8],
                               (1, 4): [2, 7, 8],
                               (1, 6): [4, 5, 7, 9],
                               (1, 7): [2, 3, 4, 5, 9],
                               (1, 8): [2, 5, 7, 9],
                               (2, 0): [2, 9],
                               (2, 2): [2],
                               (2, 4): [1, 2, 7],
                               (2, 7): [2, 6, 9],
                               (2, 8): [1, 2, 7, 9],
                               (3, 1): [3, 6, 8],
                               (3, 2): [3, 7, 8],
                               (3, 3): [7, 8],
                               (3, 4): [3, 6, 7, 8],
                               (3, 5): [3, 7, 8, 9],
                               (3, 8): [5, 7, 9],
                               (4, 0): [1, 2, 3, 6, 7],
                               (4, 2): [1, 2, 3, 7, 8],
                               (4, 4): [1, 2, 3, 6, 7, 8],
                               (4, 5): [2, 3, 7, 8],
                               (4, 6): [4, 7],
                               (4, 7): [4, 8],
                               (4, 8): [7],
                               (5, 0): [1, 2, 7],
                               (5, 2): [1, 2, 7, 8],
                               (5, 3): [1, 2, 7, 8],
                               (5, 5): [2, 7, 8, 9],
                               (5, 7): [8, 9],
                               (6, 0): [1, 3, 5, 6, 7],
                               (6, 3): [4, 7],
                               (6, 4): [3, 5, 7],
                               (6, 5): [3, 4, 7],
                               (6, 6): [5, 6],
                               (6, 7): [5, 6],
                               (7, 0): [5],
                               (7, 1): [8],
                               (7, 5): [2, 8],
                               (8, 0): [3, 5, 6, 7],
                               (8, 1): [3, 6, 8],
                               (8, 2): [3, 5, 7, 8],
                               (8, 3): [2, 7, 8],
                               (8, 4): [2, 3, 5, 7, 8],
                               (8, 6): [5, 6, 9],
                               (8, 7): [2, 5, 6, 9]}

    assert s.solved().rows == [[8, 7, 6,  9, 1, 4,  5, 3, 2],
                               [3, 1, 5,  2, 8, 6,  7, 4, 9],
                               [9, 4, 2,  3, 7, 5,  8, 6, 1],
                             
                               [4, 3, 8,  7, 6, 9,  2, 1, 5],
                               [6, 9, 1,  5, 2, 3,  4, 8, 7],
                               [2, 5, 7,  1, 4, 8,  3, 9, 6],
                             
                               [1, 2, 9,  4, 3, 7,  6, 5, 8],
                               [5, 8, 4,  6, 9, 2,  1, 7, 3],
                               [7, 6, 3,  8, 5, 1,  9, 2, 4]]
    
    assert s.is_complete() == False
    assert s.is_solved() == False

    assert s.possible_numbers(1, 0) == [2, 3, 5, 9]
    assert s.possible_numbers(7, 5) == [2, 8]
    assert s.possible_numbers(7, 1) == [8]

    assert s.is_valid() == True

    print("Basic functionality passed")

def test_solved_sudoku():
    solved = SudokuBoard([[7,3,5, 6,1,4, 8,9,2],
                         [8,4,2, 9,7,3, 5,6,1],
                         [9,6,1, 2,8,5, 3,7,4],
                         
                         [2,8,6, 3,4,9, 1,5,7],
                         [4,1,3, 8,5,7, 9,2,6],
                         [5,7,9, 1,2,6, 4,3,8],
                         
                         [1,5,7, 4,9,2, 6,8,3],
                         [6,9,4, 7,3,8, 2,1,5],
                         [3,2,8, 5,6,1, 7,4,9]])

    assert solved.is_complete() == True
    assert solved.is_solved() == True

    print("Solved sudoku functionality passed")

def test_hard_sudoku():
    global hard_sudoku
    hard_sudoku = SudokuBoard([[None,3   ,None, 2   ,None,None, None,None,6   ],
                               [None,None,None, None,None,9   , None,None,4   ],
                               [7   ,6   ,None, None,None,None, None,None,None],
                               
                               [None,None,None, None,5   ,None, 7   ,None,None],
                               [None,None,None, None,None,1   , 8   ,6   ,None],
                               [None,5   ,None, 4   ,8   ,None, None,9   ,None],
                               
                               [8   ,None,None, None,None,None, None,None,None],
                               [None,None,None, None,7   ,6   , None,None,None,],
                               [None,7   ,5   , None,None,8   , 1   ,None,None]])

    assert hard_sudoku.solved().rows == [[4, 3, 8,  2, 1, 5,  9, 7, 6],
                                         [5, 2, 1,  7, 6, 9,  3, 8, 4],
                                         [7, 6, 9,  8, 3, 4,  5, 1, 2],
                                    
                                         [9, 8, 2,  6, 5, 3,  7, 4, 1],
                                         [3, 4, 7,  9, 2, 1,  8, 6, 5],
                                         [1, 5, 6,  4, 8, 7,  2, 9, 3],
                                    
                                         [8, 1, 4,  5, 9, 2,  6, 3, 7],
                                         [2, 9, 3,  1, 7, 6,  4, 5, 8],
                                         [6, 7, 5,  3, 4, 8,  1, 2, 9]]

    print("Hard sudoku solving test passed")

def test_all():
    test_exceptions()
    test_simple_sudoku()
    test_solved_sudoku()
    test_hard_sudoku()

if __name__ == "__main__":
    test_all()
