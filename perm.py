
def perm(s,n):
    if n == 1:
        return tag(s)
    else:
        ll = []
        for s in tag(s):
            ll = ll + perm(s, n-1)
        return ll

def tag(s):
    # l = []
    # for i in range(len(s)+1):
    #     l.append(s[0:i] + '-' + s[i:])
    # return l
    return [s[0:i] + '-' + s[i:] for i in range(len(s)+1)]

ss=set(perm('ABC',4))
print('\n'.join(sorted(ss)))


