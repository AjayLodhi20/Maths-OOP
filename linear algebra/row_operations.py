import pprint


# multiply or divide a row by constant
# how to add or subtract row

# how to switch row in the matrix
class RowOperations:
    def __init__(self, *rows):
        self.rows = rows


    def __str__(self):
        return pprint.pformat(self.rows, width = 16)


    def switching_rows(self, row1, row2):
        self.rows[row1], self.rows[row2] = self.rows[row2], self.rows[row1]
        return self.rows


mat = RowOperations([1,2,3], [4,5,6])
print(mat)
mat.switching_rows(0,1)
print(mat)




