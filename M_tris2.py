import M_vec2 as mVec2

def VertInTri(tri,vert):
    rightToAB = mVec2.dot(mVec2.orth(mVec2.sub(tri[1],tri[0])),mVec2.sub(vert,tri[1])) <= 0
    if not rightToAB:
        return False;
    rightToBC = mVec2.dot(mVec2.orth(mVec2.sub(tri[2],tri[1])),mVec2.sub(vert,tri[2])) <= 0
    if not rightToBC:
        return False;
    rightToCA = mVec2.dot(mVec2.orth(mVec2.sub(tri[0],tri[2])),mVec2.sub(vert,tri[0])) <= 0
    if not rightToCA:
        return False;
    return True;
