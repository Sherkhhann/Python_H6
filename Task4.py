num=input().split()
n=len(num)
i=1
while i<n:
 if int(num[i])>int(num[i-1]):
  print(num[i], end=" ")
 i+=1