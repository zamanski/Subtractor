def Subtractor(*args):
    if len(args) == 1:
        return args[0]
    return args[0] - sum(args[1:])


