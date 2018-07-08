from time import sleep
from time import clock
import msvcrt
import M_vec3 as mVec3
import M_vec2 as mVec2
import M_tris3 as mTri
import M_renderer as mRenderer
import M_objects3 as mObjects
import math

CAMERAPOS = [0,-5,0]
CAMERAVX = [1,0,0]
CAMERAVY = [0,1,0]
CAMERAVZ = [0,0,1]

CAMERAH = 5
CAMERAW = 5

def gameLoop():
    global lastTime
    dt = clock() - lastTime
    lastTime = clock()
    if dt == 0:
        dt = 1;
    
    fps = int(1/dt)
        
    mechanics(dt)
    mRenderer.PrintFPS(fps)
    mRenderer.Update([CAMERAPOS,CAMERAVX,CAMERAVY,CAMERAVZ,CAMERAH,CAMERAW])
    #sleep(dt)

def mechanics(dt):
    global b1,b2,b3
    global CAMERAPOS,CPZ,CRZ
    b1.POSITION = mVec3.add(b1.POSITION,[dt/2,0,0])
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8')
        if key == 'w':
            CPZ += dt
        if key == 's':
            CPZ -= dt
        if key == 'a':
            CRZ += dt
        if key == 'd':
            CRZ -= dt
    
    CAMERAPOS[0] = 5 * math.sin(CRZ/2.0);
    CAMERAPOS[1] = 5 * math.cos(CRZ/2.0);
    CAMERAPOS[2] = CPZ * 5
    #tu bedziemy chcieli tak obliczyc cameraV zeby patrzyl na srodek
    global CAMERAVX,CAMERAVY,CAMERAVZ
    CAMERAVY = mVec3.div(mVec3.sub([0,0,0],CAMERAPOS),mVec3.len(CAMERAPOS))
    t = CAMERAVY
    txy = math.sqrt(t[0]*t[0]+t[1]*t[1])
    CAMERAVZ = [t[2]*t[0]/txy, t[2]*t[1]/txy, -txy]
    CAMERAVX = mVec3.cross(CAMERAVY,CAMERAVZ)
    

def startGameMechanics():
    print("start")
    global b1,b2,b3
    b1 = mObjects.BOX()
    b1.SCALE = [3,1,1]
    
    b2 = mObjects.BOX()
    b2.SCALE = [1,3,1]
    
    b3 = mObjects.BOX()
    b3.SCALE = [1,1,3]
    mRenderer.AddObject(b1)
    mRenderer.AddObject(b2)
    mRenderer.AddObject(b3)
    global CRZ,CPZ
    CRZ = 0
    CPZ = 0
    global lastTime
    lastTime = 0

mRenderer.Initialize(60,30)
startGameMechanics()

while(True):
    gameLoop()
