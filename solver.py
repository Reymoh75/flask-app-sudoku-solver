class Sudoku :

    def __init__(self,puzzle):
        self.puzzle = puzzle
    
    # puzzle = [
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9],
    # ]

    def is_valid(self,x,y,number):
        for i in self.puzzle[y]:
            if number == i:
                return False 
            
        for i in [self.puzzle[j][x] for j in range(9)]:
            if number == i:
                return False 
            
        x0 = (x//3)*3
        y0 = (y//3)*3
        for j in range(y0,y0+3):
            for i in range(x0,x0+3):
                if self.puzzle[j][i] == number:
                    return False

        return True

    def find_empty(self) :
        for j in range(9):
            for i in range(9):
                if self.puzzle[j][i] == 0:
                    return [i,j]            
        return False

    def solve(self):
        free = self.find_empty()
        if free == False :
            return True
        
        x = free[0]
        y = free[1]

        for number in range(1,10):
            if self.is_valid(x,y,number):
                self.puzzle[y][x] = number
                solve_result = self.solve()
                if solve_result:
                    return True
                self.puzzle[y][x] = 0      

    

    def show(self):
        print(self.puzzle)
        