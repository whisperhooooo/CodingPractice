#用两个栈实现队列，即用两个“先进后出”实现“先进先出”
#考虑用栈A实现入栈，栈B实现出栈。那么如果栈B为空，栈A不为空，则需要把栈A的元素全部压至栈B，然后删除栈B的最上元素。
#如果栈B不为空，则可以直接将栈B最上的元素删除。
#用数组实现栈的功能

class Solution:

	def __init__(self):
		self.stackA=[]
		self.stackB=[]

	def push(self,node):
		self.stackA.append(node)

	def pop(self):
		if self.stackB:
			return self.stackB.pop()
		elif not self.stackA:
			return None
		else:
			while self.stackA:
				self.stackB.append(self.stackA.pop())
			return self.stackB.pop()

p=Solution()
p.push(1)
p.push(2)
p.push(3)
print(p.pop())
print(p.pop())
print(p.pop())

#self.

#用两个队列实现栈
#保持一个队列始终为空
#当两个队列都是空的时候，优先将元素放入队列A中；不然那个队列有元素就放在哪里
#当需要删除元素的时候，先将有元素队列的元素放到空队列中，然后删除最后一个元素

class Solution():
	def __init__(self):
		self.queueA=[]
		self.queueB=[]
	def push(self,node):
		if not self.queueA and not self.queueB:
			return self.queueA.append(node)
		elif self.queueA:
			return self.queueA.append(node)
		elif self.queueB:
			return self.queueB.append(node)
	def pop(self):
		if not self.queueA and not self.queueB:
			return None
		elif self.queueA:
			while len(self.queueA)!=1:
				self.queueB.append(self.queueA.pop(0))
			return self.queueA.pop(0)
		elif self.queueB:
			while len(self.queueB)!=1:
				self.queueA.append(self.queueB.pop(0))
			return self.queueB.pop(0)

p=Solution()
p.push(1)
p.push(2)
p.push(3)
print(p.pop())
p.push(4)
print(p.pop())
print(p.pop())
print(p.pop())