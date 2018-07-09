import M_vec3 as mVec3
import M_vec2 as mVec2
import M_tris3 as mTri3
import M_tris2 as mTri2
import M_objects3 as mObjects
import math
from ctypes import *

def Initialize(xres, yres):
  global XRES
  global YRES
  global GRAPHICS
  global DEPTH
  global OBJECTS
  XRES = xres
  YRES = yres
  GRAPHICS = []
  DEPTH = []
  OBJECTS = []
  global FPS
  #initialization of Draw and depth buffer
  for i in range(0,YRES):
    GRAPHICS.append([])
    DEPTH.append([])
    for j in range(0,XRES):
      GRAPHICS[i].append('_')#[j] = ""
      DEPTH[i].append(0)
  
#camSett = [pos,vx,vy,vz,height,width]
def Update(camSett):
  _clearScreen();
  for o in OBJECTS:
    for tri in o.TRIS:
      _drawTri(mObjects.triToWS(tri,o), camSett);
  _drawScreen();

def AddObject(obj):
  OBJECTS.append(obj);

def PrintFPS(fps):
  global FPS
  FPS = fps;

def _clearScreen():
  for i in range(0,YRES):
    for j in range(0,XRES):
      GRAPHICS[i][j] = 'X';
      DEPTH[i][j] = 0;
  
#cS = [pos,vx,vy,vz,height,width]
def _drawTri(tris, cS):

    #if face normal is away from camera return
    if mVec3.dot(tris[4],cS[2]) < 0:
      return
    
    tri = [_projectVertToCamera(tris[0], cS),
           _projectVertToCamera(tris[1], cS),
           _projectVertToCamera(tris[2], cS)];

    n = int(math.floor(min(tri[0][1],tri[1][1],tri[2][1])*YRES))
    m = int(math.floor(max(tri[0][1],tri[1][1],tri[2][1])*YRES)) + 1
    p = int(math.floor(min(tri[0][0],tri[1][0],tri[2][0])*XRES))
    q = int(math.floor(max(tri[0][0],tri[1][0],tri[2][0])*XRES)) + 1
    for i in range(n,m):
        for j in range(p,q):
            pkt = [((j+0.5)/XRES),((i+0.5)/YRES)]
            if (mTri2.VertInTri(tri,pkt)):
                pixelPos = mVec3.add(cS[0],
                                     mVec3.add(
                                       mVec3.mul(cS[1],2*(pkt[0]-0.5)*cS[5]),
                                       mVec3.mul(cS[3],2*(pkt[1]-0.5)*cS[4])
                                     ))
                dpth = mTri3.tracePlaneDist(pixelPos,tris, cS[2])
                if dpth > _getDepth(j,i):
                    _drawPixel(j, i, tris[3]);
                    _drawDepth(j, i, dpth)


class COORD(Structure):
    pass
  
COORD._fields_ = [("X", c_short), ("Y", c_short)]

def _drawScreen():
  temp = ""
  
  global FPS
  temp += str(FPS)
  temp += '\n'
  
  for i in range(0,YRES):
    for j in range(0,XRES):
      temp += GRAPHICS[i][j]
    temp += '\n'

  h = windll.kernel32.GetStdHandle(-11)
  windll.kernel32.SetConsoleCursorPosition(h, COORD(0, 0))
  
  print(temp)

def _drawPixel(i,j,m):
    if (i >= 0 and i < XRES and j >= 0 and j < YRES):
        GRAPHICS[j][i] = m
def _drawDepth(i,j,d):
    if (i >= 0 and i < XRES and j >= 0 and j < YRES):
        DEPTH[j][i] = d;
def _getDepth(i,j):
    if (i >= 0 and i < XRES and j >= 0 and j < YRES):
        return DEPTH[j][i]
    else:
        return 10000;
        
#cS = [pos,vx,vy,vz,height,width]
def _projectVertToCamera(vert, cS):
    rel = mVec3.sub(vert,cS[0])
    x = 0.5 + (mVec3.dot(rel,cS[1])/(2*cS[5]))
    y = 0.5 + (mVec3.dot(rel,cS[3])/(2*cS[4]))
    return [x, y]

#cS = [pos,vx,vy,vz,height,width]
def _calcVertDepth(vert, cS):
    rel = mVec3.sub(vert,cS[0])
    return math.fabs(mVec3.dot(rel,cS[2]))
  
