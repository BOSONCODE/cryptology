class Caesar:
    def __init__(self, k):
        self.k = k
        self.charset = {}
        self.mp = {}

    def setK(self, k):
        self.k = k

    def setCharset(self):
        for i in range(26):
            self.charset[chr(ord('a')+i)] = i
            self.mp[i] = chr(ord('a')+i)

    def Encrypt(self, PlainText):
        charSetSize = len(self.charset)
        lenp = len(PlainText)
        ans = ""
        for i in range(lenp):
            item = PlainText[i]
            if item == ' ':
                ans += ' '
                continue
            ans += self.mp[(self.charset[item] + self.k)%charSetSize]
        return ans

    def Decrypt(self, CipherText):
        charSetSize = len(self.charset)
        lenc = len(CipherText)
        ans = ""
        for i in range(lenc):
            item = CipherText[i]
            if item == ' ':
                ans += ' '
                continue
            ans += self.mp[(self.charset[item] - self.k + charSetSize)%charSetSize]
        return ans


if __name__ == '__main__':
    s = 'meet me after the toga party'
    test = Caesar(3)
    test.setCharset()
    print(test.Encrypt(s))
    ct = 'gcua vq dtgcm'
    for k in range(26):
        test.setK(k)
        print(test.Decrypt(ct))
