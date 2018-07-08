import math

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
