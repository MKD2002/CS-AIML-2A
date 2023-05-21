def print_rev_array(arr,i):
    if i<0:
        return
    else:
        print(arr[i],end=" ")
        print_rev_array(arr, i-1)
        
arr=[1,2,2,4,8,4]
print_rev_array(arr, len(arr)-1)