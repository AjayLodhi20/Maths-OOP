import pprint



# how to add or subtract row

# how to switch row in the matrix
class RowOperations:
    def __init__(self, rows):
        self.rows = rows


    def __str__(self):
        return pprint.pformat(self.rows, width = 16)


    def switching_rows(self, row1, row2):
        self.rows[row1], self.rows[row2] = self.rows[row2], self.rows[row1]
        return self.rows

    # multiply or divide a row by constant
    def scaler_multiply(self, number):
        self.rows = [[i * number for i in a] for a in self.rows]
        return self.rows

    def addition(self, number):
        self.rows = [[number + a for a in i]for i in self.rows]
        return self.rows



mat = RowOperations([[1,2,3], [4,5,6]])
print(mat)
mat.switching_rows(0,1)
print(mat)
mat.scaler_multiply(2)
print(mat)
mat.addition(3)
print(mat)


