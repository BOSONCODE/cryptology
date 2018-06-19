#这是一个秘钥交换算法 目的就是求出秘钥K
#然后让K利用其它的加密算法对文本进行加密

import random
def quick_pow(a, b, p):
    ans = 1
    while b > 0:
        if b % 2 == 1:
            ans = ans * a % p
        a = a * a % p
        b >>= 1
    return ans

def cal(q, a, X):
    return quick_pow(a, X, q)

def A(q, a, Xa):
    return q, a, cal(q, a, Xa)

def B(q, a, Xb):
    return q, a, cal(q, a, Xb)

def getKa(q, Yb, Xa):
    return quick_pow(Yb, Xa, q)

def getKb(q, Ya, Xb):
    return quick_pow(Ya, Xb, q)

#p is a prime number, a is a primitive root of p
#A (q, a, Ya)  B(q, a, Yb)
#Xa, Xb is private, q, a, ya, yb is public
if __name__ == '__main__':
    q = 97; a = 5;
    '''
    Xa = random.randint(1, 100)
    Xb = random.randint(1, 100)
    '''
    Xa = 36; Xb = 58;
    q1, a1, Ya = A(q, a, Xa)
    q2, a2, Yb = B(q1, a1, Xb)
    Ka = getKa(q, Yb, Xa)
    Kb = getKb(q, Ya, Xb)
    if Ka == Kb:
        print('K = ', Ka)
        print('加密成功')
