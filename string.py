#!/usr/bin/python3

str = 'Markypooh';

print(str); #输出字符串str
print(str[0:4]); #输出第一个到第四个字符
print(str[5:]); #输出第六个开始之后的所有字符
print(str[0:-4]); #输出第一个到倒数第五个的所有字符
print(str * 2); #输出字符串两次
print(str + 'biu'); #字符串拼接

num = int(input("请输入数字:"))

if (num == 10):
    print ("恭喜你，数字正确！")
else:
    print ("数字不正确！")

# 斐波纳契数列	
a, b = 0, 1
while b < 30:
    print(b)
    a, b = b, a+b
	
