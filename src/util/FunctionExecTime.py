import time


def time_runtime(fun, *args, **kwargs):
    """
    Pass a function to and print the execution time of the function.
    Return the return value of the originally called function at the end.
    """
    start = time.time()
    val = fun(*args, **kwargs)
    end = time.time()
    runtime = end - start
    print_runtime = choose_parser(runtime)
    print(f"Runtime of function \"{fun.__name__}\": {print_runtime}")
    return val


def choose_parser(runtime):
    """
    Parse the runtime according to the corresponding scope.
    """
    if runtime < 0.001:
        return parse_nanoseconds(runtime)
    elif runtime < 1:
        return parse_milliseconds(runtime)
    elif runtime < 60:
        return parse_seconds(runtime)
    else:
        return parse_minutes(runtime)


def parse_nanoseconds(runtime):
    """
    Transform the runtime if the runtime is measured under a millisecond.
    """
    return f"{int(runtime * 1_000_000)}ns"


def parse_milliseconds(runtime):
    """
    Transform the runtime if the runtime is measured under a second.
    """
    return f"{int(runtime * 1000)}ms"


def parse_seconds(runtime):
    """
    Transform the runtime if the timing is under a minute.
    """
    return f"{int(runtime)}s"


def parse_minutes(runtime):
    """
    Transform the runtime if the timing exceeds a minute.
    """
    runtime = int(runtime)
    minutes = int(runtime / 60)
    seconds = runtime % 60
    return f"{minutes}min & {seconds}s"
