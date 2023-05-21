def get_max(arr,i,maximum):
    if i==len(arr)-1:
        return arr[i]
    else:
        maximum=max(arr[i],get_max(arr,i+1,maximum))
    return maximum
    
arr=[12,21,45,78,54,20]
maximum=get_max(arr,0,arr[0])
print(maximum)