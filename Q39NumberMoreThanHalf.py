#找出数组中唯一一个出现超过一半的数字
#由于仅有一个，用统计的方法
#从头遍历数组中的数字，相同时count+1，不同时-1，减至0时，换下一个数字
#注意需要判断这个数是否真的出现超过了一半（见测试例2）


class Solution:
	def MoreThanHalfNum_Solution(self, numbers):
		res = numbers[0]
		count = 0
		for i in range(0,len(numbers)):
			if numbers[i] == res:
				count += 1
			else:
				count -= 1
			if count == 0:
				res = numbers[i]
				count = 1
		if not self.CheckMoreThanHalf(numbers, res):
			return 0
		else:
			return res
	def CheckMoreThanHalf(self, numbers, mostnumber):
		count = 0
		for i in range(0, len(numbers)):
			if numbers[i] == mostnumber:
				count += 1
		if count*2 <= len(numbers):
			return False
		else:
			return True

p = Solution()
print(p.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))
print(p.MoreThanHalfNum_Solution([2,2,2,3,3,3]))