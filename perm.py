
def perm(s,n):
    if n == 1:
        return tag(s)
    else:
        ll = []
        for s in tag(s):
            ll.append(perm(s, n-1))
        return ll

def tag(s):
    l = []
    for i in range(len(s)+1):
        l.append(s[0:i] + '-' + s[i:])
    return l


l=perm('AB',2)
for i in l:
    print(i)
    print('\n')

