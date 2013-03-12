
def perm(s,n):
    if n == 1:
        return tag(s)
    else:
        return reduce(lambda x,y: x+y, [perm(s,n-1) for s in tag(s)])

def tag(s):
    return [s[0:i] + '-' + s[i:] for i in range(len(s)+1)]

ss=set(perm('ABC',4))
print('\n'.join(sorted(ss)))


