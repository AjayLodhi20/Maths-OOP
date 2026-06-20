import numpy as np
from scipy import stats

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
frequency = [1, 8, 28, 56, 70, 56, 28, 8, 1]

raw_data = np.repeat(x, frequency)

print(f"Actual mean: {np.mean(raw_data)}")
print(f"2nd central moment(variance): {stats.moment(raw_data, moment = 2)}")
print(f"3rd central moment: {stats.moment(raw_data, moment = 3)}")
print(f"4th central moment:{stats.moment(raw_data, moment= 4)}")