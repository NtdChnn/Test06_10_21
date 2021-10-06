class MyInt:
    def __init__(self, input):
        self.Ip = input
        self.isP = True
        self.checkP = True
        self.showP = ''
        self.showS = ''

    def isPrime(self):
        if self.Ip <= 1:
            self.isP = False
        for e in range(2,self.Ip):
            if self.Ip % e == 0:
                self.isP = False
        return f'{self.Ip} isPrime : {self.isP}'

    def showPrime(self):
        self.showP = 'Prime number between 2 and ' + str(self.Ip) + ' : '
        for e in range(2, self.Ip+1):
            self.checkP = True
            for i in range(2, e):
                if e % i == 0:
                    self.checkP = False
            if self.checkP :
                self.showP = self.showP + str(e) + ' '
        if self.Ip <= 1:
            self.showP = self.showP + '!!!A prime number is a natural number greater than 1'
        return self.showP

    def __sub__(self, other):
        Ans = self.Ip - (int(other.Ip/2))
        self.showS = str(self.Ip) + ' - ' + str(other.Ip) + ' = ' + str(Ans)
        return self.showS

IpA, IpB = input(' *** class MyInt *** \nEnter 2 number : ').split(' ')
IpA = int(IpA)
IpB = int(IpB)
A = MyInt(IpA)
B = MyInt(IpB)
print(A.isPrime())
print(B.isPrime())
print(A.showPrime())
print(B.showPrime())
print(A-B)
