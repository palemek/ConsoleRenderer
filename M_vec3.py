import math
def add(v1,v2):
    return [v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2]]

def sub(v1,v2):
    return [v1[0]-v2[0],v1[1]-v2[1],v1[2]-v2[2]]

def dot(v1,v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

def div(v, f):
    return [v[0]/f,v[1]/f,v[2]/f]

def mul(v, f):
    return [v[0]*f,v[1]*f,v[2]*f]

def len(v):
    return math.sqrt(dot(v,v))

def inv(v):
    return mul(v,-1);

def scale(v,s):
    return [v[0]*s[0],v[1]*s[1],v[2]*s[2]];

def cross(v1,v2):
    return [v1[1]*v2[2]-v1[2]*v2[1],v1[2]*v2[0]-v1[0]*v2[2],v1[0]*v2[1]-v1[1]*v2[0]]
