import threading
import time
from math import pi, sin, cos, factorial

Iterations = 1000000

def calculate_sum():
    x = 10  # Ein relativ hoher Wert für x in der Exponentialreihe
    result_sum = []
    addition = 0
    for i in range(1, Iterations):
        addition += 1/i
        result_sum.append(addition)
    return result_sum


def multi():
    x = 1  # x = 1 für arctan(1) = Pi / 4
    result_multi = []
    multiplication = 1
    for i in range(1, Iterations):
        term = ((-1)**(i-1)) * (x**(2*i-1)) / (2*i-1)
        multiplication *= term
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
    print(time_delta1, 'seconds for multi-threaded execution', '\n')

    time_delta2 = main_single_threaded()
    print(time_delta2, 'seconds for single-threaded execution', '\n')

    print('_' *100)
    print(time_delta1, 'Multithreaded')
    print(time_delta2, 'Single threaded')