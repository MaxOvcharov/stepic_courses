def f(*args):
    result = 0
    for arg in args:
        if hasattr(arg, '__len__'):
            result += f(*arg)
        else:
            result += arg
    return result

print f(1, 2, 3)
print f([1, 2, 3,])
print f((3, 5, 6,))
print f(3, (5, 6,))