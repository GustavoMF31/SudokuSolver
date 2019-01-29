# SudokuSolver
A Sudoku solver in Python

```python

from solver import SudokuBoard

sudoku = SudokuBoard([[None,3   ,None,  2   ,None,None,  None,None,6   ],
                      [None,None,None,  None,None,9   ,  None,None,4   ],
                      [7   ,6   ,None,  None,None,None,  None,None,None],
                               
                      [None,None,None,  None,5   ,None,  7   ,None,None],
                      [None,None,None,  None,None,1   ,  8   ,6   ,None],
                      [None,5   ,None,  4   ,8   ,None,  None,9   ,None],
                               
                      [8   ,None,None,  None,None,None,  None,None,None],
                      [None,None,None,  None,7   ,6   ,  None,None,None,],
                      [None,7   ,5   ,  None,None,8   ,  1   ,None,None]])

solved_sudoku = sudoku.solved()
print(solved_sudoku.rows)
```
