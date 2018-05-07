#拓扑排序：若节点U经过若干条有向边后能够达到节点V，则在求得的序列中U必排在V之前
#如何对一个有向无环图进行拓扑排序
#首先，选择一个入度为0的节点，作为序列的第一个节点，当节点被选为序列的第一个顶点后，将改点从图中删除，同时删去相关边
#得到一个新图后，在新图后找到一个新的入度为0的节点，将其作为原图的第二个节点
#采用同样的方法，直到所有的边和节点都从原图中删去
#如果节点尚未被删去后就找不到入度为0的点，则说明剩下的节点形成了一个环路，则拓扑排序失败。

import numpy
n, m = list(map(int,input().split(' ')))
ans = numpy.zeros([n,n],int)
inDegree = numpy.zeros(n, int)
Q = [] #这个列表用来存储入度为0的节点
count = 0 
SmallNum = -100 #这个小数是为了更新已经删去的节点的度数，因为能被删去，所以其入度为0，这样在步骤a中，会被重复找到，造成死循环
for i in range(0, n):
	inDegree[i] = 0
for i in range(0, n):
	for j in range(0, n):
		ans[i][j] = -1
for i in range(m):
	a, b = list(map(int,input().split(' ')))
	inDegree [b] += 1 #因为是有向图，所有这里指的是a→b，b的入度增加1
	ans[a][b] = 1
for i in range(0, n):
	if inDegree[i] == 0:
		Q.append(i)
		inDegree[i] = SmallNum
while Q:
	nowP = Q[0] #找一个列表中入度为0的节点nowP
	Q.pop(0) 
	count += 1
	for i in range(0, n): #遍历这个节点可能指向的所有节点
		if ans[nowP][i] != -1:#如果被指向了，则因为将nowP删除了，所以其入度需要减1
			inDegree[i] += -1
		if inDegree[i] == 0: #步骤a
			Q.append(i) #由于nowP被删除了，所有节点的入度会更新，继续找入度为0的节点，重复上述循环
			inDegree[i] = SmallNum
if count == n: #所有节点都能被确定拓扑序列，则原图为有向无环图
	print('YES')
else:
	print('NO')