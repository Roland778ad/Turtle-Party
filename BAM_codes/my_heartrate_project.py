# Coursera - Programming Fundamentals
# by Roland Udvari
# 2024-03-06

# --------------> Heart Rate Project <----------------------
# set count to 0
# for every data point (x) in data
# check if data point (x) is equal or above 'low' and below 'high'
# increase count
def time_in_zone(data, low, high):
    count = 0
    for x in data:
        if x >= low and x < high:
            count += 1
            pass
        pass
    return count

    # set count to 0
    # for every data point (x) in length of data
    # check if datapoint is peak
    # if yes increase count
    # otherwise continue checking

def peak_heartrate(data):
    peak_count = 0
    for x in range(len(data)):
        if is_peak_at(x, w) is True:
            peak_count += 1
            pass
        pass
    return peak_count

# set the definition of 'peak'
# i is at least w (2) enough points from left
# i is less than data-w (2) enough points from right
# data[i] is larger than w points to its left
# data[i] is larger than w points to its right

def is_peak_at(sec, w):
    if sec < w or sec >= len(data)-w:
        return False
    for x in range(1, w + 1):
        if data[sec] > data[sec - x] and data[sec] >= data[sec + x]:
            continue
        else:
            return False
    return True

data = [149, 151, 155, 150, 153, 152, 155, 155, 155, 154, 165, 164, 175, 172, 168]
w = 2
print(time_in_zone(data, 150, 165))
print(peak_heartrate(data))
print(is_peak_at(6, 3))