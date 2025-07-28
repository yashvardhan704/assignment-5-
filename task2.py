list=[]
for i in range(1,11):
    list.append(i)
print(f"orignal list is : {list}")
print(f"the first 5 element of list are: {list[0:5:1]}")
rev=list[0:5:1]
rev.reverse()
print(f"the reverse of list is: {rev}")

