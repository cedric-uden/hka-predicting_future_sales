import time


def time_runtime(fun):
    """
    Pass a function to and print the execution time of the function.
    Return the return value of the originally called function at the end.
    """
    start = time.time()
    val = fun()
    end = time.time()
    print(f"Runtime: {end - start}")
    return val
