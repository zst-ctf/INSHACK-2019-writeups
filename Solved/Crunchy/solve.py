# https://www.quora.com/Whats-a-fast-algorithm-to-find-the-remainder-of-the-division-of-a-huge-Fibonacci-number-by-some-big-integer/answer/Michal-Forišek

def matrix_multiply(A,B,m):
    return [ [ ( A[r][0]*B[0][c] + A[r][1]*B[1][c] ) % m for c in range(2) ] for r in range(2) ]

def matrix_power(A,n,m):
    if n==0: return [ [1%m,0], [0,1%m] ] # identity modulo m
    B = matrix_power(A,n//2,m)
    C = matrix_multiply(B,B,m)
    if n%2==1: C = matrix_multiply(C,A,m)
    return C

def modular_fibonacci(n,m):
    A = matrix_power( [ [0,1], [1,6] ], n, m )
    return A[1][0]

g = 17665922529512695488143524113273224470194093921285273353477875204196603230641896039854934719468650093602325707751568
for n in range(10): print(f"crunchy({n})", modular_fibonacci( n, 100000007 ) )
print( "Your flag is: INSA{%d}" % modular_fibonacci( g, 100000007 ) )
