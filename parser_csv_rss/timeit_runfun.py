from timeit import Timer 
import random


def test1():
	# Concat
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
	# Append
    l = []
    for i in range(1000):
        l.append(i)

def test3():
	# Comprehension
    l = [i for i in range(1000)]

def test4():
	# List range
    l = list(range(1000))

# Run tests for timing list bulding
t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

# Run tests for timing pop method for zero and last element
popzero = Timer("x.pop(0)", "from __main__ import x")
popend = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print ("Pop zero element: ", popzero.timeit(number=1000))


x = list(range(2000000))
print ("Pop last element: ", popend.timeit(number=1000))

# Run tests for timing number in container (list VS dict)
for i in range(10000,1000001,20000):
    t = Timer("random.randrange(%d) in x"%i,
                     "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("Element: %d,    List time: %0.3f,    Dict time: %0.3f" % (i, lst_time, d_time))
