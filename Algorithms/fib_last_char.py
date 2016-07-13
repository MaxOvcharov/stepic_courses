def fib_last_char(n):
    # If n = 0 or n = 1 return n 
	if n <= 1:
		return n
	cur = 1
	priv = 0
	num = 1
    # Return last char of n Fib number
    while cur != n:
		priv += cur
		priv, cur = cur, priv
		num += 1
	return num % 10


def main():
	# Run fib function
    n = int(input())
    print(fib_last_char(n))


if __name__ == "__main__":
    main()
