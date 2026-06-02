
class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def matrix(self):
        bn_mtrx = list(zip(*self.rows))
        return bn_mtrx

new_m = Matrix([[1,2,3,4], [5,6,7,8]])
print(new_m.matrix())
