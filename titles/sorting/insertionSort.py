def insertionSortReverse(n, l):
    current= 0
     
                
            
         
insertionSortReverse(5, [1, 2, 8,5, 3])
# help(range) 

def insertionSort(n,l):
    for i in range(n):
        ctr = n-1
        num= l[ctr]        
        while num <l[ctr-1]:
            l[ctr] = l[ctr-1]
            ctr=ctr-1        
            print(l)
        l[ctr]= num
    print(l)

insertionSort(5,[2, 4, 6, 8, 3])     
            
        