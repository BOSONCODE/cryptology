'''
编码规则:
1.重复字母插入X
 "balloon" 转变为 "ba lx lo on"
2.同一行的两个字母, 以右边的字母来代替
 如"ar"用"RM"代替
3.同一列的两个字母，以下边的字母来代替
 如“mu” 用“CM”代替 
4.否则用对角线的字母代替
 如“hs” 用“BP”代替
Example
Balloonba lx lo on
 ib su pm na
表采用的关键词是 "MONARCHY"
M O N A R
C H Y B D
E F G IJ K
L P Q S T
U V W X Z
'''

class PlayFair:
    def __init__(self, keyWord, doubleLocation):
        return 
        self.keyWord = keyWord
        lenword = len(keyWord)
        cnt = 0
        self.table = [[0]for i in range(5)]
        for i in range(5):
            for j in range(5):
                table[i][j] = keyWord[cnt]
                cnt = cnt + 1
                if cnt == lenword:
                    break
            if cnt == lenword:
                break
        for i in range(5):
            for j in range(5):
                if table[i][j] != None:
                    for c in range(26):
                        if vis[c] == 1:
                            continue
                        vis[c] = 1
                        table[i][j] = chr(ord('a') + c)
                        break
    def preHandle(self, s):
        ans = ""
        lens = len(s)
        i = 0
        while i < lens:
            ans += s[i]
            if i + 1 == lens:
                break
            if s[i] == s[i+1]:
                ans += 'X'
            else:
                ans += s[i+1]
                i = i + 1
            i = i + 1
        return ans

    def atSameRow(self, a, b):

        return False

    def atSameColumn(self, a, b):

        return False
    
    def Encrypt(self, PlainText):
        PlainText = self.preHandle(PlainText)
        ans = ""
        i = 0
        lens = len(PlainText)
        while i < lens:
            if i + 1 == lens:
                ans += s[i]
                break
            if self.atSameRow(s[i], s[i+1]) == True:
                a, b = ReplaceRowRight(s[i], s[i+1])
                ans += a
                ans += b
            elif self.atSameColumn(s[i], s[i+1]) == True:
                a, b = ReplacColumnDown(s[i], s[i+1])
                ans += a
                ans += b
            else:
                a, b = ReplaceDiagonal(s[i], s[i+1])
                ans += a
                ans += b
            i = i + 2
        return ans
if __name__ == '__main__':
    test = PlayFair('MONARCHY', [2, 3])
    print(test.preHandle('balloon'))
