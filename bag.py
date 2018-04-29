#背包问题
#有一个容量为V的背包，有一些物品（体积w，价值v），每种物品只有一个。要求用这些背包装下价值尽可能多的物品，求最大价值，背包可以不装满。

#dp[i][j]表示总体积不超过j的情况下，前i个物品所能达到的最大价值。
#依据每种物品是否被放入背包，每个状态有两个状态转移的来源。
#若物品被放入背包，设其体积为w，价值为v，则dp[i][j]=dp[i-1][j-w]+v
#若不加入背包，dp[i][j]=dp[i-1][j]
#选择上述较大值成为状态dp[i][j],即dp[i][j]=max{dp[i-1][j-w]+v,dp[i-1][j]}

#j-w>0

# list=[[1,2],[2,3]] #二维数组
# print(list[0][0],list[1])

#输入
# 70 3
# 71 100
# 69 1
# 1 2
# 输出
# 3

import numpy
list1=list(map(int,input().split(' ')))
s=list1[0]#背包总体积
n=list1[1]#物品总数量
arr=[]#存储每个物品的体积和其价值,第一个位置(index=[0])放体积，第二个位置放价值
for i in range(n):
	arr1=list(map(int,input().split(' ')))
	arr.append(arr1)
dp=numpy.zeros([101,1001])#生成状态二维数组
for i in range(s+1):
	dp[0][i]=0#初始化条件,不放任何东西的时候是没有价值的
for i in range(1,n+1,1):#遍历每一个物品
	for j in range(s,arr[i-1][0]-1,-1):#把物品i放进每一种可能的剩余体积为j的背包里，背包可能剩余体积最大为j，最小为物品i的体积
		dp[i][j]=max(dp[i-1][j],dp[i-1][j-arr[i-1][0]]+arr[i-1][1])#两种转移可能取较大值
	for j in range(arr[i-1][0]-1-1,-1,-1):#当剩余背包体积小于物品i的时候，状态是无法转移的，注意j>0，所以取到了-1，j的起始值应该取比物品i的体积小一点
		dp[i][j]=dp[i-1][j]#状态无法转移，因为背包不够放物品i了
print(int(dp[n][s]))

#注意arr这里的i是有实质意义的，就是第i个物品，所以i是不能等于0的，但是arr index=0的时候存储的是 第一个物品的信息.
#所以用arr调用第一个物品信息的时候记得要-1