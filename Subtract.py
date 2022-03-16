def Subtractor(*args):
    if len(args) == 1:
        return args[0]
    print(args[0])
    print(args[1:])
    return args[0] - sum(args[1:])

