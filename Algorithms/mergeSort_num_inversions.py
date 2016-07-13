def mergeSort(alist):
    global count
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i, j, k, a = 0, 0, 0, 0
        # Compare elements of left_list and right_list
        while i < len(lefthalf) and j < len(righthalf):
            # If element of left_list less than right_list 
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i+=1
                                
            else:
                alist[k]=righthalf[j]
                j+=1
                count += len(lefthalf) - i
            k+=1           
        # Append the remainder of the left_list
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i+=1
            k+=1            
        # Append the remainder of the right_list
        while j<len(righthalf):
            alist[k]=righthalf[j]
            j+=1
            k+=1
          
        return count
    
num = input()
count = 0
A = list(map(int, input().split()))
print (mergeSort(alist))