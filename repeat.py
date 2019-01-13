def repeat(x):
  size=len(x)
  repeated=[]
  for i in range(size):
    k=i+1
    for j in range(k,size):
        if x[i]==x[j] and x[i] not in repeated:
            repeated.append(x[i])
    return repeated
list1=[5,10,20,20,30,40,40,5]
print(repeat(list1))
