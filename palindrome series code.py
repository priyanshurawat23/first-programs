n=int(input('how many palindrome no.---->'))
for i in range(1,n+1):
    i1=i
    rev=0
    while i!=0:
        d=i%10
        rev=rev*10+d
        i=i//10
    if i1==rev:
        print(i1)
