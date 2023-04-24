from functools import lru_cache
import pandas as pd
import matplotlib.pyplot as plt
import time


def fibonacci_direct(n):
    if n <= 1:
        return n
    else:
        fib_prev = 0
        fib_curr = 1
        for i in range(2, n+1):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr


def fibonacci_recursive(n):
    """ recursion calls itself until it hits one of these digits"""
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_memo(n-1) + fibonacci_memo(n-2)


def run_batch_tests():
    algorithms = [fibonacci_direct, fibonacci_recursive, fibonacci_memo]
    sizes = [10, 20, 40, 50]

    result = []
    print(f"{'Algorithms':<20} {'n':<10} {'Time elapsed':<15}")
    print("-" * 45)
    for algorithm in algorithms:
        for n in sizes:
            start_time = time.perf_counter()
            algorithm(n)
            stop_time = time.perf_counter()
            elapsed_time = stop_time - start_time
            print(f"{algorithm.__name__:<20} {n:<10} {elapsed_time:<15}")
            result.append({
                'Algorithm': algorithm.__name__,
                'n': n,
                'Time': elapsed_time
            })

    df = pd.DataFrame(result)

    fig, ax = plt.subplots()
    for algorithm in algorithms:
        ax.plot(df[df['Algorithm'] == algorithm.__name__]['n'],
                df[df['Algorithm'] == algorithm.__name__]['Time'],
                label=algorithm.__name__)
    ax.set_xlabel('n')
    ax.set_ylabel('Time (s)')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    run_batch_tests()

"""
--- sample run #1 ---
Algorithms           n          Time elapsed   
---------------------------------------------
fibonacci_direct     10         4.538000212050974e-06
fibonacci_direct     20         4.408007953315973e-06
fibonacci_direct     40         5.3919939091429114e-06
fibonacci_direct     50         7.0789974415674806e-06
fibonacci_recursive  10         4.0108003304339945e-05
fibonacci_recursive  20         0.0035407579998718575
fibonacci_recursive  40         45.24622123700101
fibonacci_recursive  50         5333.852696133006
fibonacci_memo       10         0.00014287899830378592
fibonacci_memo       20         3.818000550381839e-06
fibonacci_memo       40         3.366099554114044e-05
fibonacci_memo       50         1.9398998119868338e-05
"""