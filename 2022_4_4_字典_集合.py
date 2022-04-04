# This Python file uses the following encoding: utf-8


#-- list()  tuple()  str()      可迭代对象转换为对应序列
# print list("ABC")
# print tuple("ABC")
# print str("ABC")


# s=[1,6,3,4,5,2]
# print min(s)

# print"A","B"

# print sum([4,5,6])

# s_p=sorted(s)#不改变原来的序列
# print s
# print s_p

# print list(reversed(s))

# seasons=["spring","summer","fall","simter"]
# print enumerate(seasons)
# print list(enumerate(seasons))
# print list(enumerate(seasons,10))

# x=[1,2,3,4]
# y=[4,5,6]
# print zip(x,y)
 

# print map(ord,"ABC")

# print map(pow,[2,3,10],[5,2,3])

#字典
x={"A":"a","B":"b"}
print type(x)
print x["A"]
x["C"]="c"
print x["C"]
print x

y=dict.fromkeys("ABCD",250)
print y
y["C"]=200
print y
y.pop("A")
print y
y.update({'E':250,'F':250})
print y
y.update(G=250,H=250)
print y
y.setdefault('c',"code")
print y
print y.keys()#健
print y.values()#值
print y.items()#建值对
print len(y)

t={"关羽":{"统率":97,"武力":97,"智力":85}}
print t["关羽"]["统率"]


print set([1,1,2,3,4])



