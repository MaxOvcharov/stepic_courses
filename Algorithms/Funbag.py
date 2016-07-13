def funbag(bag, p):
    count = 0    
    for i in range(len(p)):
        # If bag != 0 and object volume < bag volume
        if p[i][1] <= bag[1] and bag[1] > 0:
            count += float(p[i][0])
            bag[1] -= p[i][1]
        # If bag != 0 and object volume > bag volume
        # put a part of the object to the bag                 
        elif p[i][1] > bag[1] and bag[1] > 0:
            # Find part of the object
            count += float(bag[1]* p[i][2])
            break
    return count
 
def main():
    n =list(map(int, input().split()))
    p = []
    for i in range(n[0]):
        p.append(list(map(int, input().split())))
        # Find the cost of kilogramms
        p[i].append(float(p[i][0])/float(p[i][1]))
    # Sort by cost of killogramm                      
    p.sort(key=lambda x: x[2], reverse= True)
    return funbag(n, p)
            
    
   

if __name__ == "__main__":
    print ('%0.3f' %main())