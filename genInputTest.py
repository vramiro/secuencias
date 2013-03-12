from random import randint

alpha = 'ACGT'
header = '''# Matriz
A:5,-1,-2,-1,-3
C:-1,5,-3,-2,-4
G:-2,-3,5,-2,-2
T:-1,-2,-2,5,-1
-:-3,-4,-2,-1,*
     # Evidencia
'''
def adn(n):
    return reduce(lambda x,y: x+y, [alpha[randint(0,3)] for i in range(0,n)])

print(header)
print('0:'+adn(randint(80,100)))
print('          # ADN Sospechosos')
for i in range(1,50):
    print(str(i) + ':' + adn(randint(50,100)))

for i in range(51,100):
    print(str(i) + ':' + adn(randint(50,100)))
