n1=int(input())
n2=int(input())
for num in range(n1,n2+1):
    sum=0
    temp=num
    while temp>0:
        dig=temp%10
        sum+=dig**3
        temp=temp//10
        if num==sum:
            print(num)
  
    

  
