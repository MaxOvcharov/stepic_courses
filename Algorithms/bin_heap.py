class BinHeap:
    def __init__(self):        
        self.heap = []

    def Insert(self, value):        
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)
        
    def siftUp(self, step):
       
        while self.heap[step] > self.heap[(step - 1) / 2] and step > 0:
            self.heap[step], self.heap[(step - 1) / 2] = self.heap[(step - 1) / 2], self.heap[step]  
            step = (step - 1) / 2
            
            
    def ExtractMax(self):        
        print (self.heap[0])
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop(len(self.heap) - 1)
        self.siftDown(0)
        
        
    def siftDown(self, dstep):
        while 2 * dstep + 1 < len(self.heap):
            left = 2 * dstep + 1             
            right = 2 * dstep + 2            
            j = left
            if right < len(self.heap) and self.heap[right] > self.heap[left]:
                j = right
            if self.heap[dstep] >= self.heap[j]:
                break
            self.heap[dstep], self.heap[j] =  self.heap[j],  self.heap[dstep]
            dstep = j
        
if __name__ == '__main__':
    # example
    bh = BinHeap()
    for i in range(int(input("How many steps you will be -> "))):
        b = raw_input("Enter next step: Insert (num) or ExtractMax  -> ").split()
        # If we need to Insert data
        if b [0] == "Insert":
            bh.Insert(int(b[1]))
            continue
        # If we need extract Max
        else:
            bh.ExtractMax()