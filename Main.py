import time
import msvcrt
import M_vec3 as mVec3
import M_vec2 as mVec2
import M_tris3 as mTri
import M_renderer as mRenderer
import M_objects3 as mObjects
import keyboard
import math

CAMERAPOS = [-5,0,0]
CAMERAVX = [1,0,0]
CAMERAVY = [0,1,0]
CAMERAVZ = [0,0,1]

CAMERAH = 1
CAMERAW = 1


def gameLoop():
    global lastTime
    dt = time.perf_counter() - lastTime
    if dt == 0:
        dt = 1;
    
    lastTime = time.perf_counter()
    fps = min(120,1.0/dt)
        
    mechanics(dt)
    mRenderer.PrintFPS(fps)
    mRenderer.Update([CAMERAPOS,CAMERAVX,CAMERAVY,CAMERAVZ,CAMERAH,CAMERAW])

def mechanics(dt):
    ti = time.perf_counter()
    global b1,b2,b3
    global CAMERAPOS,CPF, CPZ,CRZ,CPR,CRX
    global GO
    CRX = 0
    CPR = 0
    CPZ = 0
    CPF = 0
    CRZ = 0
    #b1.POSITION = mVec3.add(b1.POSITION,[dt/2,0,0])
    if keyboard.is_pressed('w'):
        CPF = dt
    if keyboard.is_pressed('s'):
        CPF = -dt
    if keyboard.is_pressed('d'):
        CPR = dt
    if keyboard.is_pressed('a'):
        CPR = -dt
    if keyboard.is_pressed('q'):
        CPZ = dt
    if keyboard.is_pressed('e'):
        CPZ = -dt
    if keyboard.is_pressed('i'):
        CRR = dt
    if keyboard.is_pressed('k'):
        CRR = -dt
    if keyboard.is_pressed('l'):
        CRZ = dt
    if keyboard.is_pressed('j'):
        CRZ = -dt
    if keyboard.is_pressed('p'):
        mRenderer.OLD = not mRenderer.OLD
    if keyboard.is_pressed('o'):
        mRenderer.TEST = not mRenderer.TEST
    

    CPF*=5
    CPZ*=5
    CPR*=5

    global CAMERAVX,CAMERAVY,CAMERAVZ

    CAMERAPOS = mVec3.add(CAMERAPOS,mVec3.mul(CAMERAVY,CPF))
    CAMERAPOS = mVec3.add(CAMERAPOS,mVec3.mul(CAMERAVX,CPR))
    CAMERAPOS = mVec3.add(CAMERAPOS,mVec3.mul(CAMERAVZ,CPZ))
    
    rS = -2
    CAMERAVY = [math.cos(CRZ*rS)*CAMERAVY[0] - math.sin(CRZ*rS)*CAMERAVY[1],math.sin(CRZ*rS)*CAMERAVY[0] + math.cos(CRZ*rS)*CAMERAVY[1],0]
    print(CAMERAPOS)
    print(CAMERAVY)    
    CAMERAVX = mVec3.cross(CAMERAVY,CAMERAVZ)
    ti = (time.perf_counter() - ti)*1000
    print("game mechanics update: " + str(ti) + " ms")
    print("render type is : " + ("old" if mRenderer.OLD else "new"))    
    

def startGameMechanics():
    print("start")
    #global b1,b2,b3
    #b1 = mObjects.BOX()
    #b1.SCALE = [3,1,1]
    #
    #b2 = mObjects.BOX()
    #b2.SCALE = [1,3,1]
    #
    #b3 = mObjects.BOX()
    #b3.SCALE = [1,1,3]
    #mRenderer.AddObject(b1)
    #mRenderer.AddObject(b2)
    #mRenderer.AddObject(b3)
    n = mObjects.OBJECT()
    mObjects.OBJECT.importNew(n,"untitled.obj")
    mRenderer.AddObject(n)
    global CRZ,CPZ
    CRZ = 0
    CPZ = 0
    global lastTime
    lastTime = 0

mRenderer.Initialize(80,40)
startGameMechanics()

while(True):
    gameLoop()
