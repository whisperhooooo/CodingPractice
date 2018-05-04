#排序问题
#快排
import random
def Partition(list,start,end):#实现一个功能，将小于某一个数字A的数都放在其左边，大于该数字的数放右边
	index=random.randint(start,end)#start<=index<=end
	list[index],list[end]=list[end],list[index]
	small=start-1
	for index in range(start,end):
		if list[index]<list[end]:#只有index指的那个数字比较小才移位small并且换位，若大于直接将index指标后移就可以
			small+=1
			if small!=index:
				list[index],list[small]=list[small],list[index]
	small+=1 #small指标前和包含这个指标的数字都是小于A的
	list[small],list[end]=list[end],list[small]
	return small

def QuickSort(list,start,end):
	if start==end:
		return
	index=Partition(list,start,end)
	if index>start:
		QuickSort(list,start,index-1)#将数字A左边的数字继续使用快排
	if index<end:
		QuickSort(list,index+1,end)#将数字A右边的数字使用快排
	return list


list=[8,7,6,5,4,2,1,3]
Len=len(list)
print(QuickSort(list,0,Len-1))


#用统计的方法做排序
#要给一家公司的人员做年龄的排序，可以先统计每个年龄出现的人的个位数，然后据此排序。
AgeList=[18,19,20,67,21,18,20,99]
import numpy
def Sort(list):
	OldestAge=100#最大年纪不能超过100岁
	L=len(list)
	TimeofAge=numpy.zeros(OldestAge,dtype=int)
	for i in range(L):
		age=AgeList[i]
		TimeofAge[age]+=1#统计每个年纪的次数
	index=0
	for i in range(OldestAge):#遍历每个年纪
		for j in range(TimeofAge[i]):#看每个年纪统计的次数，循环
			list[index]=i
			index+=1
	return list
print(Sort(AgeList))


#冒泡排序
def BubbleSort(arr):
	flag = True
	while flag:
		for i in range(1,len(arr)):
			flag = False
			for j in range(len(arr)-i):
				if arr[j] > arr[j+1]: #内部循环 两两交换
					arr[j],arr[j+1] = arr[j+1],arr[j]
					flag = True
	return arr


#选择排序
#思路：找最小的元素，放在列表的头，然后在剩余的列表里再找最小的放在已排好序的列表的后面
def SelectionSort(arr):
	for i in range(len(arr)):
		MinIndex = i
		for j in range(i+1,len(arr)):
			if arr[MinIndex]>arr[j]:
				MinIndex = j
		if i != MinIndex:
			arr[MinIndex],arr[i] = arr[i],arr[MinIndex]
	return arr
print(SelectionSort([2,3,4,1,5]))


#插入排序
#思路：前方是有序序列，依次将无序序列的每一个元素放到合适的位置
def InsertSort(arr):
	for i in range(len(arr)):
		preIndex = i-1
		current = arr[i] #现在需要插入的数字记录下来，然后就可以为前面的数字挪位子做准备
		while preIndex >=0 and arr[preIndex]>current: #如果数字大就往后挪动
			arr[preIndex+1] = arr[preIndex]
			preIndex-=1
		arr[preIndex+1] = current
	return arr
print(InsertSort([2,3,4,1,5]))


#希尔排序
#思路：希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
#待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
#一开始是每隔一半的间隔，即一次只比较两个数，后来间隔缩小，就变成了四个，八个，等等，直到gap为1
import math
def ShellSort(arr):
	gap = int(len(arr)/2)
	while gap>0:
		for i in range(gap, len(arr)):
			current = arr[i]
			j = i-gap
			while j>=0 and arr[j]>current:
				arr[j+gap] = arr[j]
				j-=gap
			arr[j+gap] = current
		gap = int(math.floor(gap/2))
	return arr
print(ShellSort([2,3,4,1,5,2,3,4,5,7,11,8,9,12]))


#归并排序
#1、申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
#2、设定两个指针，最初位置分别为两个已经排序序列的起始位置；
#3、比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
#4、重复步骤 3 直到某一指针达到序列尾；
#5、将另一序列剩下的所有元素直接复制到合并序列尾
import math
def MergeSort(arr):
	middle = int(math.floor(len(arr)/2))
	if middle <= 0:
		return arr
	left, right = arr[:middle], arr[middle:]
	return merge(MergeSort(left),MergeSort(right))
def merge(left, right):
	result = []
	while left and right:
		if left[0]<=right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	while left:
		result.append(left.pop(0))
	while right:
		result.append(right.pop(0))
	return result
print(MergeSort([2,3,4,1,5]))
#比如题中的要求，得先排[2,3]和[4,1,5],而[4,1,5]又需要分成[4]和[1,5],[1,5]排序得到[1,5],在和[4]得到[1,4,5]
#[2,3]排序得到[2,3]，在和[1,4,5]排序得到最后结果