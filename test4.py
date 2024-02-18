import math
import numpy as np
import time
import matplotlib.pyplot as plt

start_time = time.time()

numbers = [_ for _ in range(1, 10000)]
n = 500_000
fib_n = 1000

def calculate_squares(numbers):
    result = [number ** 2 for number in numbers]
    return result

def find_primes(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Ausführen der Funktionen und Ausgabe der Ergebnisse
squares_result = calculate_squares(numbers)
print("Quadratzahlen:", squares_result)

primes_result = find_primes(n)
print(f"Primzahlen bis {n}:", len(primes_result))  # Anzahl der Primzahlen

fibonacci_result = fibonacci(fib_n)
print(f"Fibonacci-Zahlenreihe bis {fib_n}:", fibonacci_result[-1])  # Letzte Zahl in der Sequenz

# Berechnung der Gesamtdauer
end_time = time.time()
print("Gesamtlaufzeit:", end_time - start_time, "Sekunden")




    