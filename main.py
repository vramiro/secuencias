#!/usr/bin/python

mi = {'A':0, 'C':1, 'G': 2,'T':3, '-': 4}
idx = lambda l: map(lambda i: mi[i], list(l))

def perm(s):
    from itertools import permutations
    return set(filter(lambda e: s.replace('-','') == ''.join(map(str,e)).replace('-',''), permutations(s)))

def align(e, s):
    n1 = len(e); n2 = len(s)
    n = min(n1, n2); N = max(n1,n2)
    (x,y) = (e, s + '-'*(N-n)) if n1 >= n2 else (s, e + '-'*(N-n))
    f = lambda x,y: sum(map(lambda i,j: M[i][j], idx(x), idx(y)))
    if(d==True):
        print('\n'.join(map(lambda s: str(e) + '/' + str(s) + ' -> '+ str(f(e,s)), map(lambda t: ''.join(c for c in t), perm(y)))))
    return (e,s,max(map(lambda s: f(x,s), perm(y))))

def parsef(fname):
    M = [None, None, None, None, None]; suspects = {}; evidence = None
    lines = filter(lambda l: not(l.startswith('#')) , map(lambda s: s.strip(), open(fname).readlines()))
    for l in lines:
        (id, rest) = l.split(":")
        if(id in ['A', 'C', 'G', 'T', '-']):
            M[mi[id]] = map(lambda x: int(x), rest.split(',')) # falta el caso del *
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
for key, suspect in iter(sorted(suspects.iteritems())):
    aux = align(evidence, suspect)
    if(aux[2]>maxv):
        index = key
        adn = aux[1]
        maxv = aux[2]
    if(d==True):
        print(aux)
print("El culpable es el sospechoso numero %s (%s)" % (index, adn))

