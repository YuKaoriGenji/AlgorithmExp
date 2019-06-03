import math
import random

def HeapSort(input_list):
    def HeapAdjust(input_list,parent,length):
        temp=input_list[parent]
        child=2*parent+1

        while child<length:
            if child+1<length and input_list[child] < input_list[child+1]:
                child+=1
            if temp>input_list[child]:
                break
            input_list[parent]=input_list[child]
            parent=child
            child=2*child+1
        input_list[parent]=temp

    if input_list==[]:
        return []
    sorted_list=input_list
    length=len(sorted_list)

    for i in range(0,length//2)[::-1]:
        HeapAdjust(sorted_list,i,length)
    for j in range(1,length)[::-1]:
        temp=sorted_list[j]
        sorted_list[j]=sorted_list[0]
        sorted_list[0]=temp

        HeapAdjust(sorted_list,0,j)
        #print('%dth' %(length-j))
        #print(sorted_list)
    return sorted_list
