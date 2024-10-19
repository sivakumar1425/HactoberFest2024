def solve_n_queens(n):
    # Helper function to check if it's safe to place a queen at position (row, col)
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check upper right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    # Backtracking function to find all solutions
    def backtrack(board, row):
        if row == n:
            # Found a valid solution
            solution = [''.join(board[i]) for i in range(n)]
            results.append(solution)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'  # Place a queen
                backtrack(board, row + 1)  # Try to place the next queen
                board[row][col] = '.'  # Backtrack and remove the queen

    results = []
    board = [['.' for _ in range(n)] for _ in range(n)]  # Initialize an empty board

    backtrack(board, 0)  # Start backtracking from the first row
    return results

# Example usage:
if __name__ == "__main__":
    N = int(input("Enter the value of N: "))  # Input for size of board
    solutions = solve_n_queens(N)
    
    if solutions:
        print(f"Total solutions for {N}-Queens problem: {len(solutions)}")
        for solution in solutions:
            for row in solution:
                print(row)
            print()  # Print a blank line between solutions
    else:
        print(f"No solution exists for {N}-Queens problem")
