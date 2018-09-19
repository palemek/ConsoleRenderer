import M_vec3 as mVec3
import M_vec2 as mVec2
import M_tris3 as mTri3
import M_tris2 as mTri2
import M_objects3 as mObjects
import math
import time
from ctypes import *

def Initialize(xres, yres):
  global XRES
  global YRES
  global GRAPHICS
  global DEPTH
  global OBJECTS
  global OLD
  global TEST
  global GRADIENT
  TEST = False
  OLD = False
  XRES = xres
  YRES = yres
  GRAPHICS = []
  DEPTH = []
  OBJECTS = []
  GRADIENT = """ .:-=+*#%@""" 
  GRADIENTLONG = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """

  global isOrtho,focal
  isOrtho = False #if we enable this, in M_tris2D we should chagnge in Vert in tri all <= to >=
  focal = 1
  
  global FPS
  #initialization of Draw and depth buffer
  for i in range(0,YRES):
    GRAPHICS.append([])
    DEPTH.append([])
    for j in range(0,XRES):
      GRAPHICS[i].append(' ')#[j] = ""
      DEPTH[i].append(0)
  
#camSett = [pos,vx,vy,vz,height,width]
def Update(camSett):
  ti = time.perf_counter()
  _clearScreen();
  ti = (time.perf_counter() - ti)*1000
  print("clear screen time: " + str(ti) + " ms")

  ti = time.perf_counter()
  for o in OBJECTS:
    for tri in o.TRIS:
      _drawTri(mObjects.triToWS(tri,o), camSett);
  ti = (time.perf_counter() - ti)*1000
  print("update screen time: " + str(ti) + " ms")

  ti = time.perf_counter()
  _drawScreen();
  ti = (time.perf_counter() - ti)*1000
  print("draw screen time: " + str(ti) + " ms")
  

def AddObject(obj):
  OBJECTS.append(obj);

def PrintFPS(fps):
  global FPS
  FPS = fps;

def _clearScreen():
  
  for i in range(0,YRES):
    for j in range(0,XRES):
      GRAPHICS[i][j] = ' ';
      DEPTH[i][j] = 100000;
#cS = [pos,vx,vy,vz,height,width]
def _drawTri(tris, cS):
    global isOrtho
    #if face normal is away from camera return
    #WRONG! GIVES WRONG RESULTS WITH PERSP
    #i should check vs some point on it
    #if mVec3.dot(tris[4],cS[2]) > 0:
    #  return
    if mVec3.dot(tris[4],mVec3.sub(tris[0],cS[0])) > 0:
      return
    
    tri = [_projectVertToCamera(tris[0], cS),
           _projectVertToCamera(tris[1], cS),
           _projectVertToCamera(tris[2], cS)];
    #to wponizej wyglada zle ale znaczano usprawnia
    #if (tri[0][2] <=0 or tri[1][2] <= 0 or tri[2][2] <= 0):
    #  return
    


    
    #tracing depth and stuff for pixels we know that trace hit them
    #'j' - x pixel pos, 'i' - y pixel pos, 'point' - view coord(left up corner is 0,0), 'tris' - current triangle  
    def updatePerPixel(j,i,pkt,tris,cS):
      global isOrtho, focal, GRADIENT
      ################
      
      if isOrtho:
        relative = mVec3.add(
                            mVec3.mul(cS[1],2*(pkt[0]-0.5)*cS[5]),
                            mVec3.mul(cS[3],2*(pkt[1]-0.5)*cS[4])
                          )
      else:
        relative = mVec3.add(
                            mVec3.mul(cS[2],focal),
                            mVec3.add(
                                mVec3.mul(cS[1],2*(pkt[0]-0.5)*cS[5]),
                                mVec3.mul(cS[3],2*(pkt[1]-0.5)*cS[4])
                                )
                             )
      if isOrtho:
        dpth = mTri3.tracePlaneDist(mVec3.add(cS[0],relative),tris, cS[2])
      else:
        dpth = mTri3.tracePlaneDist(mVec3.add(cS[0],relative),tris, mVec3.div(relative,mVec3.len(relative)))
      if dpth < _getDepth(j,i):
        light = math.fabs(mVec3.dot(tris[4],[0.5,0.5,-0.707]))
        mat = GRADIENT[int(light * 10)]
        _drawPixel(j, i, mat)
        #COLOR FROM MATERIAL
        #_drawPixel(j, i, tris[3])
        _drawDepth(j, i, dpth)
      ################

    
    global OLD
    
    if not OLD:
      tva = tri[0] if (tri[0][0] <= tri[1][0] and tri[0][0] <=tri[2][0]) else (tri[1] if tri[1][0] <= tri[2][0] else tri[2])
      tvb = tri[0] if (tri[0][0] >= tri[1][0] and tri[0][0] >=tri[2][0]) else (tri[1] if tri[1][0] >= tri[2][0] else tri[2])
      tvc = tri[0] if (tva != tri[0] and tvb != tri[0]) else (tri[1] if (tva != tri[1] and tvb != tri[1]) else tri[2])

      tva = mVec2.scale(tva,[XRES,YRES])
      tvb = mVec2.scale(tvb,[XRES,YRES])
      tvc = mVec2.scale(tvc,[XRES,YRES])
      tp = int(math.floor(tva[0] + 0.5))
      tq = int(math.floor(tvb[0] + 0.5))
      
      miny = int(min(tva[1],tvb[1],tvc[1])+0.5)
      maxy = int(max(tva[1],tvb[1],tvc[1])+0.5)
      
      def calca(a,b):
        return ((a[1]-b[1])/(a[0]-b[0])) if (a[0]-b[0]) != 0 else 1
      def calcb(a,b):
        if (a[0]-b[0]) != 0:
          return (a[0]*b[1]-a[1]*b[0])/(a[0]-b[0])
        else:
          return 0

      if tva[0]!=tvb[0]:
        aab = calca(tva,tvb)
        aac = calca(tva,tvc)
        acb = calca(tvc,tvb)
        bab = calcb(tva,tvb)
        bac = calcb(tva,tvc)
        bcb = calcb(tvc,tvb)
        cxpos = math.floor(tvc[0] + 0.5)
        for j in range(max(0,tp), min(XRES,tq)):
          bot = aab*j+bab
          if j < cxpos:
            #przed przelamaniem wierzcholka c
            if TEST:
              print("before" + "*"*30)
            top = aac*j+bac
          elif j > cxpos:
            if TEST:
              print("after" + "*"*30)
            #po przelamaniu wierzcholka c
            top = acb*j+bcb
          else:
            if TEST:
              print("else" + "*"*30)
            top = tvc[1]
          if TEST:
            print(str([bot,top,tvc]) + "*"*20)
          if bot > top:
            temp = bot
            bot = top
            top = temp
          bot = max(miny,min(maxy,math.floor(bot+0.5)))
          top = max(miny,min(maxy,math.floor(top+0.5)))
          
          for i in range(bot,top):
            #update
            pkt = [(j/XRES),(i/YRES)]
            updatePerPixel(j,i,pkt,tris,cS)
             
    else:
    ##OLD METHOD
      
      n = min(YRES,max(0,int(math.floor(min(tri[0][1],tri[1][1],tri[2][1])*YRES))))
      m = min(YRES,max(0,int(math.floor(max(tri[0][1],tri[1][1],tri[2][1])*YRES)) + 1))
      p = min(XRES,max(0,int(math.floor(min(tri[0][0],tri[1][0],tri[2][0])*XRES))))
      q = min(XRES,max(0,int(math.floor(max(tri[0][0],tri[1][0],tri[2][0])*XRES)) + 1))
    
      for i in range(n,m):
        for j in range(p,q):
          pkt = [((j+0.5)/XRES),((i+0.5)/YRES)]
          if (mTri2.VertInTri(tri,pkt)):
            updatePerPixel(j,i,pkt,tris,cS)
       
    


class COORD(Structure):
    pass
  
COORD._fields_ = [("X", c_short), ("Y", c_short)]

def _drawScreen():
  temp = ""
  global FPS
  temp += " "*(8 - min(5,len(str(FPS)))) + str(FPS)[:5]
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
    
    d = mVec3.dot(rel,cS[2]) #dist along camera forward to point
    if d == 0:
      d = 1
    if isOrtho:
      x = 0.5 + (mVec3.dot(rel,cS[1])/(2*cS[5]))
      y = 0.5 + (mVec3.dot(rel,cS[3])/(2*cS[4]))
    else:
      s = focal/d 
      x = 0.5 + (s*mVec3.dot(rel,cS[1])/(2*cS[5]))
      y = 0.5 + (s*mVec3.dot(rel,cS[3])/(2*cS[4]))

    return [x, y, d]
    

#cS = [pos,vx,vy,vz,height,width]
def _calcVertDepth(vert, cS):
    rel = mVec3.sub(vert,cS[0])
    if isOrtho:
      return math.fabs(mVec3.dot(rel,cS[2]))
    else:
      return mVec3.len(mVec3.sub(vert,cS[0]))
  
