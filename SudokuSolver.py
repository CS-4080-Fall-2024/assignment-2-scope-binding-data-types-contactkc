class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place  instead.
        """
        # We will approach this with a backtracking algorithm as well as checking if placing a number at a (row, col) is valid

        # Checks if placing a num at (row, col) is valid
        def isValid(board, row, col, num):
            # Duplicate check in the rows and cols
            for i in range(9):
                # Checks if number is already in same row or column
                if board[row][i] == num or board[i][col] == num:
                    return False
                # Checks a 3x3 square for duplicates
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True
        
        # Now we will implement backtracking in order to fill up the board
        def backtracking(board):
            # Iterates through all the cells in 9x9 matrix
            for row in range(9):
                for col in range(9):
                    # If cell = '.' then it is empty
                    if board[row][col] == '.':
                        # Try each number from 1-9
                        for num in '123456789':
                            # Uses isValid to check if it is valid to place there
                            if isValid(board, row, col, num):
                                board[row][col] = num
                                #  Recursive call to backtracking to solve and if it is return True
                                if backtracking(board):
                                    return True
                                # Resets the cell with '.' if the number placed doesn't lead to solution
                                board[row][col] = '.'
                        # If no number can be placed we return Faalse
                        return False
            # Returns true when entire board is solved
            return True
        
        backtracking(board)