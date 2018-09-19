import M_vec3 as mVec3
import M_tris3 as mTri
class OBJECT:
  def __init__(self):
    self.TRIS = [];
    self.POSITION = [0,0,0];
    self.SCALE = [1,1,1];
    self.VX = [1,0,0]
    self.VY = [0,1,0]
    self.VZ = [0,0,1]

  def rotateX90(self):
    temp = self.VY
    self.VY = mVec3.inv(self.VZ)
    self.VZ = temp

  def rotateY90(self):
    temp = self.VZ
    self.VZ = mVec3.inv(self.VX)
    self.VX = temp
    
  def rotateZ90(self):
    temp = self.VX
    self.VX = mVec3.inv(self.VY)
    self.VY = temp

  def importNew(self, path):
    file = open(path,"r")
    tempTris = []
    tempNrms = []
    tempVerts = []
    for line in file:
      words = line.split()
      if words[0] == 'v':
        tempVerts.append([float(words[1]),float(words[2]),float(words[3])])
      elif words[0] == 'vn':
        tempNrms.append([float(words[1]),float(words[2]),float(words[3])])
      elif words[0] == 'f':
        tempTris.append([tempVerts[int(words[1].split("//")[0])-1],
                        tempVerts[int(words[2].split("//")[0])-1],
                        tempVerts[int(words[3].split("//")[0])-1],
                        chr((len(tempTris)%91) + 34),
                        tempNrms[int(words[1].split("//")[1])-1]
                        ])
    self.TRIS = tempTris;

class BOX(OBJECT):
  def __init__(self):
    OBJECT.__init__(self);
    verts = [
        [ -1, -1,  1],
        [  1, -1,  1],
        [  1,  1,  1],
        [ -1,  1,  1],
        [ -1, -1, -1],
        [  1, -1, -1],
        [  1,  1, -1],
        [ -1,  1, -1]
        ]
    self.TRIS.extend(TrisFromQuad(verts[0],verts[3],verts[2],verts[1],'.'))
    self.TRIS.extend(TrisFromQuad(verts[4],verts[5],verts[6],verts[7],'_'))
    self.TRIS.extend(TrisFromQuad(verts[0],verts[1],verts[5],verts[4],'o'))
    self.TRIS.extend(TrisFromQuad(verts[2],verts[3],verts[7],verts[6],'*'))
    self.TRIS.extend(TrisFromQuad(verts[0],verts[4],verts[7],verts[3],'-'))
    self.TRIS.extend(TrisFromQuad(verts[1],verts[2],verts[6],verts[5],'!'))

def dirVecToWS(v,obj):
  return mVec3.add(
    mVec3.add(
      mVec3.mul(obj.VX,v[0]),
      mVec3.mul(obj.VY,v[1])),
    mVec3.mul(obj.VZ,v[2]))

def triToWS(tri,obj):

  return [mVec3.add(mVec3.scale(dirVecToWS(tri[0],obj),obj.SCALE),obj.POSITION),

          mVec3.add(mVec3.scale(dirVecToWS(tri[1],obj),obj.SCALE),obj.POSITION),

          mVec3.add(mVec3.scale(dirVecToWS(tri[2],obj),obj.SCALE),obj.POSITION),

          tri[3],

          dirVecToWS(tri[4],obj)]

def TrisFromQuad(A,B,C,D,M):
    tris = [[D,B,A,M],[D,C,B,M]]
    tris[0].append(mTri.nrm(tris[0]))
    tris[1].append(mTri.nrm(tris[1]))
    return tris;
