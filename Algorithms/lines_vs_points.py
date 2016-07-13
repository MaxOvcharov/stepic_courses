"""" We have sections and we want to know 
    what's the min number of points which 
    included in every sections"""


def funline(numline, p):    
    tempn = []
    tempn.append(str(p[0][1]))
    nextt = 0
    for i in range(len(p)-1):
        # check if next section in priv section,
        # if doesn't save this point 
        if p[i+1][0] <= int(tempn[nextt]) and p[i+1][1] >= int(tempn[nextt]):
            continue        
        else:
            nextt += 1
            tempn.append(str(p[i+1][1]))     
    return len(tempn),' '.join(tempn)
 
def main():
    n =int(input())
    p = []
    # input of values
    for i in range(n):
        p.append(list(map(int, input().split())))
    # sort sections by ends
    p.sort(key=lambda x: x[1])
    return funline(n, p)
   

if __name__ == "__main__":
    output = main()
    # Output of number of points and points
    for i in range(len(output)):
        print (output[i])