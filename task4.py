import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_ui()

    def create_ui(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col, padx=1, pady=1)
                self.entries[row][col] = entry

        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=9, pady=10)

    def get_grid(self):
        grid = []
        for row in self.entries:
            grid_row = []
            for entry in row:
                val = entry.get()
                if val.isdigit() and 1 <= int(val) <= 9:
                    grid_row.append(int(val))
                else:
                    grid_row.append(0)
            grid.append(grid_row)
        return grid

    def set_grid(self, grid):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if grid[i][j] != 0:
                    self.entries[i][j].insert(0, str(grid[i][j]))

    def solve(self):
        grid = self.get_grid()
        if self.solve_sudoku(grid):
            self.set_grid(grid)
        else:
            messagebox.showerror("Error", "No solution exists for the given Sudoku.")

    def is_valid(self, grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_sudoku(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve_sudoku(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()