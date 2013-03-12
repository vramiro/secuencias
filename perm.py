
def perm(s,n):
    if n == 0:        
        return [s]
    if n == 1:
        return tag(s)
    else:
        return reduce(lambda x,y: x+y, [perm(s,n-1) for s in tag(s)])

def tag(s):
    return [s[0:i] + '-' + s[i:] for i in range(len(s)+1)]

def test(s,n):
    aux = perm(s,n)
    ss=set(aux)
    print('\n'.join(sorted(ss)))
    print('++++++++++++++++++++++')

test('AB',0)
test('AB',1)
test('AB',2)
test('AB',3)

