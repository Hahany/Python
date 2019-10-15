import math
class triangle():
    #用于计算三角形边长、周长以及面积
    def __init__(self,p0,p1,p2):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        
    def lenth(self):
        l0 = math.sqrt ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        l1 = math.sqrt ((p0[0]-p2[0])**2+(p0[1]-p2[1])**2)
        l2 = math.sqrt ((p1[0]-p0[0])**2+(p1[1]-p0[1])**2)
        L = l0+l1+l2
        return l0,l1,l2,L
    
    def area(self):
        '''
        面积计算公式;
        x1=p0[0] y1=p0[1]
        x2=p1[0] y2=p1[1]
        x3=p2[0] y3=p2[1]
        s = 绝对值（行列式[[(x3-x1),(y3-y1)],[(x2-x1),(y2-y1)]]）
        '''
        a = [p2[0]-p0[0],p2[1]-p0[1]]
        b = [p1[0]-p0[0],p1[1]-p0[1]]
        s = abs((a[0]*b[1]-a[1]*b[0])/2)
        return s
      
p0 = [0,0]
p1 = [2,0]
p2 = [1,1]
t = triangle(p0,p1,p2)
l0,l1,l2,L = t.lenth()
print('三角形的三边长分别为：%f,%f,%f.周长为：%f' %(l0,l1,l2,L))
s = t.area()
print('三角形面积是：%f'%s)
