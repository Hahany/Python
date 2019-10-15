import numpy
f = open('matrix.txt')
lines = f.readlines()
f.close()
# print(lines)
m,n = lines[0].split()
# print(m,n)
m = int(m)
n = int(n)
A = numpy.zeros(shape=(m,n))
for i,line in enumerate(lines[1:1+m]):
#     print(i,line,end='')
    for j,a in enumerate(line.split()):
#         print(j,a)
        A[i][j] = float(a)
# print('矩阵A','\n',A)
m1,n1 = lines[m+1].split()
# print(m1,n1)
m1 = int(m1)
n1 = int(n1)
B = numpy.zeros(shape=(m1,n1))
# print(B)
for i,line in enumerate(lines[m+2:m+m1+2]):
#     print(i,line)
    for j,b in enumerate(line.split()):
        B[i][j] = float(b)
# print('矩阵B','\n',B)
# print(B[2][1])
if n != m1 :
    error('行列不相等')
    exit(0)
C = numpy.zeros(shape=(m,n1))
for i in range(m):
    for j in range(n1):
        for k in range(n):
            C[i][j]+=A[i][k]*B[k][j]
print(C)