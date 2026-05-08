# M01:
#  a=[1,2,3,4,5,6,7,2,4,8]
#  for i in a:
#      if i==2:
#         a.remove(2)
#  print(a)
#  M02:
# b=[23,45,65,78,89,24]
# largest=0
# seclar=0
# for x in b:
#     if x > largest:
#         seclar=largest
#         largest=x
# print(seclar)
# M03:
# a=[10,20,30,40,50,60]
# first=a[0]
# for i in a:
#     if i==10:
#         a.remove(10)
#         a.append(10)
# print(a)
# M04:
# a=[1,2,3,4,5]
# a.append(99)
# for i in range(5,2,-1):
#     a[i]=a[i-1]
# a[2]=99
# print(a)
# M05:
# a=[1,2,3,4,5,6]
# k=int(input("enter a number"))
# a.pop(k)
# print(a)
# MO6:
# a=("her baking is excellent")
# wo=a.split()
# longest= wo[0]
# for i in wo:
#     if len(i)>len(longest):
#         longest=i
# print("longest word is ",longest,"and its length is ",len(longest))
# MO7:
# a=("she has awesome skills")
# words=a.split()
# t="|".join(words)
# print(t)
# M08:
# a=[3,3,2,3,1,2,4,4]
# a.remove(3)
# a.remove(3)
# a.remove(2)
# a.remove(4)
# print(a)
# M09:
# a=[1,1,1,2,2,3,3,3]
# new=[]
# for i in a:
#     if i not in new:
#         count=0
#         for j in a:
#             if i == j :
#                 count+=1
#         new.append(i)
#         print(i,":",count)
# M10:
num=[12,56,78,34,98,678,0,23456]
for i in range(8):
    for j in range(7):
        if num[j] > num[1+j]:
            num[j],num[1+j]=num[1+j],num[j]
print(num)

