import numpy as np

def rotation(qa):
    norm = np.sqrt(sum(np.square(qa)))
    qa = qa / norm

    print(qa)

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
    print(r)
    return r

def multiply(r, v):
    return np.dot(r,v)
    
testQ = np.array([2.5, 4.5, 6.5, 8.5])
testD = np.array([5.0, 5.0, 5.0])

rotated = rotation(testQ)
multiplied = multiply(rotated, testD)

print("\n")
print(multiplied)
