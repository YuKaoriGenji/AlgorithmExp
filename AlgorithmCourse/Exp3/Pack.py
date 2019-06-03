import numpy as np
import random
import time
class Commodity(object):
    def __init__(self,weight=None,value=None):
        super(Commodity,self).__init__()
        self.weight=weight
        self.value=value
class Accumu(object):
    def __init__(self,weight=None,value=None):
        super(Accumu,self).__init__()
        self.weight=weight
        self.value=value

class Node(object):
    def __init__(self,commodity=None,chosen=None,num=None,capac=None,val=None,maxval=None,left=None,right=None):
        super(Node,self).__init__()
        self.commodity=commodity
        self.num=num
        self.capac=capac
        self.val=val
        self.maxval=maxval
        self.chosen=chosen
        self.left=None
        self.right=None

class Tree(object):
    def __init__(self,root=None):
        self.root=root


class PackProb(object):
    def __init__(self,capacity=1):
        self.capacity=capacity
        self.length=10;
        self.status=[0 for x in range(self.length+1)]
        self.Good=[]
        self.temp=[]
        self.prop=[]
        self.tmp=0 #switch time
        self.brute=[]
        self.sum=0
        self.maxvalue=0
        self.root=""
        '''
        self.Good.append(Commodity(3,66))
        self.Good.append(Commodity(2,40))
        self.Good.append(Commodity(5,95))
        self.Good.append(Commodity(4,40))
        

        self.Good.append(Commodity(1,3))
        self.Good.append(Commodity(2,2))
        self.Good.append(Commodity(3,1))
        self.Good.append(Commodity(4,6))
        self.Good.append(Commodity(5,5))
        self.Good.append(Commodity(6,4))
        self.Good.append(Commodity(7,9))
        self.Good.append(Commodity(8,8))
        self.Good.append(Commodity(9,7))
        self.Good.append(Commodity(10,10))
        '''

        self.Good.append(Commodity(23,92))
        self.Good.append(Commodity(31,57))
        self.Good.append(Commodity(29,49))
        self.Good.append(Commodity(44,68))
        self.Good.append(Commodity(53,68))
        self.Good.append(Commodity(38,43))
        self.Good.append(Commodity(63,67))
        self.Good.append(Commodity(85,84))
        self.Good.append(Commodity(89,87))
        self.Good.append(Commodity(82,72))
       
        self.BackTrace=[]
        self.NodeQueue=[]


    def insertCommodity(self,weight,value):
        self.Good.append(Commodity(weight,value))
        self.length=self.length+1

    def removeCommodity(self,i):
        self.Good.remove(i)
        self.length=self.length-1

    def PrintCommodity(self):
        for i,_ in enumerate(self.Good):
            print("id:",i,"\t","weight:",self.Good[i].weight,"\tvalue",self.Good[i].value)
        print("\n")

    def Brute(self):#蛮力法
        nowBest=0
        self.times=2**len(self.Good)
        print(self.times)
        for i in range(self.times):
            self.temp=[]
            print(i)
            #Read the binary
            binary=bin(i).replace('0b',"")  #use binary number string to enumerate all situation
            binary=binary.zfill(len(self.Good))
            print(binary,"\tlength",len(binary))
            for j in range(len(binary)):
                if binary[j]=='1':
                    self.temp.append(self.Good[j])
            self.brute.append(self.temp)
        print("\n")


        #select
        self.temp=[]
        for l in range(len(self.brute)):
            Wei=0
            Val=0
            for p in range(len(self.brute[l])):
                Wei+=self.brute[l][p].weight
                Val+=self.brute[l][p].value
            print("weight:",Wei,"\tvalue:",Val)
            print('\n')
            self.temp.append(Accumu(weight=Wei,value=Val))
        for i in range(len(self.temp)):
            if(self.temp[i].weight<=self.capacity and self.temp[i].value>=self.temp[nowBest].value):
                nowBest=i

        print("\n")
        print("Total   weight:",self.temp[nowBest].weight,"\tvalue:",self.temp[nowBest].value,"\tcapacity:",self.capacity)
        for i in range(len(self.brute[nowBest])):
            print("weight:",self.brute[nowBest][i].weight,"\tvalue:",self.brute[nowBest][i].value)

    def Memo_Init(self):#备忘录方法
        self.temp=[]
        self.temp=[["" for x in range(self.capacity+1)] for y in range(self.length+1)] 

    def Memorization(self,n,c): #recursion
        print('n=',n,'\tc=',c)
        if(self.temp[n][c]!=""):
            return self.temp[n][c]
        bestP=0
        if(n==0):
            bestP=(self.Good[n-1].value if (c>=self.Good[n-1].weight) else 0)
        else:
            bestP=self.Memorization(n-1,c)
            print('n=',n,'\tc=',c)
            if(c>=self.Good[n-1].weight):
                bestP=max(bestP,self.Memorization(n-1,c-self.Good[n-1].weight)+self.Good[n-1].value)
        self.temp[n][c]=bestP
        self.sum=self.sum+1
        print(self.sum,': B[',n,'][',c,']=',self.temp[n][c])
        return bestP

        print("unfinished")

    def FindWhat(self,i,j):#动态规划方法
        if(i>=0):
            if(self.temp[i][j]==self.temp[i-1][j]):
                self.status[i]=0
                self.FindWhat(i-1,j)
            elif(j-self.Good[i-1].weight>=0 and self.temp[i][j]==self.temp[i-1][j-self.Good[i-1].weight]+self.Good[i-1].value):
                self.status[i]=1
                self.FindWhat(i-1,j-self.Good[i-1].weight)

    def Dynamic(self):
        self.temp=[]
        self.temp=[[0 for x in range(self.capacity+1)] for y in range(self.length+1)] 
        print(self.temp)
        for i in range(1,self.length+1):
            for j in range(1,self.capacity+1):
                if(j<self.Good[i-1].weight):# RUN the epoches
                    self.temp[i][j]=self.temp[i-1][j]
                    #print(self.temp)
                else:
                    #print("i=",i,"\tj=",j,"\tself.Good[i].weight=",self.Good[i-1].weight,"\t value=",self.Good[i-1].value)
                    self.temp[i][j]=max(self.temp[i-1][j],self.temp[i-1][j-self.Good[i-1].weight]+self.Good[i-1].value)
                    #print(self.temp)
        print(self.temp)
        self.FindWhat(self.length,self.capacity)
        print(self.status)

    def BTInit(self):#回溯法
        self.BackTrace=["" for x in range(self.length)]
        self.maxvalue=0;

    def BTSearch(self,i):
        weight=0
        value=0
        for j in range(i):
            if(self.BackTrace[j]==1):
                weight=weight+self.Good[j].weight
                value=value+self.Good[j].value

        if(i>=self.length):
            self.CheckMax()
        else:
            self.BackTrace[i]=1
            if(weight+self.Good[i].weight<=self.capacity and self.bound(i+1)>=self.maxvalue):
                self.BTSearch(i+1)
            self.BackTrace[i]=0
            if(self.bound(i+1)>=self.maxvalue):
                self.BTSearch(i+1)

    def CheckMax(self):
        weight=0
        value=0
        for i in range(self.length):
            if(self.BackTrace[i]==1):
                weight=weight+self.Good[i].weight
                value=value+self.Good[i].value
        if (weight<=self.capacity):
            if(value>=self.maxvalue): #Bounding Function
                self.maxvalue=value
                print("Max Value:",self.maxvalue)
                print("selected things(1 represented selected while 0 represented unselected)")
                for j in range(self.length):
                    print(self.BackTrace[j])

    def sort(self):
        self.temp=[]
        self.prop=["" for i in range(self.length)]
        for i in range(self.length):
            self.prop[i]=self.Good[i].value/self.Good[i].weight
        for i in range(self.length-1):
            for j in range(i+1,self.length):
                if self.prop[i]<self.prop[j]:
                    self.tmp=self.prop[i]
                    self.prop[i]=self.prop[j]
                    self.prop[j]=self.tmp

                    self.tmp=self.Good[i]
                    self.Good[i]=self.Good[j]
                    self.Good[j]=self.tmp

    def bound(self,depth):
        value_now=0
        weight_now=0
        for i in range(depth):
            if(self.BackTrace[i]==1):
                weight_now=weight_now+self.Good[i].weight
                value_now=value_now+self.Good[i].value
        left_weight=self.capacity-weight_now
        while depth<self.length:
            if(self.Good[depth].weight<=left_weight):
                left_weight-=self.Good[depth].weight
                value_now+=self.Good[depth].value
            if(self.Good[depth].weight>left_weight):
                value_now+=(self.Good[depth].value/self.Good[depth].weight)*left_weight
                left_weight=0
                break
            
            depth+=1
          
        return value_now

    def BranchBound(self,Node):
        print("\nin bound",Node.num)
        Node.maxval=Node.val
        capac=Node.capac
        print("capac:",capac)
        if(capac<0):
            Node.maxval=0
            return
        for j in range(Node.num+1,len(self.Good)-1):
            if(self.Good[j].weight<=capac):
                Node.maxval+=self.Good[j].value
                capac-=self.Good[j].weight
                print("capacity aru",capac,"maxval",Node.maxval)
            elif(self.Good[j].weight>capac):
                Node.maxval+=(self.Good[j].value/self.Good[j].weight)*capac
                capac=0
                print("capacity over",Node.maxval)
                print("out bound\n")
                return
            else:
                return
    def BranchInit(self):
        self.BackTrace=["" for x in range(self.length)]
        self.root=Node(commodity="start",num=-1,chosen=2,capac=self.capacity,val=0,maxval=0)


    def BranchSearch(self):
        self.BranchInit()
        self.BranchBound(self.root)
        self.Good.append(None)
        print(self.Good)
        node=self.root
        while(self.Good[node.num+1]!=None):
            temp_commodity=self.Good[node.num+1]
            temp_capac=(node.capac-self.Good[node.num+1].weight)
            temp_val=node.val+self.Good[node.num+1].value
            temp_num=node.num+1
            temp_chosen=1
            temp_maxval=0
            nodeB=Node(commodity=temp_commodity,capac=temp_capac,val=temp_val,chosen=temp_chosen,num=temp_num,maxval=temp_maxval)
            node.left=nodeB

            temp_commodity=self.Good[node.num+1]
            temp_capac=node.capac
            temp_val=node.val
            temp_num=node.num+1
            temp_chosen=0
            temp_maxval=0
            nodeC=Node(commodity=temp_commodity,capac=temp_capac,val=temp_val,chosen=temp_chosen,num=temp_num,maxval=temp_maxval)
            node.right=nodeC

            print("node.left.num",node.left.num)
            print("node.right.num",node.right.num)
            self.BranchBound(node.left)
            self.BranchBound(node.right)

            if(node.left.capac>=0):
                self.NodeQueue.append(node.left)
            if(node.right.capac>=0):
                self.NodeQueue.append(node.right)
            print("maxval:",node.left.maxval,node.right.maxval)

            self.NodeSort()
            node=self.NodeQueue.pop(0)
            print("node.number",node.num,"node.val",node.val)


    def NodeSort(self):
        self.temp=[]
        for i in range(len(self.NodeQueue)-1):
            for j in range(i+1,len(self.NodeQueue)):
                if self.NodeQueue[i].maxval<self.NodeQueue[j].maxval:
                    self.tmp=self.NodeQueue[i]
                    self.NodeQueue[i]=self.NodeQueue[j]
                    self.NodeQueue[j]=self.tmp
        print("\ntoday's NodeQueue")
        for i in range(len(self.NodeQueue)):
            print("self.NodeQueue[",i,"]:",self.NodeQueue[i].maxval)
        print("\n")

    def MonteCarlo(self):
        bestp=0
        for i in range(20000):
            leftc=self.capacity
            item=self.Good[:]
            presentvalue=0
            while True:
                key=random.choice(item)
                item.remove(key)
                if key.weight<=leftc:
                    presentvalue+=key.value
                    leftc-=key.weight
                else:
                    break
            if presentvalue>bestp:
                bestp=presentvalue
        print("MonteCarlo:Maximum value",bestp)

 
#---------------------------------------------------------------------------------
print("----------------------------Brute Way------------------------------------")
start_time=time.time()
a=PackProb(capacity=165)
print(a.Good[1].weight,"\n")
a.PrintCommodity()
a.Brute()
end_time=time.time()
print("Brute \ttime:",end_time-start_time)
print("--------------------------Dynamic---------------------------------------")
# test command
start_time=time.time()
b=[["" for x in range(3)] for y in range(5)]
b[2][1]=1
print(b)
print("\n")
a.Dynamic()
end_time=time.time()
print("Dynamic: \ttime:",end_time-start_time)
print("---------------------------Memorization------------------------------------------")
start_time=time.time()
a.Memo_Init()
print(a.temp)

a.Memorization(a.length,a.capacity)
print(a.temp[a.length-1][a.capacity])
end_time=time.time()
print("Memorization: \ttime:",end_time-start_time)
print("---------------------------Back Tracing------------------------------------------")
start_time=time.time()
a.sort()
a.BTInit()
a.BTSearch(0)
print("maxvalue:",a.maxvalue)
end_time=time.time()
print("BackTracing: \ttime:",end_time-start_time)
print("----------------------------Branch test------------------------------------------------")
start_time=time.time()
node=Node(commodity="start",num=-1,chosen=2,capac=a.capacity,val=0,maxval=0)
a.BranchBound(node)
print("node.maxval",node.maxval)
end_time=time.time()
print("Branch Test: \ttime:",end_time-start_time)
print("-----------------------Branch-Bound time 2019.5.29 20:49---------------------------------")
start_time=time.time()
a.sort()
a.BranchSearch()
end_time=time.time()
print("Branch-Bound: \ttime:",end_time-start_time)
print("----------------------------Monte Carlo-----------------------------------------------")
start_time=time.time()
a.Good.pop()
a.MonteCarlo()
end_time=time.time()
print("time:",end_time-start_time)
