from tkinter import Tk, messagebox, Spinbox, Button, END
from solver import SudokuBoard, UnsolvableSudokuException, InvalidSudokuException

FONT_SIZE = 15
BOX_WIDTH = 2
TITLE = "Sudoku Solver"
SOLVE_TEXT = "Solve"
CLEAR_TEXT = "Clear"

def solve_sudoku(rows):
    return SudokuBoard(rows).solved().rows

def set_to_solved(spinboxes):
    #Sets all spinboxes to the solved sudoku
    #Shows messageboxes for unsolvable/invalid Sudokus
    
    rows = get_all_spinboxes(spinboxes)
    rows_with_nones = zeros_to_nones(rows)
    
    try:
        solved_rows = solve_sudoku(rows_with_nones)
        set_all_spinboxes(spinboxes, solved_rows)
        
    except InvalidSudokuException:
        messagebox.showinfo("Error", "Invalid Sudoku")
        
    except UnsolvableSudokuException:
        messagebox.showinfo("Error", "Unsolvable Sudoku")

def set_spinbox(spinbox, value):
    #Sets the value of a spinbox
    
    spinbox.delete(0, END)
    spinbox.insert(0, str(value))

def set_all_spinboxes(spinboxes, new_values):
    #Sets all spinboxes to an array of values
    
    for y, row in enumerate(spinboxes):
        for x, spinbox in enumerate(row):
            set_spinbox(spinbox, str(new_values[y][x]))

def clean_all_spinboxes(spinboxes):
    #Sets all their values to 0
    
    set_all_spinboxes(spinboxes, [[0,0,0,0,0,0,0,0,0] for _ in range(9)])

def get_all_spinboxes(spinboxes):
    #Gets the value of all spinboxes
    
    values = [[],[],[],[],[],[],[],[],[]]
    
    for y, row in enumerate(spinboxes):
        for x, spinbox in enumerate(row):
            values[y].append(int(spinbox.get()))

    return values
            

def nones_to_zeros(rows):
    #Transforms all the 'None's into zeros
    output = [[],[],[],[],[],[],[],[],[]]
    
    for y, row in enumerate(rows):
        for num in row:
            output[y].append(num if num else 0)

    return output

def zeros_to_nones(rows):
    #Transforms all the zeros into None's
    output = [[],[],[],[],[],[],[],[],[]]
    
    for y, row in enumerate(rows):
        for num in row:
            output[y].append(num if num != 0 else None)

    return output
        
def generate_spinboxes(window):
    spinboxes = [[],[],[],[],[],[],[],[],[]]
    
    for y in range(9):
        for x in range(9):
            spinbox = Spinbox(window, from_=0, to=9, width=BOX_WIDTH, font=("DEFAULT", FONT_SIZE))
            spinbox.grid(column=x, row=y)
            spinboxes[y].append(spinbox)

    return spinboxes

if __name__ == "__main__":
    window = Tk()
    window.title(TITLE)
    
    spinboxes = generate_spinboxes(window)
    
    solve = Button(text=SOLVE_TEXT, command=lambda:set_to_solved(spinboxes))
    solve.grid(row=9, column=6)

    clear = Button(text=CLEAR_TEXT, command=lambda:clean_all_spinboxes(spinboxes))
    clear.grid(row=9, column=2)

    window.mainloop()
