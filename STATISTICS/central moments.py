# μ
class CentralMoments:
    def __init__(self, X, frequency):
        self.X = X
        self.frequency = frequency

    def d(self, A):
        d= [x-A for x in self.X]
        return d

    def μ1_prime(self):
        μ1_prime = list(map(self.d(A), self.frequency))

    def μ

