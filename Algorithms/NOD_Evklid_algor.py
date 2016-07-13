def gcd(a, b):
	# Evklid's Algoritm 
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    elif b == 0:
        return a


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()