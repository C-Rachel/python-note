#!/usr/bin/python3

# 关键字def 用于引入一个函数定义，构成函数体的语句从下一行开始，并且必须缩进
def func(n):
	a,b = 0,1
	while a < n:
		print(a,end=' ')
		a,b = b,a+b
	print()
	
func(1000)