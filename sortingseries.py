#排序问题
#快排
# import random
# def Partition(list,start,end):#实现一个功能，将小于某一个数字A的数都放在其左边，大于该数字的数放右边的数都放在其左边，大于该数字的数放右边
	# index=random.randint(start,end)#start<=index<=end
	# list[index],list[end]=list[end],list[index]
	# small=start-1
	# for index in range(start,end):
		# if list[index]<list[end]:
			# small+=1
			# if small!=index:
				# list[index],list[small]=list[small],list[index]
	# small+=1
	# list[small],list[end]=list[end],list[small]
	# return small

# def QuickSort(list,start,end):
	# if start==end:
		# return
	# index=Partition(list,start,end)
	# if index>start:
		# QuickSort(list,start,index-1)#将数字A左边的数字继续使用快排
	# if index<end:
		# QuickSort(list,index+1,end)#将数字A右边的数字使用快排
	# return list


# list=[8,7,6,5,4,2,1,3]
# Len=len(list)
# print(QuickSort(list,0,Len-1))


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

