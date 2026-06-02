
# multiply or divide a row by constant
# how to add or subtract row

# how to switch row in the matrix
class RowOperations:
    def __init__(self, *rows):
        self.rows = rows

    def __str__(self):
        return

    def switch_row(self, first, second):
        """switching the rows"""
        for row in range(len(self.rows)):
            if row == len(first):
                if row == second







rowop = RowOperations([[1,2,3],[4,5,6]])