import math
import M_vec3 as vec3

def nrm(tri):
    n = vec3.cross(vec3.sub(tri[1],tri[0]),vec3.sub(tri[2],tri[0]));
    return vec3.div(n,vec3.len(n));
def project(x,tri):
    n = tri[4]#nrm(tri)
    a = tri[0]
    return vec3.sub(x,vec3.mul(n,vec3.dot(vec3.sub(a,x),n)));
def distToPlane(x,tri):
    n = tri[4]#nrm(tri)
    a = tri[0]
    return math.fabs(vec3.dot(n,vec3.sub(a,x)));

#(trace start, plane normal, point on plane, trace dir)
def tracePlaneDist(x,tri,v):
    n = tri[4]#nrm(tri)
    h = distToPlane(x,tri)
    return math.fabs(h/vec3.dot(v,n));
