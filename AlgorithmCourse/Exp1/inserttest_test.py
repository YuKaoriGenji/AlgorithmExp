import insertsort
import random
import numpy as np
import time


def random_int_list(start,stop,length):
    start,stop=(int(start),int(stop)) if start<= stop else (int(stop),int(start))
    length=int(abs(length)) if length else 0
    random_list=[]
    for i in range(length):
        random_list.append(random.randint(start,stop))
        
    return random_list
    
print("This is YukaoriGenji's sort algorithm test battlefield\n")

print("ほんじつのアシスト教授は insert sort")
arr=[1,4,2,3,6,6,43,6,8,45,3,1,53,7,45,3,64,7,10000,999999,44,2,8,5,3,7]
print("example initial array:\n",arr)
insertsort.InsertSort(arr)
print("example result array:\n",arr)
arr1=random_int_list(1,1000000,length=1000)
#print("initial array next\n",arr1)
print("array's size",len(arr1))
print("さあ、ゲームが始めよ!")
time_start=time.time()
insertsort.InsertSort(arr1)
print("終わりましたよ\＿＿嘘です！びっくりした？")
time_end=time.time()
print("running time= ",time_end-time_start,'s')

arr1=random_int_list(1,1000000,length=10000)
#print("initial array next\n",arr1)
print("array's size",len(arr1))
print("さあ、ゲームが続けよ!")
time_start=time.time()
insertsort.InsertSort(arr1)
print("しばらくお休みをしてくださいませ")
time_end=time.time()
print("running time= ",time_end-time_start,'s')

arr1=random_int_list(1,1000000,length=50000)
#print("initial array next\n",arr1)
print("array's size",len(arr1))
print("未だ未だ続けてるよ!")
time_start=time.time()
insertsort.InsertSort(arr1)
print("終わりませんけどね")
time_end=time.time()
print("running time= ",time_end-time_start,'s')

arr1=random_int_list(1,1000000,length=100000)
#print("initial array next\n",arr1)
print("array's size",len(arr1))
print("つづき")
time_start=time.time()
insertsort.InsertSort(arr1)
print("中断します")
time_end=time.time()
print("running time= ",time_end-time_start,'s')

arr1=random_int_list(1,1000000,length=200000)
#print("initial array next\n",arr1)
print("array's size",len(arr1))
print("さあ、ゲームが始めよ!　それはただの繰り返す")
time_start=time.time()
insertsort.InsertSort(arr1)
print("もうはや")
time_end=time.time()
print("running time= ",time_end-time_start,'s')

arr1=random_int_list(1,1000000,length=500000)
#print("initial array next\n",arr1)
print("array's size",len(arr1))
print("さあ、ゲームが始めよ!　それはただの繰り返す")
time_start=time.time()
insertsort.InsertSort(arr1)
print("しばらくお待ちください")
time_end=time.time()
print("running time= ",time_end-time_start,'s')

arr1=random_int_list(1,1000000,length=1000000)
#print("initial array next\n",arr1)
print("array's size",len(arr1))
print("夢の始める場所!")
time_start=time.time()
insertsort.InsertSort(arr1)
print("終わりましたよ!それは本間")
time_end=time.time()
print("running time= ",time_end-time_start,'s')


