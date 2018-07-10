m=int(input())
sum=0
temp=m
while temp>0:
    dig=m%10
    sum+=dig**3
    temp=temp//10
if sum==m:
    print("is an armstrong number")
else:
    print("is not an armstrong number:")

