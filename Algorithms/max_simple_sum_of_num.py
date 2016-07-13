def fun_sum(num):
    summ, count, temp = 0, 0, 0
    res = []  
    for i in range(num):
        # Summ numbers while remainder >= 2*i+1
        if num - summ >= 2*i+1:
            summ +=i+1
            res.append(str(i+1))
            count += 1
            continue
        else:
            # If the number already exists
            if str(num - summ) in res:
                res[i-1] = str(int(res[i-1]) + (num - summ))
                break
           	# otherwise put number - summ of numbers
            else:                
                res.append(str(num - summ))
                count += 1
                break            
    return count, res
 
def main():
    n = int(input())
    return fun_sum(n)

if __name__ == "__main__":
    output = main()
    print (output[0])
    print (' '.join(output[1]))