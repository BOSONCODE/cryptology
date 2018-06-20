#这是一个秘钥交换算法 目的就是求出秘钥K
#然后让K利用其它的加密算法对文本进行加密

import random

class User:
    __X = random.randint(1, 100)
    __K = None
    def __init__ (self, q, a):
        self.q = q
        self.a = a
        self.Y = self.cal()
        
    def quick_pow(self, a, b, p):
        ans = 1
        while b > 0:
            if b % 2 == 1:
                ans = ans * a % p
            a = a * a % p
            b >>= 1
        return ans

    def cal(self):
        return self.quick_pow(self.a, self.__X, self.q)

    def post(self):
        return self.q, self.a, self.cal()

    def calK(self, q, Yb):
        return self.quick_pow(Yb, self.__X, q)

    def getK(self, q, Yb):
        self.__K = self.calK(q, Yb)
        return self.__K

    def setX(self, val):
        self.__X = val
        self.Y = self.cal()

    def getY(self):
        return self.Y

#p is a prime number, a is a primitive root of p
#A (q, a, Ya)  B(q, a, Yb)
#Xa, Xb is private, q, a, ya, yb is public

def test():
    q = 97; a = 5;
    A = User(q, a)
    B = User(q, a)
    #A.setX(36)
    #B.setX(58)
    #print(B.getY(), A.getY())
    print(A.getK(q, B.getY()), B.getK(A.q, A.getY()))
    if A.getK(q, B.getY()) == B.getK(A.q, A.getY()):
        print('K = ', A.getK(q, B.getY()))
        print('加密成功')
    
if __name__ == '__main__':
    test()
