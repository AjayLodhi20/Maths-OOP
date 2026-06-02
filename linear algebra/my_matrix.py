class Matrix:
    def __init__(self, row, column, type):
        if isinstance(row, list):
            self.row = row
        if isinstance(column, list):
            self.column = column

    def create_a_matrix(self):
        if len(self.row) == len(self.column):
            return self.matrix()
        raise ValueError("length of both should be same..")


    def matrix(self, row, column):

