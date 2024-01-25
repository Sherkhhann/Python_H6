num=input().split()
n=len(num)
i=0
while i<n-1:
 a=num[i]
 b=num[i+1]
 if int(a)>0 and int(b)>0 or int(a)<0 and int(b)<0:
  print(a, b)
  break
 i+=1