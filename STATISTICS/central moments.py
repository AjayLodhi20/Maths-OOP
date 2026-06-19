# μ

x_o = [0, 1, 2, 3, 4, 5, 6, 7, 8]
frequency_o = [1, 8, 28, 56, 70, 56, 28, 8, 1]
assumed_mean = 4

class CentralMoments:
    def __init__(self, x, frequency, origin):
        self.x = x
        self.frequency = frequency
        self.a = origin

    def d(self):
        """find the d which is x-a"""
        d= [x-self.a for x in self.x]
        return d

    def mu1_prime(self):
        mu_prime = [f * d for f,d in zip(self.frequency, self.d())]
        new_mu1 = sum(mu_prime) / sum(self.frequency)
        return new_mu1

    def mu2_prime(self):
        mu2_prime = [f*d**2 for f,d in zip(self.frequency, self.d())]
        mu2_prime_o = sum(mu2_prime) / sum(self.frequency)
        return mu2_prime_o

    def mu3_prime(self):
        mu3_prime = [f*d**3 for f,d in zip(self.frequency, self.d())]
        mu3_prime_o = sum(mu3_prime) / sum(self.frequency)
        return mu3_prime_o

    def mu4_prime(self):
        mu4_prime = [f*d**4 for f,d in zip(self.frequency, self.d())]
        mu4_prime_o = sum(mu4_prime) / sum(self.frequency)
        return mu4_prime_o

    def mu1(self):
        mu1 = 0
        return mu1

    def mu2(self):
        mu2 = self.mu2_prime() - self.mu1_prime()**2
        return mu2

    def mu3(self):
        mu3 = self.mu3_prime() - 3*self.mu2_prime()*self.mu1_prime() + self.mu1_prime()**3
        return mu3

    def mu4(self):
        mu4 = self.mu4_prime() - 4*self.mu3_prime()*self.mu2_prime() + 6*self.mu2_prime()*self.mu1_prime()**2 - 3*self.mu1_prime()**4
        return mu4
all_central_moments = CentralMoments(x_o, frequency_o, assumed_mean)
print(all_central_moments.mu2())
print(all_central_moments.mu3())
print(all_central_moments.mu4())