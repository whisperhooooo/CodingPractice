#1

# class Student(object):
	# def __init__(self, name, gender):
		# self.__name = name
		# self.__gender = gender
		
	# def get_name(self):
		# return self.__name
		
	# def get_gender(self):
		# return self.__gender
		
	# def set_gender(self, gender):
		# if gender != 'male' and gender != 'female':
			# print('wrong gender type!')
		# else:
			# self.__gender = gender
				
# bart = Student('Bart', 'male')
# jane = Student('Jane', 'female')

# # bart.name
# print(bart.get_name())
# print(bart.get_gender())
# #bart.set_gender ('female')
# bart.set_gender ('what')
# print(bart.get_gender())

#2

# class Animal(object):
	# def run(self):
		# print('Animal is runing...')
		
# class Dog(Animal):
	# def run(self):
	 # print('Dog is running...')
	
	
# class Cat(Animal):
	# pass
	
# class Tortoise(Animal):
	# def run(self):
		# print('Tortoise is running slowly...')
		
# class Timber(object):
	# def run(self):
		# print('Start...')
		
# def run_twice(animal):
	# animal.run()
	# animal.run()
	
# run_twice(Timber())


#3

#print(dir('abc'))
# print('abc'.__len__())
# print(isinstance([1,2,3],(list or tuple)))
# print(isinstance([1,2,3],(tuple or list)))


#4实例属性和类属性
# class Student(object):
	# cont = 0
	# def __init__(self, name):
		# self.name = name
		# Student.cont += 1
# Bart = Student('bart')
# Lisa = Student('lisa')
# print(Student.cont)


#5property装饰器
# class Screen(object):
	# @property
	# def width(self):
		# return self._width
	
	# @width.setter
	# def width(self,value):
		# self._width=value
	
	# @property
	# def height(self):
		# return self._height
		
	# @height.setter
	# def height(self,value):
		# self._height=value
		
	# @property
	# def resolution(self):
		# return self._width*self._height
		
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)

# class A(object):
    # def foo(self):
        # print('A foo')
    # def bar(self):
        # print('A bar')

# class B(object):
    # def foo(self):
        # print('B foo')
    # def bar(self):
        # print('B bar')

# class C1(A):
    # pass

# class C2(B):
    # def bar(self):
        # print('C2-bar')

# class D(C1,C2):
    # pass

# if __name__ == '__main__':
    # print(D.__mro__)
    # d=D()
    # d.foo()
    # d.bar()

	
#二维数据里找目标数
# -*- coding:utf-8 -*-
# class Solution():
    # # array 二维列表
    # def Find(self, target, array):
        # # write code here
        # rows=len(array)-1
        # cols=len(array[0])-1
        # i=rows
        # j=0
        # while i>=0 and j<=cols:
            # if array[i][j]<target:
                # j+=1
            # elif array[i][j]>target:
                # i-=1
            # else: 
                # return True
        # return False

# s = Solution()
# # s.target = 1
# # s.array = ([1,2],[3,4],[5,6])
# print(s.Find(7,([1,2],[3,4],[5,6])))

#字符串里的空格替换为20%
# class Solution:
	# def replaceSpace(self,s):
		# num=len(s)
		# tem=''
		# for i in range(num):
			# if s[i]==' ':
				# tem=tem+'%20'
			# else:
				# tem=tem+s[i]
		# return tem
# a=Solution()
# print(a.replaceSpace('We are happy'))

#从尾到投打印链表每个节点的值 递归
# class ListNode:
	# def __init__(self, x):
		# self.val = x
		# self.next = None

# class Solution:
	# def printListFromTailToHead(self,ListNode):
		# if ListNode is None:
			# return []
		# return self.printListFromTailToHead(ListNode.next)+[ListNode.val]

# s=Solution()
# a=ListNode('a')
# b=ListNode('b')
# c=ListNode('c')
# a.next=b
# b.next=c
# print (s.printListFromTailToHead(a))

#重建二叉树
# class TreeNode:
	# def __init__(self,x):
		# self.val=x
		# self.left=None
		# self.right=None
		
# class Solution:
	# def reConstructBinaryTree(self,pre,tin):
		# root=TreeNode(pre.pop(0))
		# index=tin.index(root.val)
		# if not pre or not tin:
			# root.left=reConstructBinaryTree(pre,tin[:index])
			# root.right=reConstructBinaryTree(pre,tin[index+1:])
		# return root
	
# s=Solution()
# print(s.reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]))


# import sys

# if __name__ == "__main__":
	# # 读取第一行的n
	# values=[]
	# c=[]
	# n = int(sys.stdin.readline().strip('\n'))
	# for i in range(n):
		# # 读取每一行
		# line = sys.stdin.readline().strip('\n').split(' ')
		# values.append(line)
	# print(values)
	# dst_time= int(sys.stdin.readline().strip('\n'))
	# class_time=sys.stdin.readline().strip('\n').split(' ')
	# b=list(map(lambda x: int(x[0])*60+int(x[1]),values))
	# print(b)
	# deadline=int(class_time[0])*60+int(class_time[1])-dst_time
	# c=[n for n in b if n<=deadline]
	# print(c)
	# print(str(max(c)//60)+' '+str(max(c)%60))
	
	
# import sys

# def get_gold(line):
	# if line[0]>=line[-1]:
		# x=line[0]
		# line.pop(0)
		# return x,line
	# else:
		# x=line[-1]
		# line.pop(-1)
		# return x,line

# T=int(input())
# HorseA=[]
# HorseB=[]
# for i in range(T):
	# a=0
	# b=0
	# n=int(input())
	# line= list(map(int,input().split(' ')))
	# #print(line)
	# # if len(line)!=n:
		# # return False
	# #total=sum(line)
	# t=len(line)
	# while t>0:
		# aa,line=get_gold(line)
		# a=a+aa
		# t-=1
		# if t==0:
			# break
		# else:
			# bb,line=get_gold(line)
			# b=b+bb
			# t-=1
	# if a<b:
		# a,b=b,a
	# HorseA.append(a)
	# HorseB.append(b)
# for i in range(T):
	# print('Case#%s'%(i+1)+':',HorseA[i],HorseB[i])
	#print "Case#%s: %s %s" %(i+1,HorseA[i],HorseB[i])
	
##最长递增子序列
# n=int(input())
# list_height=list(map(int,input().split(' ')))
# dp=[1]
# for i in range(1,n):
	# t_max=1
	# for j in range(i):
		# if list_height[j]>=list_height[i]:
			# t_max=max(t_max,dp[j]+1)
	# dp.append(t_max)
# N=max(dp)
# print(dp)
# print(N)

#最长公共子序列
# import numpy
# S1=list(x for x in input())
# S2=list(x for x in input())
# l_1=len(S1)
# l_2=len(S2)
# dp=numpy.zeros([l_1,l_2])
# for i in range(l_1):
	# dp[i,0]=0
# for i in range(l_2):
	# dp[0,i]=0
# for i in range(1,l_1):
	# for j in range(1,l_2):
		# if S1[i]==S2[j]:
			# dp[i,j]=dp[i-1,j-1]+1
		# else:
			# dp[i,j]=max(dp[i-1,j],dp[i,j-1])
# N=int(dp.max())
# print(N)

#搬寝室问题
# import numpy
# arr=list(map(int,input().split(' ')))
# n=arr[0]
# k=arr[1]
# list=list(map(int,input().split(' ')))
# list=sorted(list)
# dp=numpy.zeros([100,100])
# for i in range(1,n+1):
	# dp[0][i]=0
# for i in range(1,k+1):
	# for j in range(2*i,n+1):
		# if j > 2*i:
			# dp[i][j]=dp[i][j-1]
		# else:
			# dp[i][j]=float('inf')
		# if dp[i][j]>dp[i-1][j-2]+(list[j-1]-list[j-2])*(list[j-1]-list[j-2]):
			# dp[i][j]=dp[i-1][j-2]+(list[j-1]-list[j-2])*(list[j-1]-list[j-2])
# print(int(dp[k][n]))


# class Solution():

	# def FindMinimalNumber(self,list):
		# Len=len(list)
		# index1=0
		# index2=Len-1
		# if list[index1]<list[index2]:
			# return list[index1]
		# if list[index1]==list[index2] and list[index1]==list[(index1+index2)//2]:
			# MinNum=list[index1]
			# for i in range(1,Len):
				# if MinNum>list[i]:
					# MinNum=list[i]
			# return MinNum
		# while index2-index1!=1:
			# indexMid=(index1+index2)//2
			# if list[indexMid]>=list[index1]:
				# index1=indexMid
			# elif list[indexMid]<=list[index2]:
				# index2=indexMid
			# return list[index2]

# p=Solution()
# print(p.FindMinimalNumber([1,2,3,4,5]))
# print(p.FindMinimalNumber([2,3,4,5,1]))
# print(p.FindMinimalNumber([1,0,1,1,1]))

# class Solution:
	# def minNumberInRotateArray(self,rotateArray):
		# Len=len(rotateArray)
		# if Len==0:
			# return 0
		# index1=0
		# index2=Len-1
		# if rotateArray[index1]<rotateArray[index2]:
			# return rotateArray[index1]
		# if rotateArray[index1]==rotateArray[index2] and rotateArray[index1]==rotateArray[(index1+index2)//2]:
			# MinNum=rotateArray[index1]
			# for i in range(1,Len):
				# if MinNum>rotateArray[i]:
					# MinNum=rotateArray[i]
			# return MinNum
		# while rotateArray[index2]<=rotateArray[index1]:
			# if index2-index1==1:
				# indexMid=index2
				# break
			# indexMid=(index1+index2)//2
			# if rotateArray[indexMid]>=rotateArray[index1]:
				# index1=indexMid
			# elif rotateArray[indexMid]<=rotateArray[index2]:
				# index2=indexMid
		# return rotateArray[indexMid]
		
# class Solution:
	# def Fibonacci(self, n):
		# if n==0:
			# return 0
		# Num=[0,1]
		# Index1=0
		# Index2=1
		# for i in range(n-1):
			# Index=Index1+Index2
			# Num.append(Index)
			# Index1=Index2
			# Index2=Index
		# return Num[n-1]

# p=Solution()
# print(p.Fibonacci(0),p.Fibonacci(1),p.Fibonacci(2),p.Fibonacci(3),p.Fibonacci(4),p.Fibonacci(5))

# class Solution:
	# def jumpFloorII(self, number):
		# Num=[0,1]
		# index1=0
		# index2=1
		# for i in range(number-1):
			# index=sum(Num)+1
			# Num.append(index)
		# return Num[number]

# p=Solution()
# print(p.jumpFloorII(0),p.jumpFloorII(1),p.jumpFloorII(2),p.jumpFloorII(3),p.jumpFloorII(4))

# class Solution:
	# def NumberOf1(self, n):
		# count=0
		# while n:
			# if n & 1:
				# count+=1
				# n >>> 1
		# return count

# p=Solution()
# print(p.NumberOf1(-9))

# class Solution:
	# def Power(self, base, exponent):
		# result=1
		# if base==0 and exponent<=0:
			# return False
		# if exponent==0:
			# return 1
		# elif exponent>0:
			# while exponent>0:
				# result=result*base
				# exponent-=1
			# return result
		# else: 
			# exponent=abs(exponent)
			# while exponent>0:
				# result=result*base
				# exponent-=1
			# return 1/result

# p=Solution()
# print(p.Power(2,3))
# print(p.Power(2,0))
# print(p.Power(-2,3))
# print(p.Power(2,-3))
# print(p.Power(0,-3))

# class Solution:
	# def reOrderArray(self, array):
		# Front=0
		# Behind=len(array)-1
		# while Front<Behind:
			# while array[Front]& 0x1!=0:
				# Front+=1
			# while array[Behind]& 0x1==0:
				# Behind-=1
			# if Front<Behind:
				# array[Front],array[Behind]=array[Behind],array[Front]
				# Front+=1
				# Behind-=1
		# return array

# p=Solution()
# print(p.reOrderArray([1,2,3,4,5]))

# class Solution:
	# def reOrderArray(self, array):
		# EvenArray=[]
		# OddArray=[]
		# N=len(array)
		# for i in range(N):
			# if array[i]&0x1==0:
				# EvenArray.append(array[i])
			# if array[i]&0x1!=0:
				# OddArray.append(array[i])
		# OrderArray=OddArray+EvenArray
		# return OrderArray

# p=Solution()
# print(p.reOrderArray([1,2,3,4,5]))

# class ListNode:
	# def __init__(self,x):
		# self.val=x
		# self.next=None
	# def __str__(self):
		# return "ListNode(%r)" % self.val
# class Solution:
	# def FindKthToTail(self, head, k):
		# if head==None or k<=0:
			# return None
		# p1=head
		# p2=head
		# while k>1:
			# if p1.next!=None:
				# p1=p1.next
				# k-=1
			# else:
				# return None
		# while p1.next!=None:
			# p1=p1.next
			# p2=p2.next
		# return p2

# p=Solution()
# a=ListNode('a')
# b=ListNode('b')
# c=ListNode('c')
# d=ListNode('d')
# a.next=b
# b.next=c
# c.next=d
# print(p.FindKthToTail(a,1))


# class ListNode:
	# def __init__(self, x):
		# self.val = x
		# self.next = None

# class Solution:
	# def ReverseList(self, pHead):
		# pReverseHead=None
		# pNode=pHead
		# pPrev=None
		# while pNode!=None:
			# pNext=pNode.next
			# if pNext==None:
				# pReverseHead=pNode
			# pNode.next=pPrev
			# pPrev=pNode
			# pNode=pNext
		# return pReverseHead

# p=Solution()
# a=ListNode('a')
# b=ListNode('b')
# c=ListNode('c')
# d=ListNode('d')
# a.next=b
# b.next=c
# c.next=d
# print(p.ReverseList(a))


# class ListNode:
	# def __init__(self, x):
		# self.val = x
		# self.next = None

# class Solution:
	# def Merge(self,pHead1,pHead2):
		# if pHead1==None:
			# return pHead2
		# if pHead2==None:
			# return pHead1
		# pMergeHead=ListNode(None)
		# if pHead1.val<pHead2.val:
			# pMergeHead=pHead1
			# pMergeHead.next=self.Merge(pHead1.next,pHead2)
		# else:
			# pMergeHead=pHead2
			# pMergeHead.next=self.Merge(pHead1,pHead2.next)
		# return pMergeHead
# p=Solution()
# a=ListNode(1)
# b=ListNode(3)
# c=ListNode(5)
# d=ListNode(7)
# a.next=b
# b.next=c
# c.next=d
# a1=ListNode(2)
# b1=ListNode(4)
# c1=ListNode(6)
# d1=ListNode(8)
# a1.next=b1
# b1.next=c1
# c1.next=d1
# print(p.Merge(a,a1))

# class TreeNode:
	# def __init__(self, x):
		# self.val = x
		# self.left = None
		# self.right = None
# class Solution:
	# def DoseTree1HaveTree2(self,pRoot1,pRoot2):
		# if pRoot2==None:
			# return True
		# if pRoot1==None:
			# return False
		# if pRoot1.val!=pRoot2.val:
			# return False
		# return self.DoseTree1HaveTree2(pRoot1.left,pRoot2.left) and self.DoseTree1HaveTree2(pRoot1.right,pRoot2.right)

	# def HasSubtree(self, pRoot1, pRoot2):
		# result=False
		# if pRoot1!=None and pRoot2!=None:
			# if pRoot1.val==pRoot2.val:
				# result=self.DoseTree1HaveTree2(self,pRoot1,pRoot2)
			# if not result:
				# result=self.HasSubtree(pRoot1.left,pRoot2)
			# if not result:
				# result=self.HasSubtree(pRoot1.right,pRoot2)
		# return result
		
		
# class TreeNode:
	# def __init__(self, x):
		# self.val = x
		# self.left = None
		# self.right = None
	# def __str__(self):
		# return "TreeNode(%r)" % self.val
		
# class Solution:
	# def Mirror(self, root):
		# if not root:
			# return root
		# if not root.left and not root.right:
			# return root
		# pTemp=TreeNode(None)
		# pTemp=root.left
		# root.left=root.right
		# root.right=pTemp
		# if root.left:
			# self.Mirror(root.left)
		# if root.right:
			# self.Mirror(root.right)

# p=Solution()
# a=TreeNode(1)
# b=TreeNode(3)
# c=TreeNode(5)
# d=TreeNode(7)
# e=TreeNode(9)
# a.left=b
# a.right=c
# b.left=d
# b.right=e
# a1=TreeNode(10)
# p.Mirror(a)
# print(b.left)


# class Solution:
	# # matrix类型为二维列表，需要返回列表
	# def printMatrix(self, matrix):
		# row=len(matrix)
		# column=len(matrix[0])
		# list=[]
		# if row==0 or column==0:
			# return None
		# start=0
		# while column>start*2 and row>start*2:
			# self.PrintMatrixInCircle(matrix,column,row,start,list)
			# start+=1
		# return list

	# def PrintMatrixInCircle(self,matrix,column,row,start,list):
		# endX=column-1-start
		# endY=row-1-start
		# for i in range(start,endX+1):
			# number=matrix[start][i]
			# list.append(number)
		# if start<endY:
			# for i in range(start+1,endY+1):
				# number=matrix[i][endX]
				# list.append(number)
		# if start<endX and start<endY:
			# for i in range(endX-1,start-1,-1):
				# number=matrix[endY][i]
				# list.append(number)
		# if start<endX and start<endY-1:
			# for i in range(endY-1,start,-1):
				# number=matrix[i][start]
				# list.append(number)
				
# p=Solution()
# print(p.printMatrix([[1,2],[3,4],[5,6]]))

# class Solution:
	# def __init__(self):
		# self.stackA=[]
		# self.stackAssist=[]
	# def push(self, node):
		# self.stackA.append(node)
		# if not self.stackAssist:
			# self.stackAssist.append(node)
		# elif node<=self.stackA[-2]:
			# self.stackAssist.append(node)
		# else:
			# self.stackAssist.append(self.stackAssist[-1])
	# def pop(self):
		# self.stackA.pop()
		# self.stackAssist.pop()
	# def min(self):
		# return self.stackAssist[-1]
		
# class Solution:
	# def __init__(self):
		# self.stackAssist=[]
			# # def __str__(self):
		# # return "TreeNode(%r)" % self.val
	# def IsPopOrder(self, pushV, popV):
		# flag=False
		# while popV:
			# while not self.stackAssist or self.stackAssist[-1]!=popV[0]:
				# if not pushV:
					# break
				# self.stackAssist.append(pushV.pop(0))
			# if self.stackAssist[-1]!=popV[0]:
				# break
			# self.stackAssist.pop()
			# popV.pop(0)
		# if not popV and not self.stackAssist:
			# flag=True
		# return flag
		
# p=Solution()
# print(p.IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))

# class TreeNode:
	# def __init__(self, x):
		# self.val = x
		# self.left = None
		# self.right = None
	# def __str__(self):
		# return "TreeNode(%r)" % self.val

# class Solution:
	# def PrintFromTopToBottom(self, root):
		# if not root: 
			# return []
		# Queue=[]
		# Res=[]
		# Queue.append(root)
		# while Queue:
			# if root.left:
				# Queue.append(root.left)
			# if root.right:
				# Queue.append(root.right)
			# Res.append(Queue.pop(0).val)
			# if Queue:
				# root=Queue[0]
		# return Res
		
# p=Solution()
# a=TreeNode(1)
# b=TreeNode(3)
# c=TreeNode(5)
# d=TreeNode(7)
# e=TreeNode(9)
# a.left=b
# a.right=c
# b.left=d
# b.right=e
# print(p.PrintFromTopToBottom(a))

# class TreeNode:
	# def __init__(self, x):
		# self.val = x
		# self.left = None
		# self.right = None
	# def __str__(self):
		# return "TreeNode(%r)" % self.val

# class Solution:
	# def Print(self, pRoot):
		# if not pRoot: 
			# return []
		# nextLevel=0
		# tobePrint=1
		# Queue=[]
		# Res=[]
		# Final=[]
		# Queue.append(pRoot)
		# while Queue:
			# while tobePrint>0:
				# if pRoot.left:
					# Queue.append(pRoot.left)
					# nextLevel+=1
				# if pRoot.right:
					# Queue.append(pRoot.right)
					# nextLevel+=1
				# Res.append(Queue.pop(0).val)
				# tobePrint-=1
				# if Queue:
					# pRoot=Queue[0]
			# Final.append(Res)
			# Res=[]
			# tobePrint=nextLevel
			# nextLevel=0
		# return Final
		
# p=Solution()
# a=TreeNode(8)
# b=TreeNode(6)
# c=TreeNode(10)
# d=TreeNode(5)
# e=TreeNode(7)
# f=TreeNode(9)
# g=TreeNode(11)
# a.left=b
# a.right=c
# b.left=d
# b.right=e
# c.left=f
# c.right=g
# print(p.Print(a))

# class TreeNode:
	# def __init__(self, x):
		# self.val = x
		# self.left = None
		# self.right = None
	# def __str__(self):
		# return "TreeNode(%r)" % self.val
# class Solution:
	# def Print(self, pRoot):
		# if not pRoot: 
			# return []
		# stack=[[],[]]
		# Final=[]
		# Res=[]
		# current=0
		# next=1
		# stack[current].append(pRoot)
		# while stack[0] or stack[1]:
			# pNode=stack[current][-1]
			# Res.append(pNode.val)
			# stack[current].pop()
			# if current==0:
				# if pNode.left:
					# stack[next].append(pNode.left)
				# if pNode.right:
					# stack[next].append(pNode.right)
			# else:
				# if pNode.right:
					# stack[next].append(pNode.right)
				# if pNode.left:
					# stack[next].append(pNode.left)
			# if not stack[current]:
				# Final.append(Res)
				# Res=[]
				# current=1-current
				# next=1-next
		# return Final

# p=Solution()
# a=TreeNode(1)
# b=TreeNode(2)
# c=TreeNode(3)
# d=TreeNode(4)
# e=TreeNode(5)
# f=TreeNode(6)
# g=TreeNode(7)
# a.left=b
# a.right=c
# b.left=d
# b.right=e
# c.left=f
# c.right=g
# print(p.Print(a))

# class Solution:
	# def VerifySquenceOfBST(self, sequence):
		# if not sequence:
			# return False
		# root=sequence[-1]
		# i=0
		# while i<len(sequence)-1:
			# if sequence[i]>root:
				# break
			# else:
				# i+=1
		# j=i
		# while j<len(sequence)-1:
			# if sequence[j]<root:
				# return False
				# break
			# else:
				# j+=1
		# left=True
		# if i>0:
			# left=self.VerifySquenceOfBST(sequence[:i])
		# right=True
		# if i<len(sequence)-1:
			# right=self.VerifySquenceOfBST(sequence[i:len(sequence)-1])
		# return left and right

# p=Solution()
# print(p.VerifySquenceOfBST([5,7,6,9,11,10,8]))
#print(p.VerifySquenceOfBST([7,4,6,5]))

# class TreeNode:
	# def __init__(self, x):
		# self.val = x
		# self.left = None
		# self.right = None
	# def __str__(self):
		# return "TreeNode(%r)" % self.val
# class Solution:
	# # 返回二维列表，内部每个列表表示找到的路径
	# def FindPath(self, root, expectNumber):
		# if not root:
			# return []
		# path = []
		# currentSum = 0
		# Result=[]
		# def findapath(root, path, currentSum):
			# currentSum += root.val
			# path.append(root)
			# isLeaf = root.left == None and root.right==None
			# if currentSum==expectNumber and isLeaf:
				# onepath = []
				# for i in path:
					# onepath.append(i.val)
				# Result.append(onepath)
			# if root.left:
				# findapath(root.left, path, currentSum)
			# if root.right:
				# findapath(root.right, path, currentSum)
			# path.pop()
		# findapath(root,path,currentSum)
		# return Result
# p=Solution()
# a=TreeNode(10)
# b=TreeNode(5)
# c=TreeNode(12)
# d=TreeNode(4)
# e=TreeNode(7)
# a.left=b
# a.right=c
# b.left=d
# b.right=e
# print(p.FindPath(a,22))

# class RandomListNode:
	# def __init__(self, x):
		# self.label = x
		# self.next = None
		# self.random = None
# class Solution:
	##返回 RandomListNode
	# def CloneNodes(self,pHead):
		# pNode = pHead
		# while pNode:
			# pClone = RandomListNode(None)
			# pClone.label = pNode.label
			# pClone.next = pNode.next
			# pClone.random = None
			
			# pNode.next = pClone
			# pNode = pClone.next
	# def ConnectSiblingNodes(self,pHead):
		# pNode=pHead
		# while pNode:
			# pClone = pNode.next
			# if pNode.random:
				# pClone.random = pNode.random.next
			# pNode = pClone.next
	# def ReconnectNodes(self,pHead):
		# pNode = pHead
		# pCloneHead = None
		# pCloneNode = None
		# if pNode:
			# pCloneHead=pCloneNode = pNode.next
			# pNode.next = pCloneNode.next
			# pNode = pNode.next
		# while pNode:
			# pCloneNode.next = pNode.next
			# pCloneNode = pCloneNode.next
			# pNode.next = pCloneNode.next
			# pNode = pNode.next
		# return pCloneHead
	# def Clone(self, pHead):
		# self.CloneNodes(pHead)
		# self.ConnectSiblingNodes(pHead)
		# return self.ReconnectNodes(pHead)
		
# a=RandomListNode(1)
# b=RandomListNode(2)
# c=RandomListNode(3)
# a.next = b
# b.next = c
# a.random = c
# p = Solution()
# print(p.Clone(a))

# class TreeNode:
	# def __init__(self, x):
		# self.val = x
		# self.left = None
		# self.right = None
# class Solution:
	# def ConvertNode(self, pCurrent, pLastNodeInList):
		# if not pCurrent:
			# return pLastNodeInList
		# pLastNodeInList = self.ConvertNode(pCurrent.left, pLastNodeInList)
		# pCurrent.left = pLastNodeInList
		# if pLastNodeInList:
			# pLastNodeInList.right = pCurrent
		# pLastNodeInList = pCurrent
		# return self.ConvertNode(pCurrent.right, pLastNodeInList)
	# def Convert(self, pRootOfTree):
		# if not pRootOfTree:
			# return 
		# pLastNodeInList = None
		# self.ConvertNode(pRootOfTree,pLastNodeInList)#这里返回的是尾节点
		# while pRootOfTree.left:
			# pRootOfTree = pRootOfTree.left
		# return pRootOfTree

# class Solution:
	# def Permutation(self, ss):
		# if not ss:
			# return []
		# Begin = 0
		# ss = list(x for x in ss)
		# self.PermutationInter(Begin, ss)
	# def PermutationInter(self, Begin, ss):
		# if Begin == len(ss)-1:
			# print(ss)
		# else:
			# for i in range(len(ss)):
				# ss[Begin], ss[i] = ss[i], ss[Begin]
				# self.PermutationInter(Begin+1, ss)
				# ss[Begin], ss[i] = ss[i], ss[Begin]
				
				
				#ss = ''.join(ss)

# p = Solution()
# p.Permutation('abc')

# ss = 'abcd'
# ss = list(x for x in ss)
# cc = ''.join(ss)
# print(ss)
# print(type(cc))

# ss='abcd'
# Begin = 0
# print(len(ss))

# for i in range(len(ss)):
	# ss = list(x for x in ss)
	# ss[Begin], ss[i] = ss[i], ss[Begin]
	# ss = ''.join(ss)
	# print(type(ss))
	
