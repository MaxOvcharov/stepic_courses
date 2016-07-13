import sys

from bisect import bisect_left
from bisect import bisect_right

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
    
def quickSortHelper(alist,first,last):
    if first<last:
        # Run splitpoint finder
        splitpoint = partition(alist,first,last)
        # Recursive run QuickSort fo the left side
        quickSortHelper(alist,first,splitpoint-1)
        # Recursive run QuickSort fo the rigth side
        quickSortHelper(alist,splitpoint+1,last)

# Find place of the pivot 
def partition(alist,first,last):
    pivotvalue = alist[first]
    
    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        
        while leftmark <= rightmark and \
                alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and \
                rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

def main():
    # Read all data fron input
    reader = (list(map(int,line.split())) for line in sys.stdin)
    # Save number of lines and points
    line, point = next(reader)
                              
    alist = []

    # Lists of end-points and start-points
    salist = []
    ealist = []

    for i in range(line):
        alist.append(next(reader))
        ealist.insert(i, int(alist[i][1]))
        salist.insert(i, int(alist[i][0]))
        
    points = next(reader)
    # QuickSort of start-points
    quickSort(salist)
    # QuickSort of end-points
    quickSort(ealist)

    out = []
    for i in range(len(points)):
        # Find numbers of start-point which are bigger than point
        a =  bisect_right(salist, int(points[i]))
        # Find numbers of end-point which are les than point
        b =  bisect_left(ealist, int(points[i]))
        # Find numbers of line which are include that point
        out.append(str(a - b))

    print (' '.join(out))  

main()