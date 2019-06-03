def merge(left,right):
    i,j=0,0
    result=[]
    while i< len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def MergeSort(lst):
    if len(lst)<=1:
        return lst
    middle =int(len(lst)/2)
    left=MergeSort(lst[:middle])
    right=MergeSort(lst[middle:])
    return merge(left,right)
