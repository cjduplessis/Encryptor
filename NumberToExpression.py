from math import trunc, log

def droot(n, r):
    return trunc(n**(1/r))

def dlog(n, b):
    return trunc(log(n)/log(b))

def transform_to_expr1(n, base):
    m = n
    S = ''
    my_bool = False
    while m >= base:
        d_exp = dlog(m, base)
        R1 = m // (base**d_exp)
        m = m % (base**d_exp)

        if R1 > 1:
            if d_exp > 1:
                S += str(R1)+'*'+str(base)+'^'+str(d_exp)
            else:
                S += str(R1)+'*'+str(base)
        elif d_exp > 1:
            S += str(base)+'^'+str(d_exp)
        else:
            my_bool = True

        if m > 1:
            S += ' + '
            
        if m < base:
            if my_bool:
                S += str(base + m)
            elif m > 0:
                S += str(m)

    return S

def transform_to_expr2(n, rad):
    m = n
    S = ''
    while m > 1:
        d_rt = droot(m, rad)
        R1 = m // (d_rt**rad)
        m = m % (d_rt**rad)
        
        if d_rt > 1:
            if R1 > 1:
                S += str(R1)+'*'+str(d_rt)+'^'+str(rad)
            else:
                S += str(d_rt)+'^'+str(rad)
        else:
            S += str(R1)

        if m > 1:
            S += ' + '
        elif m == 1:
            S += ' + 1'
        
    return S

print(transform_to_expr1(28, 3))
#print(transform_to_expr1(72703597494219643, 2))
