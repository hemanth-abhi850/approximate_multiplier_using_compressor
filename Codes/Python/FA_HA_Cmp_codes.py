def HA(X, Y):

    bit_sum = np.array([[0,1], [1,0]])
    bit_carry = np.array([[0,0], [0,1]])

    return bit_carry[X][Y], bit_sum[X][Y]

def TER_CONC4(a,b,c,d):
    Y=str(a)+str(b)+str(c)+str(d)
    V=decimal(Y)
    return V

def FA(x,y,z):
    c1,s1 = HA(x,y)
    c2,s2 = HA(s1,z)
    carry = c1 + c2
    return carry,s2



def  andg(a,b):
     z = a * b
     return z


def cmp(a,b,c,d): # approximate compressor
    S=[0,1,1,0, 1,0,0,1, 1,0,0,1, 0,1,1,1];

    C=[0,0,0,1, 0,1,1,1, 0,1,1,1, 1,1,1,1];

    V=TER_CONC4(a,b,c,d)

    SUM = S[V]
    CARRY= C[V]

    return [CARRY,SUM]

def Comp(p,q,r,s,t): # exact compressor
    c1,s1 = FA(p,q,r)
    carry,sum = FA(s1,s,t)
    return c1,carry,sum
