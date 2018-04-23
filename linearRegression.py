import numpy as np 

def linearRegression(X, Y):
    """Input: X = nxd matrix Y = nx1 matrix
    Output: dx1 matrix"""
    XPinv = np.linalg.pinv(X)

    Wlin = XPinv * Y
    return Wlin

def makeMatrix(l):
    """Input: nxd list of lists
    Output: nxd matrix"""
    m = np.matrix(l)
    return m

def regress(x, y):
    """Input: x = nxd list of lists y = list of len = n
    Output: weight list"""
    X = makeMatrix(x)
    Y = makeMatrix(y).transpose()
    weight = linearRegression(X, Y)
    return weight.tolist()

def getValue(W, x):
    """Input: W = Weight Matrix x = feature matrix
    Output: y value"""
    y = 0
    for i in range(len(W)):
        y += W[i][0] * x[i]
    return y