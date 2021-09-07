def insertionsort(arr):
    for j in range(0,len(arr)):
        value=arr[j]
        i=j-1
        while i>=0 and value<arr[i]:
            arr[i+1]=arr[i]
            i=i-1
            arr[i+1]=value




arr=[3,2,1,4,5]  
insertionsort(arr)   
print("the sorted array is :") 
for j in range(len(arr)):
    print(arr[j])
   














    