import threading, numpy as np, time
from math import pi, sin, cos, factorial


Iterations = 10000

def calculate_sum():
    result_sum = []
    addition = 0
    for i in range(1, Iterations):
        addition += sin(pi * i) / cos(pi / i)
        result_sum.append(addition)
    return result_sum


def multi():
    result_multi = []
    multiplication = 1
    for i in range(1, Iterations):
        multiplication *= (1 + 1/i)**i
        result_multi.append(multiplication)
    return result_multi


def main_multi_threaded():

    start1 = time.time()

    thread1 = threading.Thread(target=lambda: print(calculate_sum()))
    thread2 = threading.Thread(target=lambda: print(multi()))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end1 = time.time()
    time_delta1 = end1 - start1

    return time_delta1

def main_single_threaded():

    start2 = time.time()

    sum_result = calculate_sum()
    multi_result = multi()

    print(sum_result)
    print(multi_result)

    end2 = time.time()
    time_delta2 = end2 - start2

    return time_delta2

if __name__ == "__main__":


    time_delta1 = main_multi_threaded()
    print(time_delta1, 'Multi_threaded result in seconds', '\n')

    time_delta2 = main_single_threaded()
    print(time_delta2, 'Single_threaded result in seconds', '\n')



