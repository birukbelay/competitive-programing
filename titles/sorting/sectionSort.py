def selectionSort(n, arr):   
    
    for i in range(n):
        min=i
        for j in range(i,n):
            if arr[j]< arr[min]:
                print("swap",arr[j], arr[min] )
                min=j
        print(arr, i)
        arr[i], arr[min]=arr[min], arr[i]
    print("mm",arr)
    return arr
# print(selectionSort(5, [5,4,3,2,1]))
           
            

        
        
# class Solution:
    
def select( arr, i):        
    min = i
    for j in range(i, len(arr)):
        if arr[j] < arr[min]:
            # print("swap",arr[j], arr[min] )
            min=j
    print(arr)     
    return min
        

def selection_sort(arr,n):
    #code here
    for i in range(n):
        min=select(arr, i) 
        arr[i], arr[min]=arr[min], arr[i] 
        print("o", arr)        
        
            
print(selection_sort([5,4,3,2,1],5))