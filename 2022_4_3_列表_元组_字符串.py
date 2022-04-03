# This Python file uses the following encoding: utf-8

# print [1,2,3,4,5]
# list = [1,2,3,4,"AFAFA"]

# print list

# for i in list:
# 	print i




# list = [1,2,3,4,"AFAFA"]
# for i in range(len(list)):
# 	print list[i]

# print list [-1]
# print list[-2]



# list = [1,2,3,4,"AFAFA"]
# print list[0:3]
# print list[:3]
# print list[3:]
# print list[:]
# print list[0:5:2]
# print list[::-1]

# list2=[1,2,3,4]
# list2.append(5)
# print list2
# list2.extend([6,7,8])
# print list2
# list2[len(list2):]=[9,10,11]
# print list2

# s=[1,3,4,5]
# s.insert(1,2)
# print s
# s.insert(len(s),6)
# print s

# s.remove(6)#多相同元素存在，只会删除第一个
# print s
# s.pop(4)
# print s

# s[2:]=["3","4"]
# print s

# nums=[1,3,4,5,9,5,8,7]
# nums.sort()
# print nums
# nums.reverse()
# print nums
# print nums.count(5)
# print nums.index(3)

# # nums_copy=nums.copy()
# # print nums_copy

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print matrix

# for i in matrix:
# 	for each in i:
# 		print each

# a=[0]*3
# for i in range(3):
# 	a[i]=[0]*3
# print a

# import copy
# x=[[1,2,3],[4,5,6],[7,8,9]]
# #y=copy.copy(x)#浅拷贝
# y=copy.deepcopy(x)#深拷贝
# x[1][1]=0
# print x	
# print y


# #列表推导式
# a=[1,2,3,4,5]
# a=[i*2 for i in a]
# print a
# p=[i for i in range(10)]
# print p

# code =[ord(j) for j in "olofmeister"]
# print code 

# matrix=[[1,2,3]
# 	   ,[4,5,6]
# 	   ,[7,8,9]]

# col2 = [i[1] for i in matrix]
# print col2
# diag=[matrix[i][i] for i in range(len(matrix))]
# print diag
# diag=[matrix[i][-i-1] for i in range(len(matrix))]
# print diag


s=[[0]*3 for i in range(3)]
print s

even=[i for i in range(10) if i%2==0]
print even

matrix=[[1,2,3],[4,5,6],[7,8,9]]
flatten =[col for row in matrix for col in row]
print flatten
print([col for row in matrix for col in row])

ID=["Tom",18,"Female"]
a,b,c=ID#解包
print"the ID is %s %d %s\n"%(a,b,c)


x="12321"
print "shi hui wen shu" if x==x[::-1] else "bu shi hui wen shu"

# import string 
# sentence = "olofmeister is top o".translate(str.maketrans("lo","11"))
# print sentence

year=2015
print "olofmeister is {} of {}!".format("top1",year)
print "olofmeister is {1} of {0}!".format("top1",year)
print "olofmeister is {0} of {0}s!".format("top1",year)
print "olofmeister is {top} of {year}!".format(top="top1",year=2015)


#列表元组字符串统称序列

print "Fi"in"Fish"

arr1=[1,2,3,4,5]
arr1[1:4]=[]
print arr1

#==

arr2=[1,2,3,4,5]
del arr2[1:4]
print arr2

arr3=[1,2,3,4,5]
del arr3[::2]
print arr3

#P35


