#在一个无向连通图中，如果存在一个连通子图包含原图中的所有的节点和部分边，且这个子图不存在回路，那么我们称这个子图为
#原图的一颗生成树，在带权图中，所有的生成树中边权的和最小的那颗称为最小生成树
#Kruskal算法
#初始所有节点都为孤立节点
#按照边权递增顺序遍历所有的边，若遍历到的边两个顶点仍分属于不同的集合（该边结尾连通这两个集合的边中权值最小的那条）
#则确定该边为最小生成树中的一条边，并将这两个顶点分属的集合合并
#遍历完所有的边之后，原图上所有节点属于同一集合则被选取的边和原图中所有节点构成最小生成树；否则原图不连通，最小生成树不存在


import numpy
def FindRoot(x): #定义一个函数，找并查集的根
	if Tree[x] == -1:
		return x
	else:
		tmp = FindRoot(Tree[x])
		Tree[x] = tmp #除了根节点之外的节点都指向根节点，路径压缩
		return tmp
n = int(input())
m = int(n*(n-1)/2)
Tree = numpy.zeros(n+1, int)
original_list = []
path_length = 0
for i in range(m):
	input_list = list(map(int,input().split(' ')))
	original_list.append(input_list)
sorted_list = sorted(original_list, key = lambda x: x[2]) #列表中的第三个数字是路径长度的权重，以此为排列顺序增序
for i in range(n+1):#为了符合实际将Tree[0]不存任何东西，从Tree[1]开始放置
	Tree[i] = -1 #起始时，每个节点都是根节点
for j in range(m):
	a,b = sorted_list[j][0],sorted_list[j][1]
	a = FindRoot(a)
	b = FindRoot(b)
	if a != b:
		Tree[a] = b
		path_length += sorted_list[j][2]
print(path_length)