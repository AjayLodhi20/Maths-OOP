from collections import Counter

ung_data = [12, 15, 18, 15, 21, 15, 18, 24, 12, 19]

grp_data ={
    "Class_Interval": ["10-20", "20-30", "30-40", "40-50", "50-60"],
    "Frequency": [4, 8, 12, 7, 3]
}

# Both 15 and 18 appear exactly 3 times, which is the highest frequency.
bimodal_ung_data = [12, 15, 18, 15, 21, 15, 18, 24, 12, 18]

bimodal_grp_large = {
    "Class_Interval": ["0-10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80"],
    "Frequency": [5, 12, 25, 14, 25, 16, 8, 3]
}

class Mode:
    def __init__(self, data):
        self.data = data

    def calculate(self):
        if isinstance(self.data, list):
            return self.calc_ung_data()
        if isinstance(self.data, list) and self.is_bimodal == True:
            return self.bi_ung()
        if isinstance(self.data, dict) and len(self.data) == 2:
            return self.calc_grp_data()
        if isinstance(self.data, dict) and len(self.data) == 2 and self.is_bimodal == True:
            return self.bi_grp()
        return "no output is given"


    def is_bimodal(self, data):
        """check whether data is bimodal or not."""
        #whether ungrouped data is bimodal or not
        if isinstance(data, list):
            frequencies = Counter(data)
            maximum = max(frequencies.values())
            check = [num for num, values in frequencies.items() if frequencies.values() == maximum]
            if len(check) == 2:
                return True
        # whether grouped data is bimodal or not
        if isinstance(data, dict) and len(data) == 2:
            frequencies1 = Counter(data['Frequency'])
            maximum1 = max(frequencies1.values())
            check = []
            for i in data.values():
                if i == maximum1:
                    check.append(i)
            if len(check) > 1:
                return True
        return False

    def median(self):
        """solve bimodal ungrouped data..."""
        sorted_list = sorted(self.data)
        if len(sorted_list) % 2 == 0:
            first_no = sorted_list[len(sorted_list)//2 -1]
            second_no = sorted_list[len(sorted_list)//2]
            median = (first_no + second_no)/2
            return median
        else:
            number = int(len(sorted_list)//2)
            return sorted_list[number]


    def bi_ung(self):
        median = self.median()
        mean = sum(self.data) / len(self.data)
        mode = 3*median - 2*mean
    # check which formula should be used based on the data provided

    def calc_ung_data(self):
        maximum = Counter(self.data)
        hello = max(maximum.values())
        mode = [k for k, v in maximum if v == hello]
        return mode

    def calc_grp_data(self):
        max_freq = max(self.data['Frequency'])
        max_index = self.data['Frequency'].index(max_freq)
        class_interval = self.data['Class_Interval'][max_index]
        integer = list(map(int, class_interval.split('-')))
        l = integer[0]
        f1 = max_freq
        f0 = self.data['Frequency'][max_index -1]
        f2 = self.data['Frequency'][max_index + 1]
        h = integer[1] - integer[0]
        mode = l + ((f1-f0)/(2*f1-f0-f2))*h
        return mode

    def bi_grp(self):
        n = len(self.data['Frequency'])
        col1 = self.data['Frequency'][:]
        col2 = [sum(col1[i:i+2])for i in range(0, n-1, 2)]
        col3 = [sum(col1[i:i+2])for i in range(1, n-1, 2)]
        col4 = [sum(col1[i:i+3])for i in range(0, n-2, 3)]
        col5 = [sum(col1[i:i+3])for i in range(1, n-2, 3)]
        col6 = [sum(col1[i:i+3])for i in range(2, n-2, 3)]

    def maximum(self, class_interval , column):
        largest_classes= []
        largest_frequency = 0

        for frequency, classes in zip(class_interval, column):
            if frequency > largest_frequency:
                largest_frequency = frequency
                largest_classes.append(classes)
            elif frequency == largest_frequency:
                largest_classes.append(classes)
            



