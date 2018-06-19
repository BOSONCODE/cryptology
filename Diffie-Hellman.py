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

#p is a prime number, a is a primitive root of p
#A (q, a, Ya)  B(q, a, Yb)
#Xa, Xb is private, q, a, ya, yb is public
if __name__ == '__main__':
    q = 97; a = 5;
    Xa = random.randint(1, 100)
    Xb = random.randint(1, 100)
    #Xa = 36; Xb = 58;
    Ya = cal(q, a, Xa)
    Yb = cal(q, a, Xb)
    Ka = quick_pow(Yb, Xa, q)
    Kb = quick_pow(Ya, Xb, q)
    if Ka == Kb:
        print('K = ', Ka)
        print('加密成功')
