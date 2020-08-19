#coding:utf-8
import time
# print("添加dev分支")
# #1
# #2
# a=1
# b=2
# print(a+b)
# a=1
# while a < 7:
#     if(a % 2 == 0):
#         print(a,"is even")
#     else:
#         print(a,"is odd")
#     a += 1
# flag = False
# name = 'luren'
# if name == 'python':
#     flag = True
#     print('welcome boss')
# else:
#     print(name)
# num = 9
# if num >= 0 and num <= 10:  # 判断值是否在0~10之间
#     print
#     'hello'
# 输出结果: hello

# num = 10
# if num < 0 or num >= 10:  # 判断值是否在小于0或大于10
#     print(num)
# else:
#     print("no")
#
# num = 4
# if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
#     print(num)
# else:
#     print("错了")
# i = 1
# while i < 10:
#     i += 1
#     if i % 2 > 0:  # 非双数时跳过输出
#         continue
#     print(i)
# time.sleep(2)
# print("=============================")
# i = 1
# while 9:  # 循环条件为1必定成立
#     print(i)
#     i += 1
#     if i > 10:  # 当i大于10时跳出循环
#         print(i)
#         break
# a=time.time()
# print(a)
# for num in range(10,20):  # 迭代 10 到 20 之间的数字
#    for i in range(2,num): # 根据因子迭代
#       if num%i == 0:      # 确定第一个因子
#          j=num/i          # 计算第二个因子
#          print('%d 等于 %d * %d' % (num,i,j))
#          break            # 跳出当前循环
#    else:                  # 循环的 else 部分
#       print(num, '是一个质数')
# rows=int(input(": "))

# for i in range(0,rows):
#     for k in range(0, rows - i):
#         print(" * ",end="")
#         k += 1
#     i += 1
#     print("\n")
#
#












# for a in range(0,4):
#     for b in range(0,4-a):
#         print(1,end="")
#         b+=b
#     a+=a
#     print("\n")
#
for a in range(0,5):
    for b in range(0,a):
        print(" ",end="")
    for b in range(a,5):
        print(1,end="")
    print("\n")


#
# for i in range(10):
#     for j in range(0,i):
#         print("-",end=" ")
#
#     for j in range(i,10):
#         print("$", end=" ")
#
#     print("")
#
# print("-------------------------")
