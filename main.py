#!/usr/bin/python

mi = {'A': 0, 'C': 1, 'G': 2,'T': 3, '-': 4}
idx = lambda l: map(lambda i: mi[i], list(l))

def perm(s):
    from itertools import permutations
    return set(filter(lambda e: s.replace('-','') == ''.join(map(str,e)).replace('-',''), permutations(s)))


def perm(s,n):
    if n == 1:
        return tag(s)
    else:
        ll = []
        for s in tag(s):
            ll = ll + perm(s, n-1)
        return ll

def tag(s):
    l = []
    for i in range(len(s)+1):
        l.append(s[0:i] + '-' + s[i:])
    return l

def order(x,y):
    n1 = len(x); n2 = len(y)
    n = min(n1, n2); N = max(n1,n2)
    return (x, y + '-'*(N-n)) if n1 >= n2 else (y, x + '-'*(N-n))

def align(e, s):
    (x,y) = order(e,s)
    f = lambda x,y: sum(map(lambda i,j: int(M[i][j]), idx(x), idx(y)))
    if(d==True):
        dfmt = lambda s: str(e) + '/' + str(s) + ' -> '+ str(f(e,s))
        tuptosrt = lambda t: ''.join(c for c in t)
        print('\n'.join(map(dfmt, map(tuptosrt, perm(y)))))
    return (e,s,max(map(lambda s: f(x,s), perm(y))))

def parsef(fname):
    M = [None, None, None, None, None]; suspects = {}; evidence = None
    for l in open(fname).readlines():
        l = l.strip()
        if(l.startswith('#')):
            continue
        (id, rest) = l.split(":")
        if(id in ['A', 'C', 'G', 'T', '-']):
            M[mi[id]] = map(lambda x: x, rest.split(','))   
        elif(id == '0'):
            evidence = rest
        else:
            suspects[id] = rest 
    return (M, evidence, suspects)

# main
import sys
(M, evidence, suspects) = parsef(sys.argv[1])
d = False if len(sys.argv) < 3 else True
maxv = -float('Inf'); index = 0; adn = None
for key, suspect in sorted(suspects.iteritems()):
    aux = align(evidence, suspect)
    if(aux[2]>maxv):
        index = key
        adn = aux[1]
        maxv = aux[2]
    if(d==True):
        print(aux)
print("El culpable es el sospechoso numero %s (%s)" % (index, adn))
