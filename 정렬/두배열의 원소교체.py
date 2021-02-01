n,m = map(int,input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
array = sorted(b,reverse=True)

for i in range(m):
    if a[i] <= array[i]:
         a[i],array[i] = array[i],a[i]
    else: break     



print(sum(a))





