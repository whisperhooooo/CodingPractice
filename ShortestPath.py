#最短路径问题：寻找图中某两个特定节点间的最短路径长度
#输入：第一行N表示几个节点；M表示M行
#每一行包含三个数字：a，b：两个节点；c：两个节点之间的距离

import numpy
n, m = list(map(int,input().split(' ')))
ans = numpy.zeros([n+1,n+1],int)
for i in range(1, n+1):
	for j in range(1, n+1):
		ans[i][j] = -1 #初始化节点的距离，先假设各节点都是孤立的，即距离为无穷
	ans[i][i] = 0 #自己和自己的距离为0
for i in range(m):
	a, b, c = list(map(int,input().split(' ')))
	ans[a][b] = ans[b][a] = c #无向图，要进行两次赋值
for k in range(1,n+1): #k从1到N循环，依次代表允许经过的中间节点编号小于等于k
	for i in range(1,n+1):
		for j in range(1,n+1):#遍历所有ans[i][j]的值，判断其值保持原值还是要更新
			if ans[i][k] == -1 or ans[k][j] == -1:#若两值中有一个为无穷，则ans[i][j]不能经过节点k而被更新，跳出循环，保持原值
				continue
			elif ans[i][j] == -1 or ans[i][j]>ans[i][k]+ans[k][j]:#可以通过k打破不能连接的问题，或者获得更短路径则更新
				ans[i][j] = ans[i][k]+ans[k][j]
print(ans[1][n]) #起始节点标号为1，终止节点标号为n

#上述方法解决的是 全源最短路 问题：Floyd算法

#Dijkstra算法解决特定节点到其他所有节点的最短路径长度：单源最短路路径问题，这里计算由1到n的最短路径
#思路：按照最短路径长度递增的顺序确定每一个节点的最短路径长度，即先确定的节点的最短路径长度不大于后确定的节点的最短路径长度
#1、初始化，集合K（保存已经确定最短路径长度最短的节点）中加入节点1，节点1到节点1的最短长度为0，到其他的为无穷。
#2、遍历与集合K中节点直接相邻的边（U，V，C），U属于集合K，V不属于集合K，计算由节点1出发按照已经得到的最短路径达到U，
#再由U经过该边达到V时的路径长度。
#比较所有与集合K中节点直接相邻的非集合K节点的路径长度，其中路径长度最小的节点被确定为下一个最短路径确定的节点，其最短
#路径长度最小的节点被确定为下一个最短路径确定的节点，其最短路径长度即为这个路径长度，最后将该节点加入集合K
#3、直到集合K中已经包含了所有的点，算法结束。

import numpy
n, m = list(map(int,input().split(' ')))
ans = numpy.zeros([n+1,n+1],int) #邻接矩阵用来保存两节点和其之间的距离
Dis = numpy.zeros(n+1,int) #距离向量，当mark[i]为true时，表示已得的最短路径长度；否则，表示所有从节点1出发，经过已知的最短路径达到集合K中的某节点，在经过一条边达到节点i的路径最短距离
mark = numpy.zeros(n+1,int)#标记，mark[i]为true时，表示节点i的最短路径已经得到，该节点已经加入集合K
for i in range(1, n+1):#邻接矩阵初始化
	for j in range(1, n+1):
		ans[i][j] = -1
	ans[i][i] = 0
for i in range(m):
	a, b, c = list(map(int,input().split(' ')))
	ans[a][b] = ans[b][a] = c
for i in range(1,n+1):
	Dis[i] = -1 #初始化所有距离-1，即不可达
	mark[i] = False #所有节点不属于集合K
Dis[1] = 0
mark[1] = True #得到最近的点为节点1，距离为0；将节点1加入集合K中，
newP = 1#表示新加入的点，节点1
for i in range(1, n): #循环n-1次，按照最短路径递增的顺序确定其他n-1个点的最短路径长度
	for j in range(1,n+1):
		if ans[newP][j] != -1:#遍历与新加入的节点相邻的节点
			adjP = j #新加入节点的相邻节点
			tmp_dis = ans[newP][adjP]#两个节点之间的距离
			if mark[adjP]:#如果相邻节点已经在K中了，那么其最短路径是不用更新的，因为已经确定了
				continue
			elif Dis[adjP] == -1 or Dis[adjP]>Dis[newP]+tmp_dis:#若原本相邻节点是不可达的，由于新节点的加入可达了；或者由于新节点的加入其可达距离变短了，则更新
				Dis[adjP] = Dis[newP]+tmp_dis
	min = 100000 #初始化一个值，为下面找最短距离的可达节点做准备
	for k in range(1, n+1):
		if mark[j] == True or Dis[j] == -1: #如果节点本来就在K中或者仍不可达，则不考虑
			continue
		if Dis[j] < min:#找到经过节点1，并通过集合K中的某一点达到的最短距离节点
			min = Dis[j]
			newP = j
	mark[newP] = True#将其加入集合K中；Dis[newP]的值虽然不变，但是意义发生变化；
						#所有经过集合K中的节点在经过一条边达到时的距离中的最小值变为从节点1到节点newP的最短距离
print(Dis[n])

