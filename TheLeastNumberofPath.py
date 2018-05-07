#测试需要至少多少条道路联通整个城镇
#测试用例的第一行给出两个正整数，分别是城镇数目N和现有的道路M
#随后的M行对应M条道路，每行给出一个正整数，分别是该条道路直接连通的两个城镇的编号
#思路：该问题为在一个图上查找连通分量的个数。可以使用并查集完成；
#初始时，每个节点都是孤立的连通分量，当读入已经建成的边后，将边的两个顶点所在集合合并，表示这两个集合中的所有节点连通。
#对所有边重复该操作，最后计算所有的节点被保存在几个集合中便可得答案



import numpy
def FindRoot(x): #定义一个函数，找并查集的根
	if Tree[x] == -1:
		return x
	else:
		tmp = FindRoot(Tree[x])
		Tree[x] = tmp #除了根节点之外的节点都指向根节点，路径压缩
		return tmp
m,n = list(map(int,input().split(' ')))
Tree = numpy.zeros(m+1, int)
res = 0
for i in range(m+1):#为了符合实际将Tree[0]不存任何东西，从Tree[1]开始放置
	Tree[i] = -1 #起始时，每个节点都是根节点
for j in range(n):
	a,b = list(map(int,input().split(' ')))
	a = FindRoot(a)
	b = FindRoot(b)
	if a != b:
		Tree[a] = b
for k in range(m+1):
	if Tree[k] == -1:
		res += 1
print(res-2)#由于Tree[0]一定是等于-1的，所以要减去这一个无意义的点；此外每有两个根结点，便需要一条边来连接


#如果需要知道最大集合的数的数量，需要一个sum数组进行统计

import numpy
def FindRoot(x): #定义一个函数，找并查集的根
	if Tree[x] == -1:
		return x
	else:
		tmp = FindRoot(Tree[x])
		Tree[x] = tmp #除了根节点之外的节点都指向根节点，路径压缩
		return tmp
m,n = list(map(int,input().split(' ')))
Tree = numpy.zeros(m+1, int)
Sum = numpy.zeros(m+1, int)#用来统计每个集合中有多少个节点
res = 0
for i in range(m+1):#为了符合实际将Tree[0]不存任何东西，从Tree[1]开始放置
	Tree[i] = -1 #起始时，每个节点都是根节点
	Sum[i] = 1 #起始时，每个集合中至少有一个数
for j in range(n):
	a,b = list(map(int,input().split(' ')))
	a = FindRoot(a)
	b = FindRoot(b)
	if a != b:
		Tree[a] = b
		Sum[b] +=Sum[a] #b是a的更靠近根的节点，所以要将以a根所有的节点的数量加至b中
ans = 1
for k in range(m+1):
	if Tree[k] == -1:
		res += 1
		if Sum[k]>ans:
			ans = Sum[k]
print(res-2)#由于Tree[0]一定是等于-1的，所以要减去这一个无意义的点；此外每有两个根结点，便需要一条边来连接
print(ans)#输出最大的集合的数量
