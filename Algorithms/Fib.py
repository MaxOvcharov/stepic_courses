def fib(n):
    # If n = 0 or n = 1 return n 
	if n <= 0:
		return n
	cur = 1
	priv = 0
    # Return value of n Fib number
	for i in range(n):
		priv += cur
		priv, cur = cur, priv
	return cur


def main():
	# Run fib function
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
