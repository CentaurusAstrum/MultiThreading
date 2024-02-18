import multiprocessing

def calculate_squares(numbers, queue):
    result = [number ** 2 for number in numbers]
    queue.put(result)

def sieve_of_eratosthenes(n, queue):
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    primes = [p for p in range(2, n) if prime[p]]
    queue.put(primes)

def fibonacci(n, queue):
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    queue.put(fib_sequence)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    numbers = [_ for _ in range(1, 1000)]
    n = 50 # Anpassung der Grenze für Primzahlen
    fib_n = 100

    processes = [
        multiprocessing.Process(target=calculate_squares, args=(numbers, queue)),
        multiprocessing.Process(target=sieve_of_eratosthenes, args=(n, queue)),  # Verwendung des optimierten Algorithmus
        multiprocessing.Process(target=fibonacci, args=(fib_n, queue)),
    ]

    # Starten der Prozesse
    for p in processes:
        p.start()

    # Auf die Beendigung der Prozesse warten
    for p in processes:
        p.join()

    # Ergebnisse aus der Queue auslesen und ausgeben
    results = [queue.get() for _ in processes]
    for result in results:
        print(result)
