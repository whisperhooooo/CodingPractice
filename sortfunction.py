#sort函数使用
#对学生成绩进行排序
#输入数据组数N 接下来每一行的格式：姓名 年龄 成绩
#样例输入
#3
#abc 20 99
#bcd 19 97
#bed 20 97
#样例输出 #将学生按照成绩排序，成绩相同的则按姓名的字母进行排序。
#bcd 19 97
#bed 20 97
#abc 20 99


N=int(input())
L=[]
for i in range(N):
	l=list(input().split(' '))
	L.append(l)
SortedList=sorted(L,key=lambda x:(x[2],x[0],x[1]))
for i in range(len(SortedList)):
		print(SortedList[i][0]+' '+SortedList[i][1]+' '+SortedList[i][2])