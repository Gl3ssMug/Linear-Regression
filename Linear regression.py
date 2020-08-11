import math
import matplotlib.pyplot as plt
import numpy as np

data = [[0,20.1],[60,23],[120,26.9],[180,30],[240,33.1],[300,36.9]]

datax = []
datay = []


class LinearRegression():
    
    def __init__(self):
        pass
    
    def sigmax(self):
        a1 = 0
        for a in range(len(data)):
            a1 = a1+(data[a][0])
        return a1
    
    def xbar(self):
        return self.sigmax() / len(data)
    
    def sigmaxsq(self):
        b1 = 0
        for b in range(len(data)):
            b1 = b1+(data[b][0])**2
        return b1
    
    def sigmay(self):
        d1 = 0
        for d in range(len(data)):
            d1 += data[d][1]
        return d1
    
    def ybar(self):
        return self.sigmay() / len(data)
    
    def sigmaysq(self):
        e1 = 0
        for e in range(len(data)):
            e1 += (data[e][1])**2
        return e1
    
    def sigmaxy(self):
        g1 = 0
        for g in range(len(data)):
            g1 += (data[g][0])*(data[g][1])
        return g1
    
    def SXX(self):
        return ((self.sigmaxsq()) - (self.sigmax()**2) / len(data))
        
    def SYY(self):
        return ((self.sigmaysq()) - ((self.sigmay())**2 / len(data)))
    
    def SXY(self):
        return ((self.sigmaxy()) - ((self.sigmax()*self.sigmay()) / len(data)))
    
    def b(self):
        return self.SXY() / self.SXX()
    
    def a(self):
        return (self.b()*-self.xbar()) + (self.ybar())
     
    def linregres(self):
        return ('y =  '+str(self.b())+'x'+' + '+str(self.a()))
        
    def PMCC(self):
        pmcc = ((self.SXY()) / math.sqrt(self.SXX()*self.SYY()))
        return ('PMCC = '+str(pmcc))
    
    def scatter(self):
        for i in range(len(data)):
            datax.append(data[i][0])
        for p in range(len(data)):
            datay.append(data[p][1])
            
        
        
if __name__ == '__main__':
    lr = LinearRegression()
    lr.scatter()
    print(lr.linregres())
    print(lr.PMCC())
    m = lr.b()
    c = lr.a()
    
    x = np.linspace(0,300,10)
    y = m*x + c
    plt.plot(x, y, 'r')
    plt.scatter(datax, datay)
    plt.show()
    
    inp = input('predict values?')
    if inp == 'y':
        x = float(input('value for x?'))
        y = (m*x) + c
        print(y)
    else:
        pass
    
    
    
    
    
    
    

