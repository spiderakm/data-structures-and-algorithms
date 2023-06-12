def fun(a,l,r):
    if l >= r:
        return
    a[l], a[r] = a[r], a[l]
    fun(a,l+1,r-1)


a = [1,2,3,4,5]
n = len(a)
fun(a,0,n-1)
print(a)

def fun(a, n, i=0):
    if i >= n/2:
        return
    a[i], a[n-i-1] = a[n-i-1], a[i]
    fun(a, n, i+1)

a = [1, 2, 3, 4, 5]
n = len(a)
fun(a, n)
print(a)
