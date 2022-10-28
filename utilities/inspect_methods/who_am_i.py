import inspect


def inspect_methods():
    return inspect.stack()[1][3]