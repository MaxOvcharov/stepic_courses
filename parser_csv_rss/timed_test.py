import time

def timed(f, *args, n_iter=100):
	acc = float("inf")
	for i in range(n_iter):
		t0 = time.perf_counter()
		f(*args)
		t1 = time.perf_counter()
		acc = min(acc, t1 -t0)
	return acc

