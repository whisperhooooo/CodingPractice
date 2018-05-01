#输出字符串的所有排列：'abc'输出'abc','acb','bac','bca','cab','cba'


# class Solution:
	# def Permutation(self, ss):
		# if not ss:
			# return []
		# Begin = 0
		# n = 0
		# ss = list(x for x in ss)
		# self.PermutationInter(Begin, ss, n)
	# def PermutationInter(self, Begin, ss, n):
		# if Begin == len(ss)-1:
			# print(ss)
		# else:
			# for i in range(n, len(ss)):
				# ss[Begin], ss[i] = ss[i], ss[Begin]
				# self.PermutationInter(Begin+1, ss, n+1)
				# ss[Begin], ss[i] = ss[i], ss[Begin]

# p = Solution()
# p.Permutation('abc')

#递归的思路 将字符串看成两个部分 1、首字符+2、后面所有的字符；第一部分和第二部分不断交换，即可得到后续所有情况，不交换也算一种情况即下面i=Begin的时候
#首先看第一个字符abc(bac(bca),cba(cab))
#第二个字符(acb) 

class Solution:
	def Permutation(self, ss):
		if not ss:
			return []
		Begin = 0 #指示该以第几个字符为首字符
		ss = list(x for x in ss)
		res = []
		self.PermutationInter(Begin, ss, res)
		return sorted(res)
	def PermutationInter(self, Begin, ss, res):
		if Begin == len(ss)-1:
			tt = ss[:] #由于递归调用这里需要copy一下，否则输出为None
			tt = str(''.join(tt))
			res.append(tt)
		else:
			for i in range(Begin, len(ss)):
				if i!=Begin and ss[Begin]==ss[i]:#对于字符相同的不交换，以免重复计算
					continue
				ss[Begin], ss[i] = ss[i], ss[Begin]
				self.PermutationInter(Begin+1, ss, res)#起始字符串位置后移一位
				ss[Begin], ss[i] = ss[i], ss[Begin]

p = Solution()
print(p.Permutation('abc'))