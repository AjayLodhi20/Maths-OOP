# μ
class CentralMoments:
    def __init__(self, X, frequency):
        self.X = X
        self.frequency = frequency

    def d(self, a):
        """find the d which is x-a"""
        d= [x-a for x in self.X]
        return d

    def mu1_prime(self, a):
        mu_prime = [f * d for f,d in zip(self.frequency, self.d(a))]
        new_mu1 = sum(mu_prime) / sum(self.frequency)
        return new_mu1

    def mu2_prime(self, a):
        mu2_prime = [f*d**2 for f,d in zip(self.frequency, self.d(a))]
        mu2_prime_o = sum(mu2_prime) / sum(self.frequency)
        return mu2_prime_o

    def

