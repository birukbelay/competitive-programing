def bigV(n):
    j=0
    for i in range(n-1):
        print(" "*j,"\\", " "* ((n*2)-4), "/")  
        
        n=n-1
        j=j+1
    print(" "*j,"\\/")
    

# def pos(n):
#     if n<0:
#         return 0       
# # # print("."," "*4,"...")4
bigV(6)
