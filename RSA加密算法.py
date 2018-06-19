def quick_pow(a, b, p):
    ans = 1
    while b > 0:
        if b % 2 == 1:
            ans = ans * a % p
        a = a * a % p
        b >>= 1
    return ans

def getPhi(n):
    ans = n
    i = 2
    while True:
        if i*i > n:
            break
        if n % i == 0:
            ans = ans//i*(i-1)
            while n % i == 0:
                n //= i
        i = i + 1
    if n > 1:
        ans = ans//n*(n-1)
    return ans

def isprime(a, b):
    for i in range(2, a):
        if a % i == 0:
            return False, False
    for i in range(2, b):
        if b % i == 0:
            return False, False
    return True, True

def getSecretKey(p, q, e):
    isprimep, isprimeq = isprime(p, q)
    if isprimep == False or isprimeq == False:
        raise Exception("p或者q有一个不是素数")
    n = p*q
    phin = (p - 1)*(q - 1)
    phim = getPhi(phin)
    d = quick_pow(e, phim - 1, phin)
    return d, n

def encrypt(p, e, n):
    return quick_pow(p, e, n)

def decrypt(c, d, n):
    return quick_pow(c, d, n)


if __name__ == '__main__':
    p = 7; q = 17; e = 5; P = 6;
    C = encrypt(P, e, p*q)
    print(C)
    d, n = getSecretKey(p, q, e)
    print(decrypt(C, d, n))
