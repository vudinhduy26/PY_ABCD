import re
class add(int):
	def __call__(self, n):
		return add(self + n)

if __name__ == '__main__':
	print(add(1)(2))
	# print(result)
