def print_array(arr,i):
    if i==len(arr):
        return
    else:
        print(arr[i],end=" ")
        print_array(arr, i+1)
        
arr=[1,2,2,4,8,4]
print_array(arr, 0)