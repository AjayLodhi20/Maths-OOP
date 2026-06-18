frequency_data_1 = [
    {"lower_limit": 0, "upper_limit": 10, "frequency": 5},
    {"lower_limit": 10, "upper_limit": 20, "frequency": 8},
    {"lower_limit": 20, "upper_limit": 30, "frequency": 12},
    {"lower_limit": 30, "upper_limit": 40, "frequency": 18},
    {"lower_limit": 40, "upper_limit": 50, "frequency": 7}
]

class Median:
    def __init__(self, data):
        self.data = data


    def dividing(self):
        lower = [i['lower_limit'] for i in self.data]
        upper = [i['upper_limit'] for i in self.data]
        frequency = [i['frequency'] for i in self.data]
        return lower, upper, frequency


    def x(self):
        lower, upper, _ = self.dividing()

        new_x = [(x+y)/2 for x,y in zip(lower,upper)]
        return new_x

    def cum_freq(self):
        _, _, frequency = self.dividing()
        cf = []
        loop = 0

        for i in range(len(frequency)):
            loop += frequency[i]
            cf.append(loop)
        return cf

    def n_by_2_for_further_calc(self):
        total_f = self.cum_freq()[-1]
        new_total = total_f / 2

        for_l = None
        for loop in self.cum_freq():
            if loop <= new_total:
                for_l = loop
            median_class = self.cum_freq().index(for_l) + 1
            median_class_2 = self.cum_freq()[median_class]
            lower, _, _ = self.dividing()
            lower_limit = lower[median_class + 1]
            _, upper, _ = self.dividing()
            upper_limit = upper[median_class + 1]
            return lower_limit, upper_limit, median_class_2
        return None





sol1 = Median(frequency_data_1)
print(sol1.cum_freq())
print(sol1.n_by_2_for_further_calc())