class Matrix:
    def __init__(self, row, column, type):
        if isinstance(row, list):
            self.row = row
        if isinstance(column, list):
            self.column = column
        self.two_d = type


    def