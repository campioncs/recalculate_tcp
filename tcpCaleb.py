import numpy as np

def rotation(qa):
    norm = np.sqrt(sum(np.square(qa)))
    qa = qa / norm

    r = np.zeros((3,3))
    r[0][0] = 1 - 2 * (np.square(qa[2]) + np.square(qa[3]))
    r[0][1] = 2 * (qa[1] * qa[2] - qa[0] * qa[3])
    r[0][2] = 2 * (qa[1] * qa[3] + qa[0] * qa[2])
    r[1][0] = 2 * (qa[1] * qa[2] + qa[0] * qa[3])
    r[1][1] = 1 - 2 * (np.square(qa[1]) + np.square(qa[3]))
    r[1][2] = 2 * (qa[2] * qa[3] - qa[0] * qa[1])
    r[2][0] = 2 * (qa[1] * qa[3] - qa[0] * qa[2])
    r[2][1] = 2 * (qa[2] * qa[3] + qa[0] * qa[1])
    r[2][2] = 1 - 2 * (np.square(qa[1]) + np.square(qa[2]))    

    return r

def multiply(r, v):
    return np.dot(r,v)
    
testQ = np.array([2.5, 4.5, 6.5, 8.5])
testD = np.array([5.0, 5.0, 5.0])

initialPos = np.array([0.0, 0.0, 0.0])
initialPosIn = input("Type initial X Y Z values serperated by a space: ").split()
initialPos[0] = float(initialPosIn[0])
initialPos[1] = float(initialPosIn[1])
initialPos[2] = float(initialPosIn[2])
                      
quat = np.array([0.0, 0.0, 0.0, 0.0])
quatIn = input("Type values for q1 q2 q3 q4 seperated by a space: ").split()
quat[0] = float(quatIn[0])
quat[1] = float(quatIn[1])
quat[2] = float(quatIn[2])
quat[3] = float(quatIn[3])

cog = np.array([0.0, 0.0, 0.0, 0.0])
cogIn = input("Type vaues for mass cogX cogY cogZ seperated by a space: ").split()
cog[0] = float(cogIn[0])
cog[1] = float(cogIn[1])
cog[2] = float(cogIn[2])
cog[3] = float(cogIn[3])

orient = np.array([0.0, 0.0, 0.0, 0.0])
orientIn = input("Type values for cog orient q1 q2 q3 q4 seperated by a space: ").split()
orient[0] = float(orientIn[0])
orient[1] = float(orientIn[1])
orient[2] = float(orientIn[2])
orient[3] = float(orientIn[3])

moi = np.array([0.0, 0.0, 0.0])
moiIn = input("Tye moments of inertia iX iY iZ seperated by a space: ").split()
moi[0] = float(moiIn[0])
moi[1] = float(moiIn[1])
moi[2] = float(moiIn[2])

disp = np.array([0.0, 0.0, 0.0])
dispIn = input("Type displacement values for x y z in mm seperated by a space: ").split()
disp[0] = float(dispIn[0])
disp[1] = float(dispIn[1])
disp[2] = float(dispIn[2])

newPos = np.array([0.0, 0.0, 0.0])
good = True
while good:
    frame = input("type T for tool, or W for world: ")
    if frame == 'T' or frame == 't':
        rotated = rotation(quat)
        displaced = multiply(rotated, disp)
        newPos[0] = displaced[0] + initialPos[0]
        newPos[1] = displaced[1] + initialPos[1]
        newPos[2] = displaced[2] + initialPos[2]
        good = False
    if frame == 'W' or frame == 'w':
        newPos[0] = initialPos[0] + disp[0]
        newPos[1] = initialPos[1] + disp[1]
        newPos[2] = initialPos[2] + disp[2]
        good = False

print(newPos)
print(quat)
print(cog)
print(orient)
print(moi)
