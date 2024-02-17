import numpy as np
from math import pi, factorial, sin, cos
import threading

List_1 = []
List_2 = []
N = 100

def summation(list_target):
    sum_result = 0
    for i in range(1, 1001):
        for j in range(1, 1001):
            sum_result += sin(j) * (i**2) / (i**3)
    list_target.append(sum_result)
    print(list_target)

def series():
    new_series = 0
    for i in range(1, N):
        new_series += (-1)**i + (i) / (factorial(i))
    List_2.append(new_series)


    print(List_2)
print('_'*50)

    
def main():

    t1 = threading.Thread(target=summation, args=(List_1,))
    t2 = threading.Thread(target=series)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(List_1)
    print(List_2)

if __name__ == "__main__":
    main()
