i=3
j=5
sum=0
while i<1000:
    sum+=i
    i+=3
while j<1000:
    if j%3!=0:
        sum+=j
    j+=5
print(sum)
