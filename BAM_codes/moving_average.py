# Coursera - Programming Fundamentals
# by Roland Udvari
# 2024-03-06

# =================> Moving average <===========================
# THREE FUNCTIONS
    # 1 one to filter the data down to only the peaks
    # 2 one to take the N-second moving average
    # 3 one that gives the N-second moving average of just the peaks

# 1
# Data is the dataset, sec is the amount of time a datapoint has to be the peak compares to its neighbors
def get_only_peaks(data, w):
    peak_list = []
    for peaks in range(len(data)):
        if peaks < w or peaks + w >= len(data):
            continue
        if max(data[peaks - w : peaks]) < data[peaks] and max(data[peaks + 1 : peaks + w + 1]) <= data[peaks]:
            peak_list.append(data[peaks])
    return peak_list
# 2
# n is the length of the moving section
# Should need annotation for NO negative and/or decimal input numbers.
def find_moving_average(data, n):
    mov_avg_lst = []
    for span in range(len(data)):
        if span + n > len(data):
            continue
        avg = sum(data[span: span + n]) / len(data[span: span + n])
        print(data[span: span + n], avg)
        mov_avg_lst.append(avg)
    return mov_avg_lst

# 3
def moving_average_of_peaks(data, n, w):
    peak_data = get_only_peaks(data, n)
    return find_moving_average(peak_data, w)

data = [149, 151, 155, 150, 153, 152, 155, 155, 155, 154, 165, 164, 175, 172, 168]
sec = 2
movsec = 2
# print(moving_average_of_peaks(data, sec, movsec))
print(get_only_peaks([100, 105, 110, 115, 120, 115, 110, 120, 125, 120, 125, 120, 130, 135, 140, 135, 130], 2))
print(find_moving_average([120, 125, 140], 2))
moving_average_of_peaks([100, 105, 110, 115, 120, 115, 110, 120, 125, 120, 125, 120, 130, 135, 140, 135, 130], 2,1)