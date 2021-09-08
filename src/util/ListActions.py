from itertools import chain  # chain a list with another one


def cl(l, *args):
    """
    Chain List.

    Input a list and one or more arguments.
    Put the arguments into a list and chain the two lists together.
    """
    args_list = []
    for arg in args:
        args_list.append(arg)
    return list(chain(l, args_list)) if len(args_list) > 0 else None
