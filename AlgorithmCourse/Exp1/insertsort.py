def InsertSort(arr):
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            temp=arr[i]
            index=i
            while index>0 and arr[index-1]>temp:
                arr[index]=arr[index-1]
                index-=1
            arr[index]=temp
    return
