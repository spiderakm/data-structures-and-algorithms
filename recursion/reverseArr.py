def fun(a,l,r):
    if l >= r:
        return
    a[l], a[r] = a[r], a[l]
    fun(a,l+1,r-1)


a = [1,2,3,4,5]
n = len(a)
fun(a,0,n-1)
print(a)