import math

def mul(a,f):
    return [a[0]*f,a[1]*f];
def div(a,b):
    return [a[0]/b,a[1]/b];
def sub(a,b):
    return [a[0]-b[0],a[1]-b[1]];
def add(a,b):
    return [a[0]+b[0],a[1]+b[1]];
def dot(a,b):
    return a[0]*b[0] + a[1]*b[1];
def len(a):
    return math.sqrt(dot(a,a));
def orth(v):
    return [v[1],-v[0]];
def floor(a):
    return [math.floor(a[0]),math.floor(a[1])];
def ceil(a):
    return [math.ceil(a[0]),math.ceil(a[1])];
def scale(a,b):
    return [a[0]*b[0],a[1]*b[1]];
