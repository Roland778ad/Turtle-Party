# from count_laps import is_peak_at


def find_moving_average(data, n):
    mov_avg_lst = []
    for span in range(len(data)):
        if span + n > len(data):
            continue
        avg = sum(data[span: span + n]) / len(data[span: span + n])
        mov_avg_lst.append(avg)
    return mov_avg_lst


def get_only_peaks(data, w):
    peak_list = []
    for peaks in range(len(data)):
        if peaks < w or peaks + w >= len(data):
            continue
        if max(data[peaks - w : peaks]) < data[peaks] and max(data[peaks + 1 : peaks + w + 1]) <= data[peaks]:
            peak_list.append(data[peaks])
    return peak_list


def moving_average_of_peaks(data, w, n):
    peak_data = get_only_peaks(data, n)
    return find_moving_average(peak_data, w)


# some functions to help with testing
def report_test(ans, expected):
    if ans == expected:
        print(" - correct:" + str(ans))
    else:
        print(" **INCORRECT** got " + str(ans) + " but expected " +
              str(expected))
        pass
    pass


def check_ma(data, n, expected):
    print("find_moving_average(" + str(data) + ", " + str(n) + ")")
    report_test(find_moving_average(data, n), expected)
    pass


def check_peaks(data, w, expected):
    print("get_only_peaks(" + str(data) + ", " + str(w) + ")")
    report_test(get_only_peaks(data, w), expected)
    pass


def check_ma_of_peaks(data, n, w, expected):
    print("moving_average_of_peaks(" + str(data) + ", " + str(n) + "," +
          str(w) + ")")
    report_test(moving_average_of_peaks(data, n, w), expected)
    pass


if __name__ == "__main__":
    # test with our basic example data
    data0 = [160, 161, 162, 161, 160, 161, 162, 163, 164, 163, 162]
    check_ma(data0, 4, [161, 161, 161, 161, 161.5, 162.5, 163, 163])
    check_peaks(data0, 2, [162, 164])
    check_ma_of_peaks(data0, 2, 2, [163])
    # trying to take the 3 element moving average of a 2 element list
    # gives the empty list
    check_ma_of_peaks(data0, 3, 2, [])
    # the one element moving average is just the data
    check_ma(data0, 1, data0)
    # test with the empty list
    data1 = []
    check_ma(data1, 1, [])
    check_peaks(data1, 1, [])
    check_ma_of_peaks(data1, 1, 1, [])
    # another list to test with
    data2 = [
        100, 105, 110, 115, 120, 115, 110, 120, 125, 120, 125, 120, 130, 135,
        140, 135, 130
    ]
    check_ma(data2, 5,
             [110, 113, 114, 116, 118, 118, 120, 122, 124, 126, 130, 132, 134])
    check_ma(data2, 10, [114, 116.5, 118, 120, 122, 124, 126, 128])
    check_peaks(data2, 1, [120, 125, 125, 140])
    check_peaks(data2, 2, [120, 125, 140])
    check_peaks(data2, 8, [])
    check_ma_of_peaks(data2, 2, 1, [122.5, 125, 132.5])
    check_ma_of_peaks(data2, 2, 2, [122.5, 132.5])
    pass
