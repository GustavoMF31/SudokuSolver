from copy import deepcopy

INTEGERS = [1,2,3,4,5,6,7,8,9]

class SudokuException(Exception):
    """Basic Sudoku exception"""
    pass

class UnsolvableSudokuException(SudokuException):
    """Raised by an unsolvable Sudoku"""
    pass

class InvalidSudokuException(SudokuException):
    """Raised by a Sudoku with an invalid structure"""
    pass

class SudokuBoard:
    def __init__(self, rows):
        if len(rows) != 9:
            raise InvalidSudokuException(
                f"A Sudoku needs 9 rows, but {len(rows)} found")

        for index, row in enumerate(rows):
            if len(row) != 9:
                raise InvalidSudokuException(
                    f"""A Sudoku needs a combination of
                    numbers or 'None's totalizing 9 per row,
                    but got {len(row)} in row {row} at index {index}""")

        self.rows = rows
        self.subgrids = self.generate_subgrids()
        self.cols = self.generate_cols()
        
        if self.is_valid() != True:
            raise InvalidSudokuException("A Sudoku can't have 2 equal numbers on the same row, columns or subgrid")

    def is_complete(self):
        #True if the sudoku is completely filled with numbers
        #Not necessarily solved
        
        for row in self.rows:
            for number in row:
                if number is None:
                    return False
        return True

    def is_valid(self):
        #Checks if there are no repeated numbers
        #In the same row, column or subgrid
        
        for row in self.rows:
            for integer in INTEGERS:
                if row.count(integer) > 1:
                    return False

        for col in self.cols:
            for integer in INTEGERS:
                if col.count(integer) > 1:
                    return False

        for subgrid in self.subgrids:
            for integer in INTEGERS:
                if subgrid.count(integer) > 1:
                    return False

        return True

    @staticmethod
    def subgridize(three_rows):
        #Transforms three rows into three subgrids
        #111 222 333    111111111
        #111 222 333 -> 222222222
        #111 222 333    333333333
        
        subgrids = [[],[],[]]
        
        if len(three_rows) != 3:
            raise ValueError(f"Subgridize needs 3 rows, but got {len(three_rows)}")

        for subgrid_index in range(3):
            for row in three_rows:
                for num in row[subgrid_index * 3:(subgrid_index + 1) * 3]:
                    subgrids[subgrid_index].append(num)

        return subgrids
    
    def generate_subgrids(self):
        #Returns the board, reorganized into 3x3 subgrids
        subgrids = []

        #Iterate through the rows in groups of three
        for three_rows in [[self.rows[i],
                            self.rows[i+1],
                            self.rows[i+2]]
                           for i in range(0, 9 ,3)]:

            #Add each subgrid to the subgrids list
            for row in self.subgridize(three_rows):
                subgrids.append(row)
        
        return subgrids

    def generate_cols(self):
        #Returns the board, reorganized into columns
        cols = [[],[],[],[],[],[],[],[],[]]
        
        for i in range(9):
            for row in self.rows:
                cols[i].append(row[i])

        return cols
    
    def is_solved(self):
        #True if the Sudoku is solved
        
        for row in self.rows:
            for integer in INTEGERS:
                if row.count(integer) != 1:
                    return False

        for col in self.cols:
            for integer in INTEGERS:
                if col.count(integer) != 1:
                    return False

        for subgrid in self.subgrids:
            for integer in INTEGERS:
                if subgrid.count(integer) != 1:
                    return False

        return True

    def possible_numbers(self, y, x):
        #Returns wich numbers could occupy a specific tile

        possible_numbers = []

        #Add to the list each number that is
        for num in INTEGERS:
            #Not in the row
            if (num not in self.rows[y] and
                   #Not in  the column
                   num not in self.cols[x] and
                   #Not in the subgrid
                   num not in self.subgrids[x // 3 + (y // 3) * 3]):
                   
                possible_numbers.append(num)

        return possible_numbers
            
            
    def possibilities(self):
        #Returns the possible numbers for each tile
        possibilities = {}
        
        for y in range(9):
            for x in range(9):
                if self.rows[y][x] is None:
                    possible_numbers = self.possible_numbers(y, x)
                    possibilities[y, x] = possible_numbers

        return possibilities

    def solved(self):
        #Returns a solved version of the board
        
        least_possibilities_tile = () #(y, x)
        least_possibilities_tile_possibility_count = 10
        least_possibilities_tile_possibilities = []

        #For each empty tile
        for y in range(9):
            for x in range(9):
                if self.rows[y][x] is None:

                    #Get it's possible numbers
                    possible_numbers = self.possible_numbers(y, x)
                    possibility_count = len(possible_numbers)

                    #If no number is possible, it's unsolvable
                    if possibility_count == 0:
                        raise UnsolvableSudokuException
                    
                    #If there is just one possibility, it's the right one
                    #Return a solved sudoku with it
                    if possibility_count == 1:
                        new_rows = deepcopy(self.rows)
                        new_rows[y][x] = possible_numbers[0]
                        return SudokuBoard(new_rows).solved()
                    
                    #Keep track of the tile with the least possibilities
                    if possibility_count < least_possibilities_tile_possibility_count:
                        least_possibilities_tile = (y, x)
                        least_possibilities_tile_possibility_count = possibility_count
                        least_possibilities_tile_possibilities = possible_numbers

        #If with that process we completed the board, we are done
        if self.is_complete():
            return SudokuBoard(deepcopy(self.rows))

        #If that was't enough, start making assumptions.
        #If we end up with an unsolvable sudoku, the assumption was wrong

        #For each possibility of the tile with the least possibilities
        for possibility in least_possibilities_tile_possibilities:
            #Assume it's the right possibility and go from there
            try:
                assumption_rows = deepcopy(self.rows)
                y = least_possibilities_tile[0]
                x = least_possibilities_tile[1]
                assumption_rows[y][x] = possibility
                return SudokuBoard(assumption_rows).solved()
            
            #If we end up with an unsolvable Sudoku, try the next possibility
            except UnsolvableSudokuException:
                continue

        #If every possibility gives an unsolvable sudoku, the board is unsolvable
        raise UnsolvableSudokuException
