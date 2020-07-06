import math

def vector_substract(v,w):
    if len(v)==len(w):
        s = 0
        for i in range(len(v)):
            s += (int(v[i])-int(w[i]))**2
        s = math.sqrt(s)
        return s

a,b,c = input('v벡터 값:').split()
x,y,z = input('w벡터 값:').split()

v = [a,b,c]
w = [x,y,z]

print(vector_substract(v,w))
            
