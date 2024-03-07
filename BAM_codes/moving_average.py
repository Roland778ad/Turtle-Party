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
def peak_filter(data, sec):
    peak_list = []
    for peaks in range(len(data)):
        if peaks < sec or peaks + sec >= len(data):
            continue
        if max(data[peaks - sec : peaks]) < data[peaks] and max(data[peaks+1 : peaks + sec +1]) <= data[peaks]:
            peak_list.append(data[peaks])
    return peak_list
# 2
# n is the length of the moving section
# Should need annotation for NO negative and/or decimal input numbers.
def moving_average(movdata, n):
    mov_avg_lst = []
    for span in range(len(movdata)):
        if span + n > len(movdata):
            continue
        avg = sum(movdata[span : span + n]) / len(movdata[span : span + n])
        print(movdata[span : span + n], avg)
        mov_avg_lst.append(avg)
    return mov_avg_lst

# 3
def peak_mov_avg(data, peak_sec, avg_sec):
    peak_data = peak_filter(data, peak_sec)
    return moving_average(peak_data, avg_sec)

data = [149, 151, 155, 150, 153, 152, 155, 155, 155, 154, 165, 164, 175, 172, 168]
sec = 2
movsec = 2
print(peak_mov_avg(data, sec, movsec))