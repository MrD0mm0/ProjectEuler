i=1
j=2
sum=0
while j<4000000:
    if j%2==0:
        sum+=j
    k=i+j
    i=j
    j=k
print(sum)
